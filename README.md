# 🎨 BashBrush

*Because your terminal should match your vibe*

BashBrush is a Python tool that automatically generates beautiful terminal themes from your wallpapers. Pick a wallpaper, run the script, and watch your entire terminal ecosystem transform to match!

## ✨ What it does

1. **Picks a random wallpaper** from your wallpaper directory
2. **Extracts a color palette** using smart color theory algorithms
3. **Sets your wallpaper** (GNOME and Hyprland supported)
4. **Themes your terminal apps** with cohesive color schemes

## 🎯 Supported Apps

BashBrush plays nice with your favorite terminal emulators and TUIs:
- **Alacritty** - Generates beautiful TOML themes
- **Kitty** - Because cats deserve pretty colors too
- **Foot** - Lightweight and fast
- **Ghostty** - The new kid on the block
- **Cava** - Audio visualizer eye candy
- **WezTerm** - For the power users
- **ncspot** - Cause you've got good taste in music

## 🚀 How it works

The magic happens in a few simple steps:

1. **Color Extraction** - Uses ColorThief (based on k-means clustering) to extract dominant colors from your wallpaper
2. **Smart Contrast Adjustment** - Automatically adjusts background/foreground colors to ensure optimal readability using HLS color space transformations
3. **16-Color Terminal Palette Generation** - Creates proper ANSI color schemes with normal (0-7) and bright (8-15) color pairs using color space manipulation
4. **Dynamic App Theming** - Dynamically imports and applies themes only to apps you have installed, detected through config directory existence
5. **Safe Config Management** - Automatically backs up existing configs before making changes and uses regex patterns for precise config updates

## 🎲 Usage

```bash
# Use default apps
python -m bashbrush.cli

# Or customize which apps to theme
export BASHBRUSH_APPS="alacritty,kitty,cava"
python -m bashbrush

# Custom wallpaper directory
export BASHBRUSH_WALLPAPERS="~/Pictures/Wallpapers"
python -m bashbrush.cli
```

## 🏗️ Technical Architecture

BashBrush follows a modular architecture with clearly separated concerns:

- **Core Modules** (`bashbrush.core`): 
  - `palette.py` - Handles color extraction, contrast adjustment, and palette generation
  - `wallpaper.py` - Manages wallpaper setting across different desktop environments
  - `config.py` - Provides safe config file management with backup functionality

- **App Modules** (`bashbrush.apps`): Each app has its own module that implements an `apply_theme()` function
  - Uses standardized function signatures for consistency
  - Implements app-specific config formats (TOML, INI, etc.)
  - Handles theme file generation and config file updates

- **Settings Management** (`bashbrush.settings`): Centralized path configuration with environment variable overrides
- **Dynamic Module Loading**: Apps are loaded dynamically based on environment variables or defaults

## 🎨 Color Theory Implementation

BashBrush uses sophisticated color theory to create readable, aesthetically pleasing themes:

1. **Dominant Color Extraction**: Uses ColorThief's k-means clustering algorithm to extract the most representative colors
2. **Contrast Optimization**: Employs HLS (Hue, Lightness, Saturation) color space to ensure minimum luminance contrast between background and foreground
3. **Palette Generation**: Automatically generates 16-color ANSI palettes with perceptually uniform bright variants
4. **Color Space Manipulation**: Uses HLS transformations to create bright color variants that maintain hue while increasing lightness and saturation

## 🔧 Smart Features

- **Automatic App Detection** - Skips apps you don't have installed by checking for config directories
- **Environment Awareness** - Detects desktop environments (GNOME, Hyprland) and uses appropriate wallpaper setting methods
- **Safe Config Updates** - Always backs up your existing configs and uses regex-based line replacement for precision
- **Contrast Optimization** - Makes sure text is readable against backgrounds using perceptual lightness calculations
- **Random Selection** - Keeps things fresh with surprise wallpapers
- **Modular Design** - Easy to extend with new apps through the standardized module interface

## 📦 Dependencies

- `colorthief` - For intelligent color palette extraction from images
- `pillow` - For image processing support in colorthief

Perfect for rice enthusiasts, theme collectors, and anyone who thinks their terminal should be as pretty as their wallpaper! 🌈
