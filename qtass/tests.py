import logging
import json
from rich.traceback import install as install_rich_traceback
from rich.logging import RichHandler
import qtass
import sys
from PySide6.QtCore import QCoreApplication, QObject
from PySide6.QtWidgets import QApplication



def setup_logging():
    """
    Configures the logging settings for the application.
    """
    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     format='%(asctime)s.%(msecs)03d | %(levelname)-6s | %(name)-25s | %(message)s',
    #     datefmt='%H:%M:%S'
    # )

    # rich logging and exception handling
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d | %(name)-25s | %(message)s',
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True, )]
    )
    install_rich_traceback(show_locals=True)

    # List all loggers
    #for name in logging.root.manager.loggerDict:
    #    print(name)

    #logging.getLogger("nv200.device_discovery").setLevel(logging.DEBUG)
    #logging.getLogger("nv200.telnet_protocol").setLevel(logging.DEBUG)


def test_json_parsing():
    # Load JSON data from the file
    with open("styles/metro/metro.json", "r") as file:
        data = json.load(file)

    # Access the value of "base_color" in the "palette"
    base_color_key = data["palette"]["base_color"]
    print("Base color key name:", base_color_key)

    # Get the HEX value for that key from the "resources" > "normal" section
    resources_normal = data["resources"]["normal"]

    # Reverse the dictionary to map values to keys
    value_to_color = {v: k for k, v in resources_normal.items()}

    # Get the HEX value corresponding to the base color
    base_color_hex = value_to_color.get(base_color_key)
    print("Base color hex:", base_color_hex)



class MyApp(QObject):
    def __init__(self):
        super().__init__()
        self.style = qtass.QtAdvancedStylesheet()
        self.style.current_theme_changed.connect(self.on_theme_changed)
        self.style.set_styles_dir_path("styles")
        print("Available styles:", self.style.styles())
        self.style.set_current_style("metro")
        self.style.set_default_theme()

    def on_theme_changed(self, theme):
        print("Theme changed:", theme)


def test_qtass():
    style = qtass.QtAdvancedStylesheet()
    style.set_styles_dir_path("styles")
    print("Available styles:", style.styles)
    style.output_dir = "style_output2"
    style.set_current_style("material")
    style.set_default_theme()
    style.update_stylesheet()


def main():
    setup_logging()
    app = QApplication(sys.argv)
    test_qtass()
    #my_app = MyApp()
    #return app.exec()


if __name__ == "__main__":
    sys.exit(main())