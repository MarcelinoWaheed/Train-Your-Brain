# storage.py
import os
from typing import Optional

_HS_FILE = "highscore.txt"

def load_highscore() -> int:
    if os.path.exists(_HS_FILE):
        with open(_HS_FILE, "r", encoding="utf-8") as f:
            content: Optional[str] = f.read().strip() or "0"
            try:
                return int(content)
            except ValueError:
                return 0
    return 0

def save_highscore(score: int) -> None:
    with open(_HS_FILE, "w", encoding="utf-8") as f:
        f.write(str(score))