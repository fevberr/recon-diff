from __future__ import annotations
from abc import ABC, abstractmethod
from ..config import Config
from ..models import Finding


class Scanner(ABC):
    name: str = "base"

    def __init__(self, cfg: Config | None = None):
        self.cfg = cfg or Config()

    @abstractmethod
    async def scan(self, target: str) -> list[Finding]:
        ...

    async def hosts(self, target: str) -> list[str]:
        from ..store import latest
        from pathlib import Path
        hs = {target, f"www.{target}"}
        try:
            s = latest(Path(self.cfg.store), target)
            if s:
                for f in s.kind("subdomain"):
                    hs.add(f.key)
        except Exception:
            pass
        return sorted(hs)