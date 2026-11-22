![ukraine](doc/ukraine.jpg)

![logo](doc/ass_logo.svg)

------------------

# Qt Advanced Stylesheets for PySide6

[![PyPI version](https://img.shields.io/pypi/v/qtass-pyside6)](https://pypi.org/project/qtass-pyside6/)
[![Python Version](https://img.shields.io/pypi/pyversions/qtass-pyside6)](https://www.python.org/downloads/)

- Original Repository: https://github.com/githubuser0xFFFF/qtass-pyside6
- [Documentation](doc/user-guide.md)

This is the Python version of the [Qt Advanced Stylesheets Project](https://github.com/githubuser0xFFFF/Qt-Advanced-Stylesheets) for C++.

The library allows runtime color switching for CSS stylesheet themes including
SVG resources and SVG icons. The image below shows switching of accent color
and switching between dark and light theme. Notice how the icons in the left 
sidebar change color when switching between dark and light theme.

![color_switching](doc/CETONI_Elements_Styling.gif)

The main features are:

- runtime switching of CSS colors
- runtime color switching of CSS SVG icons / resources
- runtime color switching of icons loaded via `loadThemeAwareSvgIcon()`
- runtime switching of QPalette colors
- definition of CSS styles that switch the complete application design
- definition of XML color themes that allow switching of theme colors (dark / light)
- switching of individual theme color or switching of accent color
- QML support

If you run the `full_features` example, then you can test the functionality. 
There are some custom dark themes:

![dark](doc/qt_material_dark.gif)

And light:

![light](doc/qt_material_light.gif)

The library allows you to create stylesheets that contain variables that are
replaced at runtime like in this example:

```css
QComboBox:disabled {
  color: {{primaryColor|opacity(0.2)}};
  background-color: {{secondaryColor|opacity(0.75)}};
  border-bottom: 2px solid {{primaryColor|opacity(0.2)}};
}

QComboBox::drop-down {
  border: none;
  color: {{primaryColor}};
  width: 20px;
}
```

## Navigation

- [Navigation](#navigation)
- [Features](#features)
  - [Theme-aware Icons](#theme-aware-icons)
- [Getting started](#getting-started)
- [Run examples](#run-examples)
- [Credits](#credits)
- [Donation](#donation)
- [Showcase](#showcase)
  - [CETONI Elements](#cetoni-elements)
  - [PySoWorks](#pysoworks)

## Features

### Theme-aware Icons

The library supports loading of theme-aware SVG icons.

```python
QtAdvancedStylesheet.load_theme_aware_svg_icon(":/app/images/progress.svg");
```

This allows runtime color switching of application icons like in the
toolbar below.

![Theme Aware Icon](doc/theme_aware_icons.gif)


## Getting started

Have look into the file `CMainWindow` in the full_features example to learn
ho to use the `CStyleManager`. Here are the basic steps to add the style
manager to your application:

```python
QString AppDir = qApp->applicationDirPath();
QtAdvancedStylesheet AdvancedStylesheet;

// first set the directory that contains all your styles
AdvancedStylesheet.setStylesDirPath(AppDir + "/../../styles");

// now set the output folder where the processed styles are stored. The
// style manager will create a sub directory for each style
AdvancedStylesheet.setOutputDirPath(AppDir + "/output");

// set the current style and select a theme. After these two calls, the output
// folder will contains the generated resoruces and stylesheet.
AdvancedStylesheet.setCurrentStyle("qt_material");
AdvancedStylesheet.setCurrentTheme("dark_teal");

// now you can set the generated stylesheet
qApp->setStyleSheet(StyleManager.styleSheet());
```

## Run examples

The `full_features` example shows a window with almost all widgets to test all 
themes and create new ones.

![theme](doc/theme.gif)


## Credits

- Uwe Kindler, Project Maintainer
- [GCPDS](https://github.com/UN-GCPDS) - Grupo de control y procesamiento digital de señales

The project is strongly inspired by the great [Qt-material](https://github.com/UN-GCPDS/qt-material) project from [GCPDS](https://github.com/UN-GCPDS) and uses the qt-material stylesheet from this project.

## Donation

If this project help you reduce time to develop or if you just like it, you can give me a cup of coffee :coffee::wink:.

<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=85R64TMMSY9T6">
  <img src="doc/donate.png" alt="Donate with PayPal" width="160"/>
</a>

## Showcase

### [CETONI Elements](https://cetoni.com/cetoni-elements/)

The [CETONI Elements](https://youtu.be/xWTpCwCz8dI) software from
[CETONI](https://www.cetoni.com) is a comprehensive,
plugin-based and modular laboratory automation software for controlling CETONI devices using a joint graphical user interface. The software features a powerful script system to automate processes.

CETONI Elements Dark / Light Theme
![CETONI Elements Theme](doc/cetoni_elements_split.png)

### [PySoWorks](https://github.com/piezosystemjena/PySoWorks)

[PySoWorks](https://pypi.org/project/pysoworks/) is an application for controlling the piezo amplifiers, such as the [NV200/D](https://www.piezosystem.com/product/nv-200-d-compact-amplifier/), from [piezosystem jena](https://www.piezosystem.com/) GmbH. It demonstrates the use of the [NV200 Python library](https://pypi.org/project/nv200/) within a graphical interface based on PySide6.

PySoWorks Dark / Light Theme
![PySoWorks Theme](doc/pysoworks_split.png)

## Accent color sources (1.0.0)

The existing `accentColor` variable now supports three sources. Theme selection
(Dark/Light) and accent selection are independent.

```python
from PySide6.QtGui import QColor
from qtass import AccentSource, QtAdvancedStylesheet

style = QtAdvancedStylesheet()  # construct before applying your own palette
style.set_current_style("metro")
style.set_current_theme("dark_orange")
style.set_accent_color(QColor("#4169e1"))  # selects CUSTOM
style.set_accent_source(AccentSource.SYSTEM)
style.set_accent_source(AccentSource.THEME)  # restore current XML theme's accent
```

`THEME` is the backwards-compatible default. `CUSTOM` survives subsequent theme
switches. `SYSTEM` reads Windows' native accent and tracks its changes without
reading back QtASS' own application palette. Unavailable system colors fall back
to the current theme; on other platforms the initial native Qt accent palette is
used as a snapshot. Construct the style before replacing the application's palette.

`accent_color()` returns the effective QColor. `accent_color_changed(QColor)` and
`accent_source_changed(AccentSource)` expose changes. Invalid custom colors are
rejected before changing the policy. Selecting CUSTOM without a saved custom color
raises ValueError. `set_theme_variable_value("accentColor", value)` also selects
persistent CUSTOM mode; call `update_stylesheet()` afterwards as before.

New accent setters and native change notifications refresh CSS, palette and SVG
resources and apply the generated stylesheet to QApplication. Existing explicit
`update_stylesheet()` callers continue applying `style.stylesheet` themselves.
Keep Qt calls on the GUI thread. Native Windows event callbacks are queued there
automatically. Native subscriptions are released on style destruction/application exit.

Applications own preference storage: persist the chosen source and custom color
in per-user settings, not in shared theme XML files. QtASS does not change system
personalization settings or automatically persist application preferences.

For tests or alternative platforms, subclass `qtass.system_accent.AccentProvider`,
implement `color() -> QColor`, and emit its `changed(QColor)` signal on the GUI
thread. Pass the instance as `QtAdvancedStylesheet(accent_provider=provider)`.
The caller owns an injected provider; the default native provider is style-owned.

Run regression checks with:
```shell
python -m unittest discover -s tests -v
```
