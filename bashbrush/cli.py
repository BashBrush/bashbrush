from __future__ import annotations
import os, random, importlib
from pathlib import Path
from typing import Sequence

from bashbrush.settings import default_paths
from bashbrush.core.palette import extract_palette, adjust_palette_for_contrast
from bashbrush.core.wallpaper import set_wallpaper, in_gnome
from bashbrush.apps import DEFAULT_APPS

# current_version = "bashbrush"

def load_selected_apps() -> Sequence[str]:
    env = os.getenv("BASHBRUSH_APPS")
    if env:
        mods = [m.strip() for m in env.split(",") if m.strip()]
        return [m if m.startswith("bashbrush.apps.") else f"bashbrush.apps.{m}" for m in mods]
    return DEFAULT_APPS

def main() -> None:
    paths = default_paths()
    if not paths.wallpaper_dir.exists():
        raise SystemExit(f"No wallpaper directory found at {paths.wallpaper_dir}")

    wallpaper_files = [p for p in paths.wallpaper_dir.iterdir() if p.suffix.lower() in (".jpg",".jpeg",".png",".webp",".gif")]
    if not wallpaper_files:
        raise SystemExit(f"No valid wallpaper files found in {paths.wallpaper_dir}")

    chosen = random.choice(wallpaper_files).resolve()
    print(f"Processing wallpaper: {chosen.name}")

    palette = extract_palette(chosen, color_count=10, quality=5)
    final_palette = adjust_palette_for_contrast(palette)
    set_wallpaper(chosen)

    # Dynamically import and apply enabled app modules
    app_modules = load_selected_apps()
    for mod_name in app_modules:
        try:
            mod = importlib.import_module(mod_name)
        except Exception as e:
            print(f"Skip {mod_name}: import failed ({e})")
            continue

        # Decide if the app should run based on simple heuristics/paths
        try:
            if mod_name.endswith(".gnome_terminal"):
                if not in_gnome():
                    print("Skip GNOME Terminal: not in GNOME session.")
                    continue
                mod.apply_theme(final_palette, chosen, paths)
                continue
        except Exception:
            # in_gnome check failed; skip silently
            pass

        # For file-based apps, only run if their config directory exists
        try:
            if hasattr(paths, "alacritty_config") and mod_name.endswith(".alacritty"):
                if not paths.alacritty_config.parent.exists():
                    print("Skip Alacritty: config directory not found.")
                    continue
            if hasattr(paths, "cava_config") and mod_name.endswith(".cava"):
                if not paths.cava_config.parent.exists():
                    print("Skip Cava: config directory not found.")
                    continue        
            if hasattr(paths, "kitty_config") and mod_name.endswith(".kitty"):
                if not paths.kitty_config.parent.exists():
                    print("Skip Kitty: config directory not found.")
                    continue
            if hasattr(paths, "foot_config") and mod_name.endswith(".foot"):
                if not paths.foot_config.parent.exists():
                    print("Skip foot: config directory not found.")
                    continue
            if hasattr(paths, "ptyxis_config") and mod_name.endswith(".ptyxis"):
                if not paths.ptyxis_config.parent.exists():
                    print("Skip Ptyxis: config directory not found.")
                    continue
            if hasattr(paths, "ghostty_config") and mod_name.endswith(".ghostty"):
                if not paths.ghostty_config.parent.exists():
                    print("Skip Ghostty: config directory not found.")
                    continue
        except Exception:
            pass

        try:
            mod.apply_theme(final_palette, chosen, paths)
        except Exception as e:
            print(f"Error processing {mod_name}: {e}")

    print("\nSuccessfully set wallpaper and themes.")
    print("Restart your terminal(s) to see the changes.")

if __name__ == "__main__":
    main()
