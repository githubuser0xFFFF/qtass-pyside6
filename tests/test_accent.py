"""Accent policy, palette/CSS propagation and native provider regression tests."""

import sys
import tempfile
import unittest
from pathlib import Path

from PySide6.QtCore import QThread
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QWidget

from qtass import AccentSource, QtAdvancedStylesheet, color_role_from_string
from qtass.system_accent import AccentProvider, SystemAccentProvider

_APP = QApplication.instance() or QApplication(["qtass-release-tests"])


class FakeProvider(AccentProvider):
    """Supply deterministic system colors without changing Windows settings."""

    def __init__(self) -> None:
        super().__init__()
        self.value = QColor("#0067c0")

    def color(self) -> QColor:
        return QColor(self.value)

    def change(self, value: str) -> None:
        self.value = QColor(value)
        self.changed.emit(QColor(self.value))


class AccentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.provider = FakeProvider()
        self.style = QtAdvancedStylesheet(accent_provider=self.provider)
        self.style.output_dir = self.directory.name
        self.style.set_current_style("metro")
        self.assertTrue(self.style.set_current_theme("dark_orange"))

    def tearDown(self) -> None:
        self.style.deleteLater()
        self.provider.deleteLater()
        _APP.processEvents()
        self.directory.cleanup()

    def test_default_and_theme_return_value(self) -> None:
        self.assertEqual(self.style.accent_source, AccentSource.THEME)
        self.assertEqual(self.style.accent_color().name(), "#f78a09")
        self.assertEqual(self.style._current_theme, "dark_orange")
        changes: list[str] = []
        self.style.current_theme_changed.connect(changes.append)
        self.assertTrue(self.style.set_current_theme("light_orange"))
        self.assertEqual(changes, ["light_orange"])

    def test_custom_survives_switch_and_updates_css_palette_resources(self) -> None:
        self.style.set_accent_color("#4169e1")
        self.assertEqual(self.style.accent_source, AccentSource.CUSTOM)
        self.assertEqual(_APP.palette().color(QPalette.ColorRole.Highlight).name(), "#4169e1")
        self.assertEqual(_APP.palette().color(QPalette.ColorRole.Accent).name(), "#4169e1")
        self.assertIn("#4169e1", self.style.stylesheet.lower())
        self.assertEqual(_APP.styleSheet(), self.style.stylesheet)
        generated = list(Path(self.directory.name).rglob("*.svg"))
        self.assertTrue(generated)
        self.assertTrue(any("#4169e1" in path.read_text().lower() for path in generated))
        self.style.set_current_theme("light_orange")
        self.style.update_stylesheet()
        self.assertEqual(self.style.accent_color().name(), "#4169e1")
        self.style.set_accent_source(AccentSource.THEME)
        self.assertEqual(self.style.accent_color().name(), "#f78a09")

    def test_legacy_variable_assignment_is_persistent_custom(self) -> None:
        self.style.set_theme_variable_value("accentColor", "#112233")
        self.style.set_current_theme("light_orange")
        self.style.update_stylesheet()
        self.assertEqual(self.style.theme_variable_value("accentColor"), "#112233")

    def test_system_changes_only_affect_system_mode(self) -> None:
        self.style.set_accent_source(AccentSource.SYSTEM)
        self.assertEqual(self.style.accent_color().name(), "#0067c0")
        changes: list[str] = []
        self.style.accent_color_changed.connect(lambda color: changes.append(color.name()))
        self.provider.change("#aabbcc")
        self.assertEqual(self.style.accent_color().name(), "#aabbcc")
        self.assertEqual(changes, ["#aabbcc"])
        self.style.set_current_theme("light_orange")
        self.style.update_stylesheet()
        self.assertEqual(self.style.accent_color().name(), "#aabbcc")
        self.style.set_accent_color("#abcdef")
        self.provider.change("#123456")
        self.assertEqual(self.style.accent_color().name(), "#abcdef")
        self.style.set_accent_source(AccentSource.SYSTEM)
        self.assertEqual(self.style.accent_color().name(), "#123456")

    def test_unavailable_system_uses_current_theme(self) -> None:
        self.provider.value = QColor()
        self.style.set_accent_source(AccentSource.SYSTEM)
        self.assertEqual(self.style.accent_color().name(), "#f78a09")

    def test_invalid_values_do_not_change_state(self) -> None:
        with self.assertRaises(ValueError):
            self.style.set_accent_color("not a color")
        with self.assertRaises(ValueError):
            self.style.set_accent_source(AccentSource.CUSTOM)
        with self.assertRaises(TypeError):
            self.style.set_accent_source("system")
        self.assertEqual(self.style.accent_source, AccentSource.THEME)
        self.assertEqual(color_role_from_string("Accent"), QPalette.ColorRole.Accent)

    def test_initialization_with_existing_widgets(self) -> None:
        widget = QWidget()
        other = QtAdvancedStylesheet(accent_provider=self.provider)
        other.output_dir = self.directory.name
        other.set_current_style("metro")
        self.assertTrue(other.set_current_theme("dark_orange"))
        widget.close()
        widget.deleteLater()
        other.deleteLater()


class NativeProviderTests(unittest.TestCase):
    @unittest.skipUnless(sys.platform == "win32", "Requires Windows UISettings")
    def test_actual_windows_provider_and_close(self) -> None:
        provider = SystemAccentProvider()
        try:
            self.assertTrue(provider.color().isValid())
            self.assertIsNotNone(provider._event_token)
            observed: list[QThread] = []
            provider.changed.connect(lambda color: observed.append(QThread.currentThread()))
            provider._color = QColor("#010203")
            provider._windows_changed(None, None)
            _APP.processEvents()
            self.assertTrue(observed)
            self.assertTrue(all(thread == _APP.thread() for thread in observed))
            provider.close()
            provider.close()
            self.assertIsNone(provider._event_token)
        finally:
            provider.close()


if __name__ == "__main__":
    unittest.main()
