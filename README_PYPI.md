# qtass-pyside6

**Qt Advanced Stylesheets for PySide 6**

[![PyPI version](https://img.shields.io/pypi/v/qtass-pyside6)](https://pypi.org/project/qtass-pyside6/)
[![Python Version](https://img.shields.io/pypi/pyversions/qtass-pyside6)](https://www.python.org/downloads/)

This is the Python version of the [Qt Advanced Stylesheets Project](https://github.com/githubuser0xFFFF/Qt-Advanced-Stylesheets) for C++.

The library allows runtime color switching for CSS stylesheet themes including
SVG resources and SVG icons. The image below shows switching of accent color
and switching between dark and light theme. Notice how the icons in the left 
sidebar change color when switching between dark and light theme.

![color_switching](https://raw.githubusercontent.com/githubuser0xFFFF/qtass-pyside6/refs/heads/main/doc/CETONI_Elements_Styling.gif)

The main features are:

- runtime switching of CSS colors
- runtime color switching of CSS SVG icons / resources
- runtime color switching of icons loaded via `loadThemeAwareSvgIcon()`
- runtime switching of QPalette colors
- definition of CSS styles that switch the complete application design
- definition of XML color themes that allow switching of theme colors (dark / light)
- switching of individual theme color or switching of accent color
- QML support

---

## 📦 Installation

Install from **PyPI**:

```shell
pip install qtass-pyside6
```