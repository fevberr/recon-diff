from __future__ import annotations
import asyncio
import re
import httpx
from ..models import Finding
from .base import Scanner

SIGS = [
    ("cloudflare", [r"cf-ray", r"server: cloudflare"]),
    ("akamai", [r"akamai", r"server: akamaighost"]),
    ("fastly", [r"x-served-by", r"x-fastly"]),
    ("cloudfront", [r"x-amz-cf-id"]),
]


class Waf(Scanner):
    name = "waf"

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
                blob = "\n".join(f"{k}: {v}" for k, v in r.headers.items()).lower()
                for name, pats in SIGS:
                    for pat in pats:
                        if re.search(pat, blob):
                            return Finding(kind="waf", key=host,
                                           value={"name": name, "host": host})
                return None

        rs = await asyncio.gather(*[probe(h) for h in hs])
        return [x for x in rs if x]