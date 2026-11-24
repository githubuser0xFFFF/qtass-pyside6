# Changelog

## 1.0.2 - 2026-11-24

### Fixed
- Use Python 3.14 in both GitHub publication jobs to satisfy the >=3.13 minimum.
- Default manual publication to the v1.0.2 release tag.

## 1.0.1 - 2026-11-24

### Changed
- Require Python >=3.13 without an upper bound in package metadata.
- Scope Poetry dependency locking to >=3.13,<3.16, matching current PySide6 support.
- Allow installation on Python 3.14; runtime behavior is unchanged.

## 1.0.0 - 2026-11-22

### Added
- AccentSource.THEME, CUSTOM and SYSTEM policies for the existing accentColor variable.
- set_accent_color(), set_accent_source(), accent_color(), accent_source and change signals.
- Native Windows accent lookup with UISettings.GetColorValue(ACCENT) and live
  ColorValuesChanged notifications marshalled onto the Qt GUI thread.
- Injectable accent providers and initial Qt-palette fallback on other platforms.
- Regression coverage for CSS, palette, generated SVG resources, theme switching,
  invalid colors, missing system colors and native Windows subscription cleanup.

### Changed
- Explicit accentColor variable assignments now select persistent CUSTOM mode,
  retaining the color across Dark/Light theme changes.
- New accent setters and system notifications refresh and apply the generated
  stylesheet. Existing update_stylesheet() calls retain their explicit-application
  contract. Applications remain responsible for persisting user preferences.
- Windows installations include the required Python/WinRT UI and Foundation modules.

### Fixed
- Theme loading returns success correctly and updates the current theme name and signal.
- QPalette.Accent is recognized in palette JSON and populated by the Metro style.
- Font registration uses the supplied directory correctly when widgets already exist.
- Build isolation declares the dynamic-versioning backend dependency.
- Package project URLs refer to qtass-pyside6.

### Compatibility
- THEME remains the default; existing XML/CSS themes require no new accent field.
- Non-Windows SYSTEM mode uses the native Qt palette captured before styling;
  live system-color observation is currently Windows-specific.
- Existing user settings and theme files are not modified automatically.
