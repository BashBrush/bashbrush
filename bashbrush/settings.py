from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import os

@dataclass(frozen=True)
class Paths:
    home: Path
    base_dir: Path
    wallpaper_dir: Path
    # app configs (alphabetical order :))
    alacritty_config: Path
    alacritty_themes: Path
    cava_config: Path
    foot_config: Path
    foot_themes: Path
    ghostty_config: Path
    ghostty_themes: Path
    kitty_config: Path
    kitty_themes: Path
    wezterm_config: Path
    wezterm_colors: Path

def default_paths() -> Paths:
    home = Path.home()
    # Resolve to absolute paths
    base_dir = Path(__file__).resolve().parent
    # Assume wallpapers live next to this package by default (can be overridden via ENV)
    wallpaper_dir = Path(os.getenv("BASHBRUSH_WALLPAPERS", base_dir / "wallpapers")).expanduser().resolve()

    return Paths(
        home=home,
        base_dir=base_dir,
        wallpaper_dir=Path(wallpaper_dir).resolve(),
        alacritty_config=(home / ".config" / "alacritty" / "alacritty.toml").resolve(),
        cava_config=(home / ".config" / "cava" / "config").resolve(),
        foot_config=(home / ".config" / "foot" / "foot.ini").resolve(),
        foot_themes=(home / ".config" / "foot" / "themes").resolve(),
        ghostty_config=(home / ".config" / "ghostty" / "config").resolve(),
        ghostty_themes=(home / ".config" / "ghostty" / "themes").resolve(),
        alacritty_themes=(home / ".config" / "alacritty" / "themes").resolve(),
        kitty_config=(home / ".config" / "kitty" / "kitty.conf").resolve(),
        kitty_themes=(home / ".config" / "kitty" / "themes").resolve(),
        wezterm_config=(home / ".config" / "wezterm" / "wezterm.lua").resolve(),
        wezterm_colors=(home / ".config" / "wezterm" / "colors").resolve(),
    )