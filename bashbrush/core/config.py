from __future__ import annotations
import re, shutil
from pathlib import Path

def safe_mkdir(p: Path) -> None:
    p = p if p.is_dir() else p.parent
    p.mkdir(parents=True, exist_ok=True)

def update_config(config_path: Path, new_line: str, regex_pattern: str) -> None:
    """Generic function to back up and update a config file using absolute paths."""
    safe_mkdir(config_path)
    if config_path.exists():
        backup_path = config_path.with_suffix(config_path.suffix + ".bak")
        try:
            shutil.copy(str(config_path), str(backup_path))
            print(f"Backed up existing config to: {backup_path}")
        except Exception as e:
            print(f"Warning: Could not backup config: {e}")

    try:
        text = config_path.read_text(encoding="utf-8")
    except Exception:
        text = ""

    lines = text.splitlines(keepends=True)
    found = False
    for i, line in enumerate(lines):
        try:
            if re.search(regex_pattern, line):
                lines[i] = new_line
                found = True
                break
        except re.error as e:
            print(f"Warning: Regex error in config update: {e}")

    if not found:
        lines.insert(0, new_line)

    try:
        config_path.write_text("".join(lines), encoding="utf-8")
        print(f"Updated {config_path.name} to use new theme.")
    except Exception as e:
        print(f"Error: Could not write config file {config_path}: {e}")
