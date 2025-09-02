bashbrush (BashBrush / Himari Edition) – Modular & Absolute-Import Refactor

Structure:
  bashbrush/
    __init__.py
    settings.py
    core/
      palette.py
      wallpaper.py
      config.py
    apps/
      __init__.py
      alacritty.py
      cava.py
      kitty.py
      foot.py
      gnome_terminal.py
      ghostty.py
      wezterm.py
    cli.py

Usage:
  # Option A: run as a script
  python -m bashbrush.cli

  # Option B: run the module directly (once installed into PYTHONPATH)
  python -c "from bashbrush.cli import main; main()"

  # Toggle apps via environment:
  export BASHBRUSH_APPS="alacritty,kitty,ghostty"

Notes:
  • All imports are absolute (e.g., `from bashbrush.core.palette import …`).
  • Themes and config references use absolute filesystem paths.
  • End users can comment out modules in `bashbrush/apps/__init__.py` (DEFAULT_APPS),
    or set BASHBRUSH_APPS to a comma-separated list.
  • Default wallpaper directory resolves to `<package>/wallpapers`. Override with
    BASHBRUSH_WALLPAPERS=/absolute/path/to/wallpapers
