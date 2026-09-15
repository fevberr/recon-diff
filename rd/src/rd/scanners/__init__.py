from __future__ import annotations
import asyncio
import time
from datetime import datetime, timezone

from ..config import Config
from ..models import Finding, Snapshot
from .subdomains import Subdomains
from .ports import Ports
from .http import Http
from .tls import Tls
from .js import Js
from .headers import Headers
from .robots import Robots
from .tech import Tech
from .waf import Waf

ALL = [Subdomains, Ports, Http, Tls, Js, Headers, Robots, Tech, Waf]


async def run(target: str, cfg: Config | None = None) -> Snapshot:
    cfg = cfg or Config()
    started = time.perf_counter()
    scanners = [c(cfg) for c in ALL]

    discovery = [s for s in scanners if s.name == "subdomains"]
    rest = [s for s in scanners if s not in discovery]

    findings: list[Finding] = []
    errors: list[str] = []

    if discovery:
        rs = await asyncio.gather(*[s.scan(target) for s in discovery],
                                  return_exceptions=True)
        for s, r in zip(discovery, rs):
            if isinstance(r, Exception):
                errors.append(f"{s.name}: {r}")
                continue
            findings.extend(r)

    if rest:
        rs = await asyncio.gather(*[s.scan(target) for s in rest],
                                  return_exceptions=True)
        for s, r in zip(rest, rs):
            if isinstance(r, Exception):
                errors.append(f"{s.name}: {r}")
                continue
            findings.extend(r)

    return Snapshot(
        target=target,
        timestamp=datetime.now(timezone.utc),
        duration_ms=int((time.perf_counter() - started) * 1000),
        findings=findings,
        errors=errors,
    )