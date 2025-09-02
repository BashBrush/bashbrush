from __future__ import annotations
import os, shutil, subprocess
from pathlib import Path

def is_hyprland_active() -> bool:
    sig = os.getenv("HYPRLAND_INSTANCE_SIGNATURE")
    if not sig:
        return False
    sock = Path(os.getenv("XDG_RUNTIME_DIR", "")) / "hypr" / sig / ".socket.sock"
    return sock.exists() and shutil.which("hyprctl") is not None

def in_gnome() -> bool:
    desk = (os.getenv("XDG_CURRENT_DESKTOP") or "").lower()
    sess = (os.getenv("DESKTOP_SESSION") or "").lower()
    return "gnome" in desk or "gnome" in sess

def set_wallpaper(wallpaper_path: Path) -> None:
    wp = str(wallpaper_path.resolve())
    if in_gnome():
        uri = f"file://{wp}"
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", uri])
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", uri])
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-options", "zoom"])
        print("GNOME: wallpaper set via gsettings.")
        return
    if is_hyprland_active():
        cmd = (f"swww img '{wp}'")
        os.system(cmd)
        print("Hyprland: wallpaper set via swww.")
        return
    try:
        uri = f"file://{wp}"
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", uri])
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", uri])
        print("Fallback: gsettings worked.")
    except Exception:
        print("No supported compositor detected; consider adding feh/swww fallback.")
