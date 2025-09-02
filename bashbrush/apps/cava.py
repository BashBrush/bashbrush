from __future__ import annotations
from pathlib import Path
import re
from typing import List, Tuple
from bashbrush.core.palette import ensure_16, rgb_to_hex
from bashbrush.core.config import safe_mkdir
from bashbrush.settings import Paths

def apply_theme(palette: List[Tuple[int,int,int]], wallpaper_path: Path, paths: Paths) -> None:
    print("\n--- Processing Cava ---")
    normal, _ = ensure_16(palette)

    theme_settings = {
        "gradient": "1",
        "gradient_color_1": f"'{rgb_to_hex(normal[0])}'",
        "gradient_color_2": f"'{rgb_to_hex(normal[0])}'",
        "gradient_color_3": f"'{rgb_to_hex(normal[5])}'",
        "gradient_color_4": f"'{rgb_to_hex(normal[5])}'"
    }

    safe_mkdir(paths.cava_config.parent)

    try:
        if paths.cava_config.exists():
            content = paths.cava_config.read_text(encoding="utf-8")
        else:
            content = "[general]\n"

        if not re.search(r"^\s*\[color\]", content, re.MULTILINE | re.IGNORECASE):
            content = content.strip() + "\n\n[color]\n"

        for key, value in theme_settings.items():
            pattern = re.compile(rf"^\s*{key}\s*=\s*.*", re.MULTILINE | re.IGNORECASE)
            new_line = f"{key} = {value}"

            if pattern.search(content):
                content = pattern.sub(new_line, content)
            else:
                content = re.sub(r"(^\s*\[color\].*)", f"\1\n{new_line}", content, 1, re.MULTILINE | re.IGNORECASE)

        paths.cava_config.write_text(content, encoding="utf-8")
        print(f"Updated Cava config at: {paths.cava_config}")

    except Exception as e:
        print(f"Error: Could not update Cava config file {paths.cava_config}: {e}")

    print("Cava configuration updated with new theme.")
