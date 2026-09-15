from __future__ import annotations
import asyncio
import re
import httpx
from ..models import Finding
from .base import Scanner

SIGS = [
    ("nginx", r"nginx", "header"),
    ("apache", r"apache", "header"),
    ("cloudflare", r"cloudflare", "header"),
    ("wordpress", r"wp-content", "body"),
    ("grafana", r"grafana", "body"),
    ("kibana", r"kibana", "body"),
    ("jenkins", r"jenkins", "body"),
    ("gitlab", r"gitlab", "body"),
    ("phpmyadmin", r"phpmyadmin", "body"),
]


class Tech(Scanner):
    name = "tech"

    async def scan(self, target: str) -> list[Finding]:
        hs = await self.hosts(target)
        sem = asyncio.Semaphore(self.cfg.concurrency)
        headers = {"User-Agent": self.cfg.user_agent}

        async def probe(host: str):
            async with sem:
                try:
                    async with httpx.AsyncClient(timeout=self.cfg.timeout,
                                                 follow_redirects=True,
                                                 verify=False, headers=headers) as c:
                        r = await c.get(f"https://{host}/")
                except Exception:
                    return []
                hb = "\n".join(f"{k}: {v}" for k, v in r.headers.items()).lower()
                bb = r.text[:200_000].lower()
                out = []
                for name, pat, where in SIGS:
                    blob = hb if where == "header" else bb
                    if re.search(pat, blob):
                        out.append(Finding(kind="tech", key=f"{host}:{name}",
                                           value={"name": name, "host": host}))
                return out

        rs = await asyncio.gather(*[probe(h) for h in hs])
        out: list[Finding] = []
        for x in rs:
            out.extend(x)
        return out