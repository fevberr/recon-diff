from __future__ import annotations
import asyncio
import ssl
import socket
from datetime import datetime
from ..models import Finding
from .base import Scanner


class Tls(Scanner):
    name = "tls"

    async def scan(self, target: str) -> list[Finding]:
        hs = await self.hosts(target)
        sem = asyncio.Semaphore(self.cfg.concurrency)

        async def probe(h: str):
            async with sem:
                loop = asyncio.get_running_loop()
                info = await loop.run_in_executor(None, _fetch, h)
                if not info:
                    return None
                return Finding(kind="tls", key=h, value=info)

        rs = await asyncio.gather(*[probe(h) for h in hs])
        return [x for x in rs if x]


def _fetch(host: str):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with socket.create_connection((host, 443), timeout=5) as sk:
            with ctx.wrap_socket(sk, server_hostname=host) as ss:
                cert = ss.getpeercert()
                proto = ss.version()
                na = cert.get("notAfter")
                exp = False
                if na:
                    try:
                        d = datetime.strptime(na, "%b %d %H:%M:%S %Y %Z")
                        exp = d < datetime.utcnow()
                    except Exception:
                        pass
                iss = dict(x[0] for x in cert.get("issuer", []))
                sub = dict(x[0] for x in cert.get("subject", []))
                return {
                    "subject": sub, "issuer": iss, "notAfter": na,
                    "protocol": proto, "expired": exp,
                    "self_signed": iss == sub,
                }
    except Exception:
        return None