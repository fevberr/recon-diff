from __future__ import annotations
import httpx
from .models import Change


def _fmt(t: str, cs: list[Change]) -> str:
    out = [f"rd - {t}"]
    for c in sorted(cs, key=lambda x: -x.score):
        out.append(c.label())
    return "\n".join(out)


def slack(w: str, t: str, cs: list[Change]) -> None:
    if cs:
        httpx.post(w, json={"text": _fmt(t, cs)}, timeout=10.0)


def discord(w: str, t: str, cs: list[Change]) -> None:
    if cs:
        httpx.post(w, json={"content": _fmt(t, cs)}, timeout=10.0)