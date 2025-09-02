from __future__ import annotations
from pathlib import Path
from typing import List, Tuple
import colorsys
from colorthief import ColorThief

RGB = Tuple[int, int, int]

def rgb_to_hex(rgb: RGB, prefix: str = "#") -> str:
    return f"{prefix}{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

def adjust_palette_for_contrast(palette: List[RGB]) -> List[RGB]:
    """Ensure palette has readable foreground/background contrast."""
    print("Adjusting palette for contrast...")
    min_contrast_luminance = 0.4
    palette.sort(key=lambda rgb: colorsys.rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)[1])
    bg_rgb, fg_rgb = palette[0], palette[-1]
    bg_h, bg_l, bg_s = colorsys.rgb_to_hls(bg_rgb[0]/255, bg_rgb[1]/255, bg_rgb[2]/255)
    fg_h, fg_l, fg_s = colorsys.rgb_to_hls(fg_rgb[0]/255, fg_rgb[1]/255, fg_rgb[2]/255)
    if (fg_l - bg_l) < min_contrast_luminance:
        print("Low contrast detected. Forcibly adjusting background and foreground.")
        bg_l = max(0.0, bg_l - 0.1)
        fg_l = min(1.0, fg_l + 0.25)
    final_bg_rgb = tuple(int(c * 255) for c in colorsys.hls_to_rgb(bg_h, max(0.0, min(1.0, bg_l)), bg_s))
    final_fg_rgb = tuple(int(c * 255) for c in colorsys.hls_to_rgb(fg_h, max(0.0, min(1.0, fg_l)), fg_s))
    return [final_bg_rgb] + palette[1:-1] + [final_fg_rgb]

def ensure_16(palette: List[RGB]) -> tuple[list[RGB], list[RGB]]:
    """Return exactly 16 terminal colors: 0-7 normal, 8-15 bright."""
    if len(palette) < 9:
        while len(palette) < 9:
            palette.extend(palette[1:min(len(palette), 4)])
        palette = palette[:10]
    normal = palette[1:9]
    out_brights = []
    for r, g, b in normal:
        h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
        l2 = min(1.0, l * 1.18 + 0.08)
        s2 = min(1.0, s * 1.06 + 0.02)
        rb, gb, bb = colorsys.hls_to_rgb(h, l2, s2)
        out_brights.append((int(rb*255), int(gb*255), int(bb*255)))
    return normal, out_brights

def extract_palette(image_path: Path, color_count: int = 10, quality: int = 5) -> list[RGB]:
    thief = ColorThief(str(image_path))
    return thief.get_palette(color_count=color_count, quality=quality)
