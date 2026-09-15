from __future__ import annotations
from .models import Snapshot, Change, Finding

VOLATILE = {"title", "duration_ms", "size"}


def diff(old: Snapshot, new: Snapshot) -> list[Change]:
    oi = old.idx()
    ni = new.idx()
    out: list[Change] = []
    for k, f in ni.items():
        if k not in oi:
            out.append(Change(kind="new", finding=f))
        elif _norm(oi[k]) != _norm(f):
            out.append(Change(kind="changed", finding=f, old=oi[k]))
    for k, f in oi.items():
        if k not in ni:
            out.append(Change(kind="gone", finding=f))
    return out


def _norm(f: Finding) -> dict:
    return {k: v for k, v in f.value.items() if k not in VOLATILE}