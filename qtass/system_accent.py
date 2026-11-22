"""System accent color observation, independent of the palette applied by QtASS."""

import logging
import sys

from PySide6.QtCore import QObject, Qt, Signal, Slot
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

_LOGGER = logging.getLogger(__name__)


class AccentProvider(QObject):
    """GUI-thread provider contract for native or application-supplied accent colors."""

    changed = Signal(QColor)

    def color(self) -> QColor:
        """Return the current color, or invalid QColor if the source is unavailable."""
        raise NotImplementedError


class SystemAccentProvider(AccentProvider):
    """Capture native palette fallback and observe Windows UISettings changes.

    Construct before applying an application stylesheet. Windows events cross a
    queued Qt signal; callbacks never mutate GUI state on a WinRT event thread.
    Call close() before application shutdown to release the native subscription.
    """

    _refresh_requested = Signal()

    def __init__(self, parent: QObject | None = None) -> None:
        """Capture the initial platform accent without changing system preferences."""
        super().__init__(parent)
        app = QApplication.instance()
        self._fallback = QColor(app.palette().color(QPalette.ColorRole.Accent)) if app else QColor()
        self._color = QColor(self._fallback)
        self._settings = None
        self._event_token = None
        self._closed = False
        self._refresh_requested.connect(self._refresh, Qt.ConnectionType.QueuedConnection)
        if sys.platform == "win32":
            try:
                from winrt.windows.ui.viewmanagement import UISettings, UIColorType
                self._accent_type = UIColorType.ACCENT
                self._settings = UISettings()
                self._event_token = self._settings.add_color_values_changed(self._windows_changed)
                self._refresh()
            except (ImportError, OSError, RuntimeError) as error:
                _LOGGER.warning("Windows accent unavailable; using initial Qt palette: %s", error)
        if app is not None:
            app.aboutToQuit.connect(self.close)
        if parent is not None:
            parent.destroyed.connect(self.close)

    def color(self) -> QColor:
        """Return a copy so callers cannot mutate the provider's cached color."""
        return QColor(self._color)

    def _windows_changed(self, sender: object, arguments: object) -> None:
        """Forward native notifications without touching Qt palette or style objects."""
        if not self._closed:
            self._refresh_requested.emit()

    @Slot()
    def _refresh(self) -> None:
        """Read native color on the QObject thread, emitting only real changes."""
        if self._closed or self._settings is None:
            return
        try:
            native = self._settings.get_color_value(self._accent_type)
            color = QColor(native.r, native.g, native.b, native.a)
        except (OSError, RuntimeError) as error:
            _LOGGER.warning("Could not refresh Windows accent: %s", error)
            return
        if color.isValid() and color != self._color:
            self._color = color
            self.changed.emit(QColor(color))

    @Slot()
    def close(self) -> None:
        """Unsubscribe once; delayed events become harmless after shutdown."""
        if self._closed:
            return
        self._closed = True
        if self._settings is not None and self._event_token is not None:
            try:
                self._settings.remove_color_values_changed(self._event_token)
            except (OSError, RuntimeError):
                _LOGGER.debug("Windows accent subscription already unavailable.", exc_info=True)
        self._event_token = None
        self._settings = None
