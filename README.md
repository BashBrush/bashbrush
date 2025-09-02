# 🎨 BashBrush

*Because your terminal should match your vibe*

BashBrush is a Python tool that automatically generates beautiful terminal themes from your wallpapers. Pick a wallpaper, run the script, and watch your entire terminal ecosystem transform to match!

## ✨ What it does

1. **Picks a random wallpaper** from your wallpaper directory
2. **Extracts a color palette** using some smart color theory magic
3. **Sets your wallpaper** (GNOME and Hyprland supported)
4. **Themes ALL your terminal apps** automagically

## 🎯 Supported Apps

BashBrush plays nice with your favorite terminal emulators:
- **Alacritty** - Generates beautiful TOML themes
- **Kitty** - Because cats deserve pretty colors too
- **Foot** - Lightweight and fast
- **Ghostty** - The new kid on the block
- **Cava** - Audio visualizer eye candy
- **WezTerm** - For the power users

## 🚀 How it works

The magic happens in a few simple steps:

1. **Color Extraction** (`palette.py`) - Uses ColorThief to pull dominant colors from your wallpaper
2. **Smart Contrast** - Automatically adjusts colors so your text is actually readable
3. **16-Color Terminal Palette** - Generates proper normal + bright color pairs
4. **App Detection** - Only themes the apps you actually have installed
5. **Config Management** - Safely backs up your existing configs before making changes

## 🎲 Usage

```bash
# Use default apps
python -m bashbrush

# Or customize which apps to theme
export BASHBRUSH_APPS="alacritty,kitty,cava"
python -m bashbrush

# Custom wallpaper directory
export BASHBRUSH_WALLPAPERS="~/Pictures/Wallpapers"
python -m bashbrush
```

## 🎨 The Philosophy

Why settle for boring, static terminal themes when your wallpaper changes? BashBrush believes your entire desktop should be a cohesive, beautiful experience. Every time you run it, you get a fresh new look that actually matches your background.

No more manually tweaking config files or hunting for themes that *almost* match your wallpaper. Just run it and enjoy the eye candy!

## 🔧 Smart Features

- **Automatic App Detection** - Skips apps you don't have installed
- **Environment Awareness** - Knows if you're in GNOME, Hyprland, etc.
- **Safe Config Updates** - Always backs up your existing configs
- **Contrast Optimization** - Makes sure text is readable against backgrounds
- **Random Selection** - Keeps things fresh with surprise wallpapers

Perfect for rice enthusiasts, theme collectors, and anyone who thinks their terminal should be as pretty as their wallpaper! 🌈
