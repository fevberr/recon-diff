from __future__ import annotations
import asyncio
import httpx
from ..models import Finding
from .base import Scanner

REQUIRED = ["content-security-policy", "strict-transport-security",
            "x-frame-options", "x-content-type-options",
            "referrer-policy", "permissions-policy"]


class Headers(Scanner):
    name = "headers"

    async def scan(self, target: str) -> list[Finding]:
        hs = await self.hosts(target)
        sem = asyncio.Semaphore(self.cfg.concurrency)
        headers = {"User-Agent": self.cfg.user_agent}

        async def probe(host: str):
            async with sem:
                try:
                    async with httpx.AsyncClient(timeout=self.cfg.timeout,
                                                 verify=False, headers=headers,
                                                 follow_redirects=True) as c:
                        r = await c.get(f"https://{host}/")
                except Exception:
                    return None
                present = {k.lower() for k in r.headers.keys()}
                missing = [x for x in REQUIRED if x not in present]
                return Finding(kind="headers", key=host,
                               value={"host": host, "missing": missing})

        rs = await asyncio.gather(*[probe(h) for h in hs])
        return [x for x in rs if x]