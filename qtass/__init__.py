from typing import Optional, Set, List, Dict, Any, Tuple, TypeVar
from enum import Enum, auto
import os
import json
import re
from pathlib import Path
import weakref
from dataclasses import dataclass
from PySide6.QtGui import (
    QIconEngine,
    QPixmap,
    QPainter,
    QImage,
    QIcon,
    QPalette,
    QColor,
    QFontDatabase,
    QPalette
)
from PySide6.QtCore import (
    QByteArray,
    QRect,
    QSize,
    Qt,
    QFileInfo,
    QXmlStreamReader,
    QObject,
    QDir,
    QFile,
    QIODevice,
)
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Signal, Slot
from PySide6.QtSvg import QSvgRenderer


tColorReplaceList = List[Tuple[str, str]]


class SvgIconEngine(QIconEngine):
    """
    An icon engine that supports loading SVG icons from a memory buffer,
    and updating their colors using an advanced stylesheet.
    """

    _instances: weakref.WeakSet["SvgIconEngine"] = weakref.WeakSet()

    def __init__(
        self,
        svg_content: QByteArray,
        advanced_stylesheet: Optional["QtAdvancedStylesheet"],
    ):
        """
        Initialize the icon engine with SVG content and an optional advanced stylesheet.

        Args:
            svg_content (QByteArray): The SVG data buffer.
            advanced_stylesheet (object): An object expected to have a replace_svg_colors method
                                          that modifies the SVG content in place.
        """
        super().__init__()
        self._svg_template: QByteArray = QByteArray(svg_content)
        self._svg_content: QByteArray = QByteArray()
        self._advanced_stylesheet = advanced_stylesheet

        self.update()
        SvgIconEngine._instances.add(self)

    def __del__(self):
        """
        Ensure the instance is removed from the global tracking set on deletion.
        Note: Python garbage collection may delay this or skip it entirely.
        """
        SvgIconEngine._instances.discard(self)

    def update(self) -> None:
        """
        Update the SVG content buffer by applying the current theme's icon colors.
        """
        self._svg_content = QByteArray(self._svg_template)
        if self._advanced_stylesheet and hasattr(
            self._advanced_stylesheet, "replace_svg_colors"
        ):
            self._advanced_stylesheet.replace_svg_colors(self._svg_content)

    @staticmethod
    def update_all_icons() -> None:
        """
        Update all icon engine instances by reapplying the theme-based transformations.
        """
        for engine in list(SvgIconEngine._instances):
            engine.update()

    def paint(
        self, painter: QPainter, rect: QRect, mode: QIcon.Mode, state: QIcon.State
    ) -> None:
        """
        Render the SVG content onto a QPainter within the given rectangle.

        Args:
            painter (QPainter): The painter to draw with.
            rect (QRect): The rectangle in which to draw.
            mode (QIcon.Mode): The icon display mode (not used).
            state (QIcon.State): The icon state (not used).
        """
        renderer = QSvgRenderer(self._svg_content)
        renderer.render(painter, rect)

    def clone(self) -> QIconEngine:
        """
        Create a copy of this icon engine.

        Returns:
            QIconEngine: A new instance with the same SVG content and stylesheet.
        """
        return SvgIconEngine(self._svg_template, self._advanced_stylesheet)

    def pixmap(self, size: QSize, mode: QIcon.Mode, state: QIcon.State) -> QPixmap:
        """
        Create a pixmap representation of the icon at the specified size and state.

        Args:
            size (QSize): The desired pixmap size.
            mode (QIcon.Mode): The icon mode (passed to paint).
            state (QIcon.State): The icon state (passed to paint).

        Returns:
            QPixmap: A transparent pixmap with the SVG content rendered into it.
        """
        image = QImage(size, QImage.Format_ARGB32)
        image.fill(Qt.transparent)
        pixmap = QPixmap.fromImage(image, Qt.NoFormatConversion)

        painter = QPainter(pixmap)
        self.paint(painter, QRect(0, 0, size.width(), size.height()), mode, state)
        painter.end()

        return pixmap


@dataclass
class PaletteColorEntry:
    """
    Represents a parsed palette color entry including its group, role, and associated color variable.
    """

    group: QPalette.ColorGroup = QPalette.ColorGroup.Active
    role: QPalette.ColorRole = QPalette.ColorRole.NoRole
    color_variable: str = ""

    def is_valid(self) -> bool:
        """
        Check if the color entry is valid.
        Returns:
            bool: True if the color variable is not empty and the role is not NoRole.
        """
        return bool(self.color_variable) and self.role != QPalette.ColorRole.NoRole



def color_role_from_string(text: str) -> QPalette.ColorRole:
    """
    Converts a string name to a QPalette.ColorRole enum.

    Args:
        text (str): The role name (e.g. "WindowText").

    Returns:
        QPalette.ColorRole: Corresponding enum or QPalette.NoRole if not matched.
    """
    color_role_map: Dict[str, QPalette.ColorRole] = {
        "WindowText": QPalette.ColorRole.WindowText,
        "Button": QPalette.ColorRole.Button,
        "Light": QPalette.ColorRole.Light,
        "Midlight": QPalette.ColorRole.Midlight,
        "Dark": QPalette.ColorRole.Dark,
        "Mid": QPalette.ColorRole.Mid,
        "Text": QPalette.ColorRole.Text,
        "BrightText": QPalette.ColorRole.BrightText,
        "ButtonText": QPalette.ColorRole.ButtonText,
        "Base": QPalette.ColorRole.Base,
        "Window": QPalette.ColorRole.Window,
        "Shadow": QPalette.ColorRole.Shadow,
        "Highlight": QPalette.ColorRole.Highlight,
        "HighlightedText": QPalette.ColorRole.HighlightedText,
        "Link": QPalette.ColorRole.Link,
        "LinkVisited": QPalette.ColorRole.LinkVisited,
        "AlternateBase": QPalette.ColorRole.AlternateBase,
        "ToolTipBase": QPalette.ColorRole.ToolTipBase,
        "ToolTipText": QPalette.ColorRole.ToolTipText,
        "NoRole": QPalette.ColorRole.NoRole,
    }
    # Add Qt 5.12+ role if available
    if hasattr(QPalette.ColorRole, "PlaceholderText"):
        color_role_map["PlaceholderText"] = QPalette.ColorRole.PlaceholderText
    return color_role_map.get(text, QPalette.ColorRole.NoRole)



K = TypeVar("K")
V = TypeVar("V")

def insert_into_map(target_map: Dict[K, V], source_map: Dict[K, V]) -> None:
    """
    Inserts key-value pairs from one map into another.

    Args:
        target_map (Dict[K, V]): The destination dictionary.
        source_map (Dict[K, V]): The dictionary to insert from.
    """
    target_map.update(source_map)


def color_group_string(color_group: QPalette.ColorGroup) -> str:
    """
    Converts a QPalette.ColorGroup enum to its corresponding lowercase string.

    Args:
        color_group (QPalette.ColorGroup): The color group enum.

    Returns:
        str: The string representation (e.g. "active", "disabled", or "inactive").
    """
    mapping = {
        QPalette.ColorGroup.Active: "active",
        QPalette.ColorGroup.Disabled: "disabled",
        QPalette.ColorGroup.Inactive: "inactive",
    }
    return mapping.get(color_group, "")


class QtAdvancedStylesheet(QObject):
    """
    Encapsulates all information about a single stylesheet-based style.
    """

    class Error(Enum):
        """
        Enumeration of possible stylesheet processing errors.
        """
        NO_ERROR = 0
        CSS_TEMPLATE_ERROR = auto()
        CSS_EXPORT_ERROR = auto()
        THEME_XML_ERROR = auto()
        STYLE_JSON_ERROR = auto()
        RESOURCE_GENERATOR_ERROR = auto()

    class Location(Enum):
        """
        An enumeration representing various resource locations within the application.

        Attributes:
            THEMES_LOCATION (int): Represents the location for theme resources.
            RESOURCE_TEMPLATES_LOCATION (int): Represents the location for resource templates.
            FONTS_LOCATION (int): Represents the location for font resources.
        """
        THEMES_LOCATION = 0
        RESOURCE_TEMPLATES_LOCATION = auto()
        FONTS_LOCATION = auto()

    # Signal emitted when the selected style changes
    current_style_changed = Signal(str)

    # Signal emitted when the selected theme within a style changes
    current_theme_changed = Signal(str)

    # Signal emitted when the stylesheet changes due to style, theme, or variable update
    stylesheet_changed = Signal()

    def __init__(self, parent: QObject | None = None):
        super().__init__(parent)
        self.styles_dir: str = ""
        self.output_dir: str = ""
        self.style_variables: Dict[str, str] = {}
        self.theme_colors: Dict[str, str] = {}
        self.theme_variables: Dict[
            str, str
        ] = {}  # theme variables = style_variables + theme_colors
        self.stylesheet: str = ""
        self._current_style: str = ""
        self._current_theme: str = ""
        self.default_theme: str = ""
        self.style_name: str = ""
        self.icon_file: str = ""
        self.resource_replace_list: List[Tuple[str, str]] = []
        self.palette_colors: List["PaletteColorEntry"] = []
        self.palette_base_color: str = ""
        self.json_style_param: Dict[str, Any] = {}
        self._error_string: str = ""
        self._error: "QtAdvancedStylesheet.Error" = QtAdvancedStylesheet.Error.NO_ERROR
        self.icon: QIcon = QIcon()
        self._styles: list[str] = []
        self._themes: list[str] = []
        self.is_dark_theme: bool = False
        self._icon_color_replace_list: "tColorReplaceList" = list()

    def __generate_stylesheet(self) -> bool:
        """
        Generate the final stylesheet from the stylesheet template file.
        Returns True on success, False otherwise.
        """
        css_template_file_name = self.json_style_param.get("css_template", "")
        if not css_template_file_name:
            return False

        template_file_path = os.path.join(
            self.current_style_path(), css_template_file_name
        )
        if not os.path.exists(template_file_path):
            self.__set_error(
                self.Error.CSS_TEMPLATE_ERROR,
                f"Stylesheet folder does not contain the CSS template file {css_template_file_name}",
            )
            return False

        try:
            with open(template_file_path, "r", encoding="utf-8") as file:
                content = file.read()
        except Exception as e:
            self.__set_error(
                self.Error.CSS_TEMPLATE_ERROR,
                f"Failed to read CSS template file: {str(e)}",
            )
            return False

        self.__replace_stylesheet_variables(content)
        self.stylesheet = content
        css_output_name = (
            os.path.splitext(os.path.basename(template_file_path))[0] + ".css"
        )
        self.__export_internal_stylesheet(css_output_name)
        return True

    def __export_internal_stylesheet(self, filename: str) -> bool:
        """
        Export the internal generated stylesheet to a file.

        Args:
            filename (str): The output filename.

        Returns:
            bool: Success status.
        """
        return self.__store_stylesheet(self.stylesheet, filename)

    def __store_stylesheet(self, stylesheet: str, filename: str) -> bool:
        """
        Store the given stylesheet content to the specified filename.
        """
        output_path = self.current_style_output_path()
        QDir().mkpath(output_path)  # Ensure the directory exists
        output_filename = output_path + "/" + filename

        output_file = QFile(output_filename)
        if not output_file.open(QIODevice.OpenModeFlag.WriteOnly):
            self.__set_error(
                self.Error.CSS_EXPORT_ERROR,
                f"Exporting stylesheet {filename} caused error: {output_file.errorString()}",
            )
            return False

        # Write the stylesheet as UTF-8 bytes
        output_file.write(QByteArray(bytes(stylesheet, "utf-8")))
        output_file.close()
        return True

    def __parse_variables_from_xml(
        self, reader: QXmlStreamReader, tag_name: str, variables: Dict[str, str]
    ) -> bool:
        """
        Parse a list of theme variables from an XML stream.
        """
        while reader.readNextStartElement():
            current_name = reader.name()
            if current_name != tag_name:
                self.__set_error(
                    self.Error.THEME_XML_ERROR,
                    f"Malformed theme file - expected tag <{tag_name}> instead of <{current_name}>",
                )
                return False

            name = reader.attributes().value("name")
            if not name:
                self.__set_error(
                    self.Error.THEME_XML_ERROR,
                    f"Malformed theme file - 'name' attribute missing in <{tag_name}> tag",
                )
                return False
            name_str = name  # PySide6 returns QString or str depending on binding

            value = reader.readElementText(QXmlStreamReader.ReadElementTextBehaviour.SkipChildElements)
            if not value:
                self.__set_error(
                    self.Error.THEME_XML_ERROR,
                    f"Malformed theme file - text of <{tag_name}> tag is empty",
                )
                return False

            variables[name_str] = value

        return True

    def __parse_theme_file(self, theme_filename: str) -> bool:
        """
        Parse the theme file given by filename.
        """
        theme_file_name = (
            self.path(QtAdvancedStylesheet.Location.THEMES_LOCATION) / theme_filename
        )
        theme_file = QFile(theme_file_name)
        if not theme_file.open(QIODevice.ReadOnly):
            self.__set_error(
                self.Error.THEME_XML_ERROR, f"Cannot open theme file: {theme_file_name}"
            )
            return False

        xml_reader = QXmlStreamReader(theme_file)
        xml_reader.readNextStartElement()
        if xml_reader.name() != "resources":
            self.__set_error(
                self.Error.THEME_XML_ERROR,
                f"Malformed theme file - expected tag <resources> instead of <{xml_reader.name()}>",
            )
            return False

        self.is_dark_theme = int(xml_reader.attributes().value("dark")) == 1

        color_variables: Dict[str, str] = {}
        if not self.__parse_variables_from_xml(xml_reader, "color", color_variables):
            # parse_variables_from_xml should set the error internally
            return False

        self.theme_variables = self.style_variables.copy()
        self.theme_variables.update(color_variables)
        self.theme_colors = color_variables

        return True

    def __parse_style_json_file(self) -> bool:
        """
        Parse the style JSON file.
        """
        style_path = Path(self.current_style_path())
        json_files = list(style_path.glob("*.json"))

        if len(json_files) < 1:
            self.__set_error(QtAdvancedStylesheet.Error.STYLE_JSON_ERROR,
                           "Stylesheet folder does not contain a style json file")
            return False

        if len(json_files) > 1:
            self.__set_error(QtAdvancedStylesheet.Error.STYLE_JSON_ERROR,
                           "Stylesheet folder contains multiple theme json files")
            return False

        try:
            with open(json_files[0], 'r', encoding='utf-8') as f:
                json_data = json.load(f)
        except Exception as e:
            self.__set_error(QtAdvancedStylesheet.Error.STYLE_JSON_ERROR,
                           f"Loading style json file caused error: {str(e)}")
            return False

        self.json_style_param = json_data
        self.style_name = json_data.get("name", "")
        if not self.style_name:
            self.__set_error(QtAdvancedStylesheet.Error.STYLE_JSON_ERROR,
                           'No key "name" found in style json file')
            return False

        variables = json_data.get("variables", {})
        if not isinstance(variables, dict):
            variables = {}

        # Convert all variables values to strings explicitly
        self.style_variables = {k: str(v) for k, v in variables.items()}

        self.icon_file = json_data.get("icon", "")
        self.__parse_palette_from_json()

        self.default_theme = json_data.get("default_theme", "")
        if not self.default_theme:
            self.__set_error(QtAdvancedStylesheet.Error.STYLE_JSON_ERROR,
                           'No key "default_theme" found in style json file')
            return False
        return True

    def __rgba_color(self, rgb_color: str, opacity: float) -> str:
        """
        Create an RGBA color string from a given RGB color string and opacity.

        Args:
            rgb_color (str): The base RGB color (e.g. "#ff0000").
            opacity (float): Opacity value from 0.0 (transparent) to 1.0 (opaque).

        Returns:
            str: The resulting RGBA color string.
        """
        alpha = int(255 * opacity)
        # Format alpha as a two-digit hexadecimal string, zero-padded
        alpha_hex = f"{alpha:02x}"
        # Insert alpha after the '#' character (at index 1)
        rgba_color = rgb_color[:1] + alpha_hex + rgb_color[1:]
        return rgba_color

    def __replace_stylesheet_variables(self, template: str) -> str:
        """
        Replace stylesheet variables in the given template string.
        """
        opacity_str = "opacity("
        pattern = re.compile(r"\{\{(.*?)\}\}")  # capture inside {{...}}

        def replace_match(match: re.Match) -> str:
            template_variable = match.group(1)
            if template_variable.endswith(')'):
                var_name, opacity_expr = template_variable.split('|')
                value = self.theme_variable_value(var_name)
                try:
                    opacity = float(opacity_expr[len(opacity_str):-1])
                except ValueError:
                    opacity = 1.0
                return self.__rgba_color(value, opacity)
            else:
                return self.theme_variable_value(template_variable)

        return pattern.sub(replace_match, template)

    def __add_fonts(self, dir: Optional["QDir"] = None) -> None:
        """
        Register style fonts to the font database.

        Args:
            directory (Optional[QDir]): Directory containing fonts. If None, defaults used.
        """
        # Return early if no widgets are present, to avoid potential crashes
        app = QApplication.instance()
        if app is None or not isinstance(app, QApplication) or not app.allWidgets():
            return

        if dir is None:
            fonts_dir = QDir(self.path(QtAdvancedStylesheet.Location.FONTS_LOCATION))
            self.__add_fonts(fonts_dir)
        else:
            # Recursively add fonts from subdirectories
            for folder in dir.entryList(QDir.Filter.Dirs | QDir.Filter.NoDotAndDotDot):
                if dir.cd(folder):
                    self.__add_fonts(dir)
                    dir.cdUp()

            # Add all .ttf font files from this directory
            for font_file in dir.entryList(["*.ttf"], QDir.Filter.Files):
                font_path = dir.absoluteFilePath(font_file)
                QFontDatabase.addApplicationFont(font_path)

    def __generate_resources_for(
        self, sub_dir: str, json_object: Dict[str, Any], entries: List[QFileInfo]
    ) -> bool:
        """
        Generate resources for various states from JSON and file entries.
        """
        output_dir = self.current_style_output_path() + "/" + sub_dir
        if not QDir().mkpath(output_dir):
            self.__set_error(self.Error.RESOURCE_GENERATOR_ERROR, f"Error creating resource output folder: {output_dir}")
            return False

        color_replace_list = self.__parse_color_replace_list(json_object)

        for entry in entries:
            svg_file = QFile(entry.absoluteFilePath())
            if not svg_file.open(QIODevice.OpenModeFlag.ReadOnly):
                self.__set_error(self.Error.RESOURCE_GENERATOR_ERROR, f"Failed to open SVG file: {entry.fileName()}")
                return False

            content = svg_file.readAll()
            svg_file.close()

            self.replace_svg_colors(content, color_replace_list)

            output_filename = output_dir + "/" + entry.fileName()
            output_file = QFile(output_filename)
            if not output_file.open(QIODevice.OpenModeFlag.WriteOnly):
                self.__set_error(self.Error.RESOURCE_GENERATOR_ERROR, f"Failed to open output file: {output_filename}")
                return False

            output_file.write(content)
            output_file.close()

        return True

    def __replace_color(
        self, content: QByteArray, template_color: str, theme_color: str
    ) -> None:
        """
        Replace all occurrences of template_color in content with theme_color.

        Args:
            content (bytes): The content to modify.
            template_color (str): The color string to replace.
            theme_color (str): The replacement color string.

        Returns:
            bytes: The modified content.
        """
        content.replace(template_color.encode('latin1'), theme_color.encode('latin1'))
        return

    def __set_error(
        self, error: "QtAdvancedStylesheet.Error", error_string: str
    ) -> None:
        """
        Set the current error code and string.
        """
        self._error = error
        self._error_string = error_string

    def __clear_error(self) -> None:
        """
        Clear the current error state.
        """
        self.__set_error(QtAdvancedStylesheet.Error.NO_ERROR, "")

    def __parse_palette_from_json(self) -> None:
        """
        Parse palette data from a JSON file.
        """
        self.palette_base_color = ""
        self.palette_colors.clear()

        palette = self.json_style_param.get("palette", {})
        if not palette:
            return

        self.palette_base_color = palette.get("base_color", "")
        self.__parse_palette_color_group(palette, QPalette.ColorGroup.Active)
        self.__parse_palette_color_group(palette, QPalette.ColorGroup.Disabled)
        self.__parse_palette_color_group(palette, QPalette.ColorGroup.Inactive)

    def __parse_palette_color_group(self, j_palette: Dict[str, Any], color_group: QPalette.ColorGroup) -> None:
        """
        Parse color roles for a given palette color group from a JSON-like dictionary.

        Args:
            j_palette (Dict[str, Any]): The parsed JSON palette object.
            color_group (QPalette.ColorGroup): The color group to process (Active, Disabled, Inactive).
        """
        group_name = color_group_string(color_group)
        j_color_group = j_palette.get(group_name, {})

        if not j_color_group:
            return

        for role_name, color_value in j_color_group.items():
            color_role = color_role_from_string(role_name)
            if color_role == QPalette.ColorRole.NoRole:
                continue

            self.palette_colors.append(PaletteColorEntry(group=color_group, role=color_role, color_variable=str(color_value)))

            # Note: The C++ version doesn't do anything inside this "if" block.
            # If logic is needed here for Active group, implement it.
            if color_group != QPalette.ColorGroup.Active:
                continue

    def __icon_color_replace_list(self) -> "tColorReplaceList":
        """
        Accessor for the icon color replace list, ensures proper initialization.
        """
        return self._icon_color_replace_list

    def __parse_color_replace_list(
        self, json_object: Dict[str, Any]
    ) -> "tColorReplaceList":
        """
        Parse a color replace list from the given JSON object.
        """
        raise NotImplementedError

    def set_styles_dir_path(self, dir_path: str) -> None:
        """
        Sets the directory path where styles are located and populates
        the list of style directories (excluding '.' and '..').

        Args:
            dir_path (str): The path to the styles directory.
        """
        self.styles_dir = dir_path

        if os.path.isdir(self.styles_dir):
            # List subdirectories only, excluding '.' and '..'
            self._styles = [
                name for name in os.listdir(self.styles_dir)
                if os.path.isdir(os.path.join(self.styles_dir, name))
            ]
        else:
            self._styles = []

    def styles_dir_path(self) -> str:
        """
        Get the currently set styles directory path.

        Returns:
            str: The styles directory path.
        """
        return self.styles_dir

    def current_style(self) -> str:
        """
        Get the name of the current style.

        Returns:
            str: The current style name.
        """
        return self._current_style

    def current_style_path(self) -> Path:
        """
        Get the absolute path of the current style directory.

        Returns:
            Path: Absolute path to the current style.
        """
        return Path(self.styles_dir) / self._current_style

    def styles(self) -> List[str]:
        """
        Get the list of available styles in the styles directory.

        Returns:
            List[str]: List of style names.
        """
        return self._styles

    def themes(self) -> List[str]:
        """
        Get the list of all themes available for the current style.

        Returns:
            List[str]: List of theme names; empty if no style set.
        """
        return self._themes

    def theme_color_variables(self) -> Dict[str, str]:
        """
        Get all theme variables related to colors.

        Returns:
            Dict[str, str]: Dictionary mapping variable names to color values.
        """
        raise NotImplementedError

    def path(self, location: Location) -> Path:
        """
        Get the absolute directory path for the specified location.

        Args:
            location (Location): One of the Location enum values.

        Returns:
            Path: The absolute path corresponding to the location.
        """
        paths = {
            self.Location.THEMES_LOCATION: "themes",
            self.Location.RESOURCE_TEMPLATES_LOCATION: "resources",
            self.Location.FONTS_LOCATION: "fonts",
        }

        subdir = paths.get(location)
        return Path(self.current_style_path()) / subdir if subdir else Path()


    def current_style_output_path(self) -> Path:
        """
        Get the output path for the current style.

        Returns:
            Path: Output path for the current style.
        """
        return Path(self.output_dir) / self._current_style

    def theme_variable_value(self, variable_id: str) -> str:
        """
        Get the value of a given theme variable.

        Args:
            variable_id (str): The theme variable identifier.

        Returns:
            str: Variable value or empty string if not found.
        """
        raise NotImplementedError

    def set_theme_variable_value(self, variable_id: str, value: str) -> None:
        """
        Add or overwrite a theme variable's value.

        Args:
            variable_id (str): The theme variable identifier.
            value (str): The new value to assign.
        """
        raise NotImplementedError

    def theme_color(self, variable_id: str) -> QColor:
        """
        Get a QColor from the theme's color mapping by variable ID.

        Args:
            variable_id (str): The color variable identifier.

        Returns:
            QColor: The corresponding color, or an invalid QColor if not found.
        """
        color_string = self.theme_colors.get(variable_id, "")
        if not color_string:
            return QColor()  # Invalid color
        return QColor(color_string)


    def process_stylesheet_template(self, template: str, output_file: str = "") -> str:
        """
        Replace style variables in the given template with registered style variables.

        Args:
            template (str): Stylesheet template content.
            output_file (str): Optional output filename to store generated stylesheet.

        Returns:
            str: Final processed stylesheet or empty string on error.
        """
        raise NotImplementedError

    def style_icon(self) -> QIcon:
        """
        Get the icon for the current style.

        Returns:
            QIcon: The style icon, or empty QIcon if none.
        """
        raise NotImplementedError

    def error(self) -> int:
        """
        Get the current error code.

        Returns:
            int: Current error code (eError enum).
        """
        raise NotImplementedError

    def error_string(self) -> str:
        """
        Get a string describing the last error.

        Returns:
            str: Last error description.
        """
        raise NotImplementedError

    def generate_theme_palette(self) -> QPalette:
        """
        Generate a QPalette based on the current theme's palette configuration.

        Returns:
            QPalette: The theme-based color palette.
        """
        app = QApplication.instance()
        if isinstance(app, QApplication):
            palette: QPalette = app.palette()
        else:
            palette: QPalette = QPalette()

        if self.palette_base_color:
            color: QColor = self.theme_color(self.palette_base_color)
            if color.isValid():
                palette = QPalette(color)

        for entry in self.palette_colors:
            color = self.theme_color(entry.color_variable)
            if color.isValid():
                palette.setColor(entry.group, entry.role, color)
        return palette

    def style_parameters(self) -> Dict[str, Any]:
        """
        Get access to the style parameters as a JSON-like dictionary.

        Returns:
            Dict[str, Any]: Style parameters.
        """
        raise NotImplementedError

    def is_current_theme_dark(self) -> bool:
        """
        Check if the current theme is a dark theme.

        Returns:
            bool: True if dark theme, False if light theme.
        """
        raise NotImplementedError

    def replace_svg_colors(
        self,
        svg_content: QByteArray,
        color_replace_list: Optional[List[Tuple[str, str]]] = None,
    ) -> None:
        """
        Replace SVG colors in the provided SVG content with theme colors.

        Args:
            svg_content (QByteArray): The SVG data to modify.
            color_replace_list (Optional[List[Tuple[str, str]]]): Optional list of color replacements.
        """
        raise NotImplementedError

    def load_theme_aware_svg_icon(self, filename: str) -> QIcon:
        """
        Load SVG data from the given filename and replace colors according to the current theme.

        Args:
            filename (str): Path to the SVG file.

        Returns:
            QIcon: The themed SVG icon.
        """
        raise NotImplementedError

    # Slots

    def set_current_theme(self, theme: str) -> bool:
        """
        Set the current theme if the theme JSON is valid and the theme file can be parsed.

        Args:
            theme (str): The name of the theme to set.

        Returns:
            bool: True if the theme was set successfully, False otherwise.
        """
        self.__clear_error()

        if not self.json_style_param:
            return False

        if not self.__parse_theme_file(f"{theme}.xml"):
            return False

        self._current_theme = theme
        self.current_theme_changed.emit(self._current_theme)
        return True

    def set_default_theme(self) -> None:
        """
        Set the default theme specified in the style JSON file.
        """
        self.set_current_theme(self.default_theme)

    def set_current_style(self, style: str) -> bool:
        """
        Set the current style and trigger related updates.

        Args:
            style (str): Name of the style to activate.

        Returns:
            bool: True if the style was successfully loaded, False otherwise.
        """
        self.__clear_error()
        self._current_style = style

        themes_path = Path(self.path(self.Location.THEMES_LOCATION))
        xml_files = themes_path.glob("*.xml")
        self._themes: List[str] = [f.stem for f in xml_files]

        result = self.__parse_style_json_file()

        # Replace QDir.addSearchPath with a method or global mechanism as needed
        #icon_path = self.current_style_output_path()
        #os.environ["ICON_PATH"] = icon_path  # or another method to inject into search paths
        QDir.addSearchPath("icon", self.current_style_output_path())

        self.__add_fonts()

        #self.current_style_changed.emit(self._current_style)
        #self.stylesheet_changed.emit()

        return result

    def update_stylesheet(self) -> bool:
        """
        Update the stylesheet by processing the style template, refreshing icons,
        and generating the final stylesheet. Emits `stylesheetChanged` signal upon success.

        Returns:
            bool: True if the stylesheet was updated successfully, False otherwise.
        """
        if not self.process_style_template():
            return False

        self._icon_color_replace_list.clear()
        SvgIconEngine.update_all_icons()

        if not self.__generate_stylesheet() and self.error() != QtAdvancedStylesheet.Error.NO_ERROR:
            return False

        self.stylesheet_changed.emit()
        return True

    def process_style_template(self) -> bool:
        """
        Update SVG files and application palette without generating the stylesheet.

        Returns:
            bool: True if successful, False otherwise.
        """
        self.update_application_palette_colors()
        return self.generate_resources()

    def generate_resources(self) -> bool:
        """
        Generate the required icons and SVG resources for the current theme.

        Returns:
            bool: True if successful, False otherwise.
        """
        raise NotImplementedError

    def update_application_palette_colors(self) -> None:
        """
        Update the application's palette colors using the generated theme palette.
        """
        app = QApplication.instance()
        if isinstance(app, QApplication):  # Ensure it's a QApplication
            app.setPalette(self.generate_theme_palette())
