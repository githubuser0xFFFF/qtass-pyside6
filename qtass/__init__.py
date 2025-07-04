from typing import Optional, List, Dict, Any, Tuple, TypeVar, Union
from enum import Enum, auto
import os
import json
from pathlib import Path
import weakref
import jinja2
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


class QtAdvancedStylesheetError(Exception):
    """Base exception for all stylesheet errors."""
    pass

class CssTemplateError(QtAdvancedStylesheetError):
    """Raised when there is a CSS template processing error."""
    pass

class CssExportError(QtAdvancedStylesheetError):
    """Raised when stylesheet export fails."""
    pass

class ThemeXmlError(QtAdvancedStylesheetError):
    """Raised when there is an error parsing the theme XML."""
    pass

class StyleJsonError(QtAdvancedStylesheetError):
    """Raised when there is an error in the style JSON."""
    pass

class ResourceGeneratorError(QtAdvancedStylesheetError):
    """Raised when resource generation fails."""
    pass


def jinja2_filter_opacity(theme, value=0.5):
    """
    Converts a hex color string from a theme into an RGBA color string with the specified opacity.
    Args:
        theme (str): A hex color string (e.g., "#RRGGBB").
        value (float, optional): The opacity value for the RGBA color (default is 0.5).
    Returns:
        str: The color in "rgba(r, g, b, value)" format suitable for CSS.
    Example:
        >>> jinja2_filter_opacity("#FFAA33", 0.8)
        'rgba(255, 170, 51, 0.8)'
    """
    r, g, b = theme[1:][0:2], theme[1:][2:4], theme[1:][4:]
    r, g, b = int(r, 16), int(g, 16), int(b, 16)

    return f"rgba({r}, {g}, {b}, {value})"


def jinja2_filter_density(value, density_scale, border=0, scale=1, density_interval=4, min_=4):
    """
    Calculates a density value for UI elements based on input value, density scale, border, and other parameters.
    Args:
        value (str|float|int): The base value to be adjusted. Can be a string (e.g., "16px", "@icon") or a numeric value.
        density_scale (int|float): The density scale factor to apply.
        border (int|float, optional): The border width to subtract from the calculation. Defaults to 0.
        scale (int|float, optional): A multiplier to scale the final density value. Defaults to 1.
        density_interval (int|float, optional): The interval to use for density scaling. Defaults to 4.
        min_ (int|float, optional): The minimum value to return if the calculated density is less than or equal to zero. Defaults to 4.
    Returns:
        float|str: The calculated density value, or a string if the input value is a special case (e.g., starts with "@" or is "unset").
    Notes:
        - If `value` is a string starting with "@", returns the string without "@" repeated `scale` times.
        - If `value` is "unset", returns "unset".
        - If the calculated density is less than or equal to zero, returns `min_`.
    """
    # https://material.io/develop/web/supporting/density
    if isinstance(value, str) and value.startswith("@"):
        return value[1:] * scale

    if value == "unset":
        return "unset"

    if isinstance(value, str):
        value = float(value.replace("px", ""))

    density = (value + (density_interval * int(density_scale)) - (border * 2)) * scale

    if density <= 0:
        density = min_
    return density


class QtAdvancedStylesheet(QObject):
    """
    Encapsulates all information about a single stylesheet-based style.
    """

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
        self.styles_dir: Path = Path(__file__).parent / "styles"
        self.output_dir: str = ""
        self.style_variables: Dict[str, str] = {}
        self.theme_color_variables: Dict[str, str] = {}
        self.theme_variables: Dict[str, str] = {}  # theme variables = style_variables + theme_colors
        self.stylesheet: str = ""
        self.current_style: str = ""
        self._current_theme: str = ""
        self.default_theme: str = ""
        self.style_name: str = ""
        self.icon_file: str = ""
        self.resource_replace_list: List[Tuple[str, str]] = []
        self.palette_colors: List["PaletteColorEntry"] = []
        self.palette_base_color: str = ""
        self.json_style_param: Dict[str, Any] = {}
        self.icon: QIcon = QIcon()
        self.styles: list[str] = []
        self.themes: list[str] = []
        self.is_dark_theme: bool = False
        self._icon_color_replace_list: "tColorReplaceList" = list()


    def __generate_stylesheet(self) -> None:
        """
        Generate the final stylesheet from the stylesheet template file.
        Returns True on success, False otherwise.
        """
        css_template_file_name = self.json_style_param.get("css_template", "")
        if not css_template_file_name:
             raise CssTemplateError('Missing required "css_template" key in the style JSON.')

        template_file_path = os.path.join(
            self.current_style_path(), css_template_file_name
        )
        if not os.path.exists(template_file_path):
            raise CssTemplateError(
                f"Stylesheet folder does not contain the CSS template file {css_template_file_name}"
            )

        parent, template = os.path.split(template_file_path)
        loader = jinja2.FileSystemLoader(parent)
        self.stylesheet = self.__render_stylesheet_template(template, loader)
        css_output_name = (
            os.path.splitext(os.path.basename(template_file_path))[0] + ".css"
        )
        self.__export_internal_stylesheet(css_output_name)
        return

    def __render_stylesheet_template(self, template_name: str, loader : jinja2.BaseLoader) -> str:
        """
        Renders a stylesheet template using Jinja2 with custom filters and theme variables.

        Args:
            template (str): The name of the Jinja2 template file to render.
            loader (jinja2.BaseLoader): The Jinja2 template loader instance.

        Side Effects:
            Sets the rendered stylesheet to the `self.stylesheet` attribute.

        Filters:
            - "opacity": Uses the `jinja2_filter_opacity` function.
            - "density": Uses the `jinja2_filter_density` function.

        """
        env = jinja2.Environment(autoescape=False, loader=loader)
        env.filters["opacity"] = jinja2_filter_opacity
        env.filters["density"] = jinja2_filter_density
        template = env.get_template(template_name)
        return template.render(self.theme_variables)
    

    def __export_internal_stylesheet(self, filename: str) -> None:
        """
        Export the internal generated stylesheet to a file.

        Args:
            filename (str): The output filename.

        Returns:
            bool: Success status.
        """
        return self.__store_stylesheet(self.stylesheet, filename)


    def __store_stylesheet(self, stylesheet: str, filename: str) -> None:
        """
        Store the given stylesheet content to the specified filename.
        """
        output_path = self.current_style_output_path()
        Path(output_path).mkdir(parents=True, exist_ok=True)
        output_filename = output_path / filename

        output_file = QFile(output_filename)
        if not output_file.open(QIODevice.OpenModeFlag.WriteOnly):
            raise CssExportError(
                f"Exporting stylesheet {filename} caused error: {output_file.errorString()}"
            )

        # Write the stylesheet as UTF-8 bytes
        output_file.write(QByteArray(bytes(stylesheet, "utf-8")))
        output_file.close()


    def __parse_variables_from_xml(
        self, reader: QXmlStreamReader, tag_name: str, variables: Dict[str, str]
    ) -> None:
        """
        Parse a list of theme variables from an XML stream.
        """
        while reader.readNextStartElement():
            current_name = reader.name()
            if current_name != tag_name:
                raise ThemeXmlError(
                    f"Malformed theme file - expected tag <{tag_name}> instead of <{current_name}>"
                )

            name = reader.attributes().value("name")
            if not name:
                raise ThemeXmlError(
                    f"Malformed theme file - 'name' attribute missing in <{tag_name}> tag"
                )
            name_str = name  # PySide6 returns QString or str depending on binding

            value = reader.readElementText(QXmlStreamReader.ReadElementTextBehaviour.SkipChildElements)
            if not value:
                raise ThemeXmlError(
                    f"Malformed theme file - text of <{tag_name}> tag is empty"
                )

            variables[name_str] = value


    def __parse_theme_file(self, theme_filename: str) -> None:
        """
        Parse the theme file given by filename.
        """
        theme_file_name = (
            self.path(QtAdvancedStylesheet.Location.THEMES_LOCATION) / theme_filename
        )
        theme_file = QFile(theme_file_name)
        if not theme_file.open(QIODevice.ReadOnly):
            raise ThemeXmlError(f"Cannot open theme file: {theme_file_name}")

        xml_reader = QXmlStreamReader(theme_file)
        xml_reader.readNextStartElement()
        if xml_reader.name() != "resources":
            raise ThemeXmlError(
                f"Malformed theme file - expected tag <resources> instead of <{xml_reader.name()}>"
            )

        dark_attr = xml_reader.attributes().value("dark")
        if not dark_attr:
            # Fallback: check if filename starts with 'dark' (case-insensitive)
            self.is_dark_theme = theme_filename.lower().startswith("dark")
        else:
            self.is_dark_theme = int(dark_attr) == 1

        color_variables: Dict[str, str] = {}
        self.__parse_variables_from_xml(xml_reader, "color", color_variables)
        self.theme_variables = self.style_variables.copy()
        self.theme_variables.update(color_variables)
        self.theme_color_variables = color_variables
        return


    def __parse_style_json_file(self) -> None:
        """
        Parse the style JSON file.
        """
        style_path = Path(self.current_style_path())
        json_files = list(style_path.glob("*.json"))

        if not json_files:
            raise StyleJsonError("Stylesheet folder does not contain a style JSON file")

        if len(json_files) > 1:
            raise StyleJsonError("Stylesheet folder contains multiple theme JSON files")

        try:
            with open(json_files[0], 'r', encoding='utf-8') as f:
                json_data = json.load(f)
        except Exception as e:
            raise StyleJsonError(f"Loading style JSON file caused error: {str(e)}") from e

        self.json_style_param = json_data
        self.style_name = json_data.get("name", "")
        if not self.style_name:
            raise StyleJsonError('No key "name" found in style JSON file')

        variables = json_data.get("variables", {})
        if not isinstance(variables, dict):
            variables = {}

        # Convert all variables values to strings explicitly
        self.style_variables = {k: str(v) for k, v in variables.items()}

        self.icon_file = json_data.get("icon", "")
        self.__parse_palette_from_json()

        self.default_theme = json_data.get("default_theme", "")
        if not self.default_theme:
            raise StyleJsonError('No key "default_theme" found in style JSON file')


    def __add_fonts(self, fonts_dir: Optional["QDir"] = None) -> None:
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
    ) -> None:
        """
        Generate resources for various states from JSON and file entries.

        Raises:
            ResourceGenerationError: If resource output folder creation, reading SVGs, or writing output fails.
        """
        output_dir = self.current_style_output_path() / sub_dir
        if not QDir().mkpath(str(output_dir)):
            raise ResourceGeneratorError(f"Error creating resource output folder: {output_dir}")

        color_replace_list = self.__parse_color_replace_list(json_object)

        for entry in entries:
            svg_file = QFile(entry.absoluteFilePath())
            if not svg_file.open(QIODevice.OpenModeFlag.ReadOnly):
                raise ResourceGeneratorError(f"Failed to open SVG file: {entry.fileName()}")

            content = svg_file.readAll()
            svg_file.close()

            self.replace_svg_colors(content, color_replace_list)

            output_filename = output_dir / entry.fileName()
            output_file = QFile(output_filename)
            if not output_file.open(QIODevice.OpenModeFlag.WriteOnly):
                raise ResourceGeneratorError(f"Failed to open output file: {output_filename}")

            output_file.write(content)
            output_file.close()
    
    @staticmethod
    def __replace_color(content: QByteArray, template_color: str, theme_color: str) -> None:
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
            if color_role != QPalette.ColorRole.NoRole:
                self.palette_colors.append(PaletteColorEntry(group=color_group, role=color_role, color_variable=str(color_value)))


    def __parse_color_replace_list(
        self, json_object: Dict[str, str]
    ) -> "tColorReplaceList":
        """
        Parses a JSON object describing color replacements.

        Args:
            json_object (Dict[str, str]): A dictionary mapping template color strings to theme color variables or values.

        Returns:
            List[Tuple[str, str]]: A list of (template_color, theme_color) pairs.
        """
        color_replace_list: tColorReplaceList = []

        for template_color, theme_color in json_object.items():
            if not theme_color.startswith("#"):
                theme_color = self.theme_variable_value(theme_color)
            color_replace_list.append((template_color, theme_color))

        return color_replace_list


    def set_styles_dir_path(self, dir_path: Union[str, Path]) -> None:
        """
        Sets the directory path where style subdirectories are located.
        Args:
            dir_path (Path): The path to the directory containing style subdirectories.
        Raises:
            NotADirectoryError: If the provided path is not a directory.
        Side Effects:
            - Updates the `styles_dir` attribute with the given directory path.
            - Populates the `_styles` attribute with the names of all subdirectories within the given directory.
        """
        path = Path(dir_path)
        if not path.is_dir():
            raise NotADirectoryError(f"The given path '{path}' is not a directory.")

        self.styles_dir = path
        self.styles = [p.name for p in path.iterdir() if p.is_dir()]


    def current_style_path(self) -> Path:
        """
        Get the absolute path of the current style directory.

        Returns:
            Path: Absolute path to the current style.
        """
        return Path(self.styles_dir) / self.current_style


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
        return Path(self.output_dir) / self.current_style

    def theme_variable_value(self, variable_id: str) -> str:
        """
        Get the value of a given theme variable.

        Args:
            variable_id (str): The theme variable identifier.

        Returns:
            str: Variable value or empty string if not found.
        """
        return self.theme_variables.get(variable_id, "")

    def set_theme_variable_value(self, variable_id: str, value: str) -> None:
        """
        Add or overwrite a theme variable's value.

        Args:
            variable_id (str): The theme variable identifier.
            value (str): The new value to assign.
        """
        self.theme_variables[variable_id] = value
        if variable_id in self.theme_color_variables:
            self.theme_color_variables[variable_id] = value

    def theme_color(self, variable_id: str) -> QColor:
        """
        Get a QColor from the theme's color mapping by variable ID.

        Args:
            variable_id (str): The color variable identifier.

        Returns:
            QColor: The corresponding color, or an invalid QColor if not found.
        """
        color_string = self.theme_color_variables.get(variable_id, "")
        if not color_string:
            return QColor()  # Invalid color
        return QColor(color_string)


    def process_stylesheet_template(self, template: str, output_file: str = "") -> str:
        """
        Process a stylesheet template by replacing all template variables,
        and optionally write the result to an output file.

        Args:
            template (str): The raw stylesheet template content.
            output_file (str): Optional filename to save the processed stylesheet.

        Returns:
            str: The processed stylesheet content.
        """
        # Perform variable replacement in the template
        template_name = "stylesheet_template"
        loader = jinja2.DictLoader({template_name : template})
        stylesheet = self.__render_stylesheet_template(template_name, loader)

        # If an output filename was provided, store the stylesheet
        if output_file:
            self.__store_stylesheet(stylesheet, output_file)
        return stylesheet


    def style_icon(self) -> QIcon:
        """
        Lazily load and return the icon for the current style.

        If no icon has been loaded yet and an icon filename is configured,
        the icon will be loaded from the style directory.

        Returns:
            QIcon: The style icon, or an empty QIcon if none is specified.
        """
        # Assume self._icon: QIcon and self.icon_file: str are initialized elsewhere
        if self.icon.isNull() and self.icon_file:
            icon_path = Path(self.current_style_path()) / self.icon_file
            self.icon = QIcon(str(icon_path))
        return self.icon


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

    @staticmethod
    def replace_colors_in_svg(svg_content: QByteArray, color_replace_list: tColorReplaceList) -> None:
        """
        Replace colors in the provided SVG content with theme colors.

        Args:
            svg_content (QByteArray): The SVG data to modify.
            color_replace_list (List[Tuple[str, str]]): List of color replacements.
        """
        for template_color, theme_color in color_replace_list:
            QtAdvancedStylesheet.__replace_color(svg_content, template_color, theme_color)

    def replace_svg_colors(
        self,
        svg_content: QByteArray,
        color_replace_list: tColorReplaceList | None = None
    ) -> None:
        """
        Replace SVG colors in the provided SVG content with theme colors.

        Args:
            svg_content (QByteArray): The SVG data to modify.
            color_replace_list (Optional[List[Tuple[str, str]]]): Optional list of color replacements.
        """
        color_replace_list = color_replace_list or self._icon_color_replace_list
        for template_color, theme_color in color_replace_list:
            self.__replace_color(svg_content, template_color, theme_color)
            

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


    def set_current_style(self, style: str) -> None:
        """
        Set the current style and trigger related updates.

        Args:
            style (str): Name of the style to activate.

        Returns:
            bool: True if the style was successfully loaded, False otherwise.
        """
        self.current_style = style
        themes_path = Path(self.path(self.Location.THEMES_LOCATION))
        xml_files = themes_path.glob("*.xml")
        self.themes: List[str] = [f.stem for f in xml_files]
        self.__parse_style_json_file()
        QDir.addSearchPath("icon", self.current_style_output_path())
        self.__add_fonts()
        self.current_style_changed.emit(self.current_style)
        self.stylesheet_changed.emit()


    def update_stylesheet(self) -> None:
        """
        Update the stylesheet by processing the style template, refreshing icons,
        and generating the final stylesheet. Emits `stylesheetChanged` signal upon success.

        Returns:
            bool: True if the stylesheet was updated successfully, False otherwise.
        """
        self.process_style_template()
        self._icon_color_replace_list.clear()
        SvgIconEngine.update_all_icons()
        self.__generate_stylesheet()
        self.stylesheet_changed.emit()


    def process_style_template(self) -> None:
        """
        Update SVG files and application palette without generating the stylesheet.

        Returns:
            bool: True if successful, False otherwise.
        """
        self.update_application_palette_colors()
        self.generate_resources()
        

    def generate_resources(self) -> None:
        """
        Generate themed resources (like recolored SVGs) based on the 'resources'
        section of the style JSON.

        Raises:
            StyleJsonError: If the JSON is missing the 'resources' key or any
                            resource definition is invalid.
            ResourceGenerationError: If generating resources for a given group fails.
        """
        resource_dir = QDir(self.path(self.Location.RESOURCE_TEMPLATES_LOCATION))
        entries: List[QFileInfo] = resource_dir.entryInfoList(["*.svg"], QDir.Filter.Files)

        jresources: Dict[str, Any] = self.json_style_param.get("resources", {})
        if not jresources:
            raise StyleJsonError("Key 'resources' missing in style JSON file")

        for group_name, params in jresources.items():
            if not isinstance(params, dict) or not params:
                raise StyleJsonError(f"Key 'resources' missing or empty for '{group_name}'")
            try:
                self.__generate_resources_for(group_name, params, entries)
            except Exception as e:
                # wrap lower-level exception if necessary
                raise ResourceGeneratorError(f"Failed to generate resources for '{group_name}': {e}") from e

    def update_application_palette_colors(self) -> None:
        """
        Update the application's palette colors using the generated theme palette.
        """
        app = QApplication.instance()
        if isinstance(app, QApplication):  # Ensure it's a QApplication
            app.setPalette(self.generate_theme_palette())
