from __future__ import annotations
import asyncio
import httpx
from ..models import Finding
from .base import Scanner


class Robots(Scanner):
    name = "robots"

    async def scan(self, target: str) -> list[Finding]:
        hs = await self.hosts(target)
        sem = asyncio.Semaphore(self.cfg.concurrency)
        headers = {"User-Agent": self.cfg.user_agent}

        async def probe(host: str):
            async with sem:
                async with httpx.AsyncClient(timeout=self.cfg.timeout,
                                             verify=False, headers=headers,
                                             follow_redirects=True) as c:
                    for path in ("/robots.txt", "/sitemap.xml"):
                        try:
                            r = await c.get(f"https://{host}{path}")
                        except Exception:
                            continue
                        if r.status_code != 200 or not r.text.strip():
                            continue
                        if path == "/robots.txt":
                            disallow = [ln.split(":", 1)[1].strip()
                                        for ln in r.text.splitlines()
                                        if ln.lower().startswith("disallow:")]
                            return Finding(kind="robots", key=f"{host}:robots",
                                           value={"host": host, "disallow": disallow[:50]})
                        return Finding(kind="robots", key=f"{host}:sitemap",
                                       value={"host": host, "present": True})
                return None

        rs = await asyncio.gather(*[probe(h) for h in hs])
        return [x for x in rs if x]