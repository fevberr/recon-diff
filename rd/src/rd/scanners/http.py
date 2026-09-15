from __future__ import annotations
import asyncio
import hashlib
import re
import httpx
from ..models import Finding
from .base import Scanner

WANT = ["server", "x-powered-by", "cf-ray", "via"]


class Http(Scanner):
    name = "http"

    async def scan(self, target: str) -> list[Finding]:
        hs = await self.hosts(target)
        sem = asyncio.Semaphore(self.cfg.concurrency)
        headers = {"User-Agent": self.cfg.user_agent}

        async def probe(host: str):
            async with sem:
                async with httpx.AsyncClient(timeout=self.cfg.timeout,
                                             follow_redirects=False,
                                             verify=False, headers=headers) as c:
                    r = None
                    for scheme in ("https", "http"):
                        try:
                            r = await c.get(f"{scheme}://{host}/")
                            break
                        except Exception:
                            continue
                    if r is None:
                        return None
                    hdrs = {k.lower(): v for k, v in r.headers.items()}
                    keep = {k: hdrs[k] for k in WANT if k in hdrs}
                    return Finding(kind="http", key=host, value={
                        "status": r.status_code,
                        "headers": keep,
                        "title": _title(r.text)[:120],
                        "body_hash": hashlib.sha256(r.content).hexdigest()[:16],
                        "server": hdrs.get("server", ""),
                    })

        rs = await asyncio.gather(*[probe(h) for h in hs])
        return [x for x in rs if x]


def _title(html: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else ""