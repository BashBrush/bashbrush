from __future__ import annotations
from pathlib import Path
from typing import List, Tuple
from bashbrush.core.palette import ensure_16, rgb_to_hex
from bashbrush.core.config import update_config
from bashbrush.settings import Paths
import re

def apply_theme(palette: List[Tuple[int,int,int]], wallpaper_path: Path, paths: Paths) -> None:
    print("\n--- Processing ncspot ---")
    normal, brights = ensure_16(palette)
    full_palette = normal + brights
    
    theme_lines = [
        '# toggle comment on background (commented == off) to activate terminal opacity\n\n'
        f'# background = "{rgb_to_hex(full_palette[-1])}"',
        f'primary = "{rgb_to_hex(full_palette[0])}"',
        f'secondary = "{rgb_to_hex(full_palette[1])}"',
        f'title = "{rgb_to_hex(full_palette[2])}"',
        f'playing = "{rgb_to_hex(full_palette[3])}"',
        f'playing_selected = "{rgb_to_hex(full_palette[4])}"',
        f'playing_bg = "{rgb_to_hex(full_palette[5])}"',
        f'highlight = "{rgb_to_hex(full_palette[0])}"',
        f'highlight_bg = "{rgb_to_hex(full_palette[7])}"',
        f'error = "{rgb_to_hex(full_palette[0])}"',
        f'error_bg = "{rgb_to_hex(full_palette[8])}"',
        f'statusbar = "{rgb_to_hex(full_palette[9])}"',
        f'statusbar_progress = "{rgb_to_hex(full_palette[10])}"',
        f'statusbar_bg = "{rgb_to_hex(full_palette[11])}"',
        f'cmdline = "{rgb_to_hex(full_palette[0])}"',
        f'cmdline_bg = "{rgb_to_hex(full_palette[-1])}"',
        f'search_match = "{rgb_to_hex(full_palette[12])}"',
    ]
    
    theme_block = "[theme]\n" + "\n".join(theme_lines)

    update_config(
        paths.ncspot_config,
        theme_block,
        r"^\[theme\].*?(?=^\[|\Z)",
        multiline=True
    )
    
    print(f"Updated ncspot config with new theme")