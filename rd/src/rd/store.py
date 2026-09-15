from __future__ import annotations
import json
from pathlib import Path
from datetime import timezone
from .models import Snapshot


def _dir(store: Path, target: str) -> Path:
    safe = target.replace("/", "_").replace(":", "_")
    d = store / safe
    d.mkdir(parents=True, exist_ok=True)
    return d


def save(store: Path, snap: Snapshot) -> Path:
    d = _dir(store, snap.target)
    ts = snap.timestamp.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    f = d / f"{ts}.json"
    f.write_text(snap.model_dump_json(indent=2), encoding="utf-8")
    _index(store, snap, f)
    return f


def load(store: Path, target: str, limit: int = 2) -> list[Snapshot]:
    d = _dir(store, target)
    fs = sorted(d.glob("*.json"))
    return [Snapshot.model_validate_json(x.read_text(encoding="utf-8")) for x in fs[-limit:]]


def latest(store: Path, target: str) -> Snapshot | None:
    a = load(store, target, 1)
    return a[0] if a else None


def list_targets(store: Path) -> list[str]:
    if not store.exists():
        return []
    return sorted(x.name for x in store.iterdir() if x.is_dir())


def _index(store: Path, snap: Snapshot, f: Path) -> None:
    ip = store / "index.json"
    v: dict = {}
    if ip.exists():
        try:
            v = json.loads(ip.read_text(encoding="utf-8"))
        except Exception:
            v = {}
    v.setdefault(snap.target, []).append({
        "path": str(f.relative_to(store)),
        "ts": snap.timestamp.isoformat(),
        "findings": len(snap.findings),
    })
    ip.write_text(json.dumps(v, indent=2), encoding="utf-8")