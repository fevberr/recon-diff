from __future__ import annotations
import asyncio
from ..models import Finding
from .base import Scanner

PORTS = [21,22,23,25,53,80,110,143,443,445,587,993,995,1433,1521,2049,
         2375,3306,3389,5432,5900,5985,6379,8080,8443,9000,9200,11211,27017]


class Ports(Scanner):
    name = "ports"

    async def scan(self, target: str) -> list[Finding]:
        hs = await self.hosts(target)
        sem = asyncio.Semaphore(self.cfg.concurrency)

        async def probe(h: str, p: int):
            async with sem:
                try:
                    rd, wr = await asyncio.wait_for(asyncio.open_connection(h, p), timeout=1.5)
                    banner = ""
                    try:
                        data = await asyncio.wait_for(rd.read(256), timeout=1.0)
                        banner = data.decode("utf-8", errors="ignore").strip()
                    except Exception:
                        pass
                    wr.close()
                    try:
                        await wr.wait_closed()
                    except Exception:
                        pass
                    return Finding(kind="port", key=f"{h}:{p}",
                                   value={"host": h, "port": p, "banner": banner[:200]})
                except Exception:
                    return None

        rs = await asyncio.gather(*[probe(h, p) for h in hs for p in PORTS])
        return [x for x in rs if x]