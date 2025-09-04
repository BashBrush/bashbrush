from __future__ import annotations
import re, shutil
from pathlib import Path

def safe_mkdir(p: Path) -> None:
    p = p if p.is_dir() else p.parent
    p.mkdir(parents=True, exist_ok=True)

def update_config(config_path: Path, new_content: str, regex_pattern: str, multiline: bool = False) -> None:
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
    
    if multiline:
        # Handle multi-line section replacement
        try:
            new_text = re.sub(regex_pattern, new_content, text, flags=re.MULTILINE | re.DOTALL)
            if new_text == text:  # No replacement made, section doesn't exist
                new_text = text + "\n\n" + new_content
        except re.error as e:
            print(f"Warning: Regex error in config update: {e}")
            new_text = text + "\n\n" + new_content
        
        config_path.write_text(new_text, encoding="utf-8")
    else:
        # Original
        lines = text.splitlines(keepends=True)
        found = False
        for i, line in enumerate(lines):
            try:
                if re.search(regex_pattern, line):
                    lines[i] = new_content
                    found = True
                    break
            except re.error as e:
                print(f"Warning: Regex error in config update: {e}")
        if not found:
            lines.insert(0, new_content)
        config_path.write_text("".join(lines), encoding="utf-8")
    
    print(f"Updated {config_path.name} to use new theme.")