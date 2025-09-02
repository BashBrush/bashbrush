from __future__ import annotations
from pathlib import Path
import shutil, subprocess
from typing import List, Tuple
from bashbrush.core.palette import ensure_16, rgb_to_hex

def apply_theme(palette: List[Tuple[int,int,int]], wallpaper_path: Path, *_) -> None:
    print("\n--- Processing GNOME Terminal ---")
    normal, brights = ensure_16(palette)
    profile_id = "bashbrush"
    base_path = f"org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/{profile_id}/"

    try:
        if not shutil.which("gsettings"):
            print("Warning: gsettings not found, skipping GNOME Terminal")
            return

        try:
            result = subprocess.run(["gsettings","get","org.gnome.Terminal.ProfilesList","list"],
                                    capture_output=True, text=True, timeout=10)
            current_profiles = result.stdout.strip()
            if 'bashbrush' not in current_profiles:
                if current_profiles == "@as []":
                    new_list = "['bashbrush']"
                else:
                    import ast
                    try:
                        profiles = ast.literal_eval(current_profiles)
                        if 'bashbrush' not in profiles:
                            profiles.append('bashbrush')
                        new_list = str(profiles)
                    except:
                        new_list = "['bashbrush']"
                subprocess.run(["gsettings","set","org.gnome.Terminal.ProfilesList","list", new_list],
                               timeout=10)
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
            print(f"Warning: Could not update GNOME Terminal profile list: {e}")

        settings = [
            ("visible-name", f"'bashbrush - {wallpaper_path.stem}'"),
            ("use-theme-colors", "false"),
            ("background-color", f"'{rgb_to_hex(palette[0])}'"),
            ("foreground-color", f"'{rgb_to_hex(palette[-1])}'"),
        ]
        for key, value in settings:
            try:
                subprocess.run(["gsettings","set", base_path, key, value], timeout=10, check=True)
            except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
                print(f"Warning: Could not set {key}: {e}")

        all_colors = normal + brights
        palette_str = "[" + ", ".join(f"'{rgb_to_hex(c)}'" for c in all_colors) + "]"
        try:
            subprocess.run(["gsettings","set", base_path, "palette", palette_str], timeout=15, check=True)
            print("Created/updated GNOME Terminal profile 'bashbrush' with new theme")
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
            print(f"Warning: Could not set palette: {e}")
    except Exception as e:
        print(f"Error updating GNOME Terminal: {e}")
