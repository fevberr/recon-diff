from __future__ import annotations
from pathlib import Path
import yaml
from pydantic import BaseModel


class Config(BaseModel):
    store: Path = Path("./snapshots")
    concurrency: int = 48
    timeout: float = 6.0
    user_agent: str = "rd/0.1"


def load(path: Path) -> Config:
    if not path.exists():
        return Config()
    d = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return Config(**d)