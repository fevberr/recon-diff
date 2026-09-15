from __future__ import annotations
import asyncio
import hashlib
import re
import httpx
from ..models import Finding
from .base import Scanner

SCRIPT = re.compile(r'<script[^>]+src=["\']([^"\']+\.js[^"\']*)["\']', re.IGNORECASE)
HINTS = re.compile(r"(api[_-]?key|secret|token|password|aws_|firebase)", re.IGNORECASE)


class Js(Scanner):
    name = "js"

    async def scan(self, target: str) -> list[Finding]:
        hs = await self.hosts(target)
        sem = asyncio.Semaphore(self.cfg.concurrency)
        headers = {"User-Agent": self.cfg.user_agent}
        urls: set[str] = set()

        async def page(host: str):
            async with sem:
                try:
                    async with httpx.AsyncClient(timeout=self.cfg.timeout,
                                                 follow_redirects=True,
                                                 verify=False, headers=headers) as c:
                        r = await c.get(f"https://{host}/")
                        for m in SCRIPT.findall(r.text):
                            urls.add(_abs(target, m))
                except Exception:
                    pass

        await asyncio.gather(*[page(h) for h in hs])

        async def grab(url: str):
            async with sem:
                try:
                    async with httpx.AsyncClient(timeout=8.0,
                                                 follow_redirects=True,
                                                 verify=False, headers=headers) as c:
                        r = await c.get(url)
                except Exception:
                    return None
                body = r.content
                text = body[:400_000].decode("utf-8", errors="ignore")
                hits = sorted({m.group(0).lower() for m in HINTS.finditer(text)})
                return Finding(kind="js", key=url, value={
                    "hash": hashlib.sha256(body).hexdigest()[:16],
                    "hints": hits[:8],
                    "size": len(body),
                })

        rs = await asyncio.gather(*[grab(u) for u in urls])
        return [x for x in rs if x]


def _abs(base: str, src: str) -> str:
    if src.startswith("http"):
        return src
    if src.startswith("//"):
        return f"https:{src}"
    return f"https://{base}{src if src.startswith('/') else '/' + src}"