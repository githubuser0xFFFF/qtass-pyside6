import logging
from rich.traceback import install as install_rich_traceback
from rich.logging import RichHandler
import qtass
import sys
from PySide6.QtWidgets import QApplication



def setup_logging():
    """
    Configures the logging settings for the application.
    """
    # rich logging and exception handling
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d | %(name)-25s | %(message)s',
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True, )]
    )
    install_rich_traceback(show_locals=True)


def test_qtass():
    """
    Test function for the QtAdvancedStylesheet class.
    """
    style = qtass.QtAdvancedStylesheet()
    style.set_styles_dir_path("styles")
    print("Available styles:", style.styles)
    style.output_dir = "build/style_output2"
    style.set_current_style("material")
    style.set_default_theme()
    style.update_stylesheet()


def main():
    setup_logging()
    app = QApplication(sys.argv)
    test_qtass()


if __name__ == "__main__":
    sys.exit(main())