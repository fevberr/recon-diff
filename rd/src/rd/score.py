from __future__ import annotations
import re
from .models import Change, Finding

INTERESTING = re.compile(
    r"(admin|staging|dev|test|jenkins|grafana|kibana|git|gitlab|vpn|sso|"
    r"login|portal|internal|beta|swagger)", re.IGNORECASE)
STATIC = re.compile(r"(cdn|static|assets|img|media|fonts)", re.IGNORECASE)
DB = {3306, 5432, 6379, 27017, 9200, 1433, 1521, 11211, 9042}
ADMIN = {22, 3389, 5900, 5985, 5986, 8291}
WEB = {80, 443}


def annotate(cs: list[Change]) -> list[Change]:
    return [go(c) for c in cs]


def go(c: Change) -> Change:
    s, r = 0, []
    f = c.finding
    if c.kind == "new":
        s += 10
        r.append("new")
        for fn in (sub, port, http, tls, js, tech, robots, bucket, headers,
                   takeover, wayback, favicon, dns, waf, asn):
            p, w = fn(f)
            s += p
            r.extend(w)
    elif c.kind == "changed":
        s += 5
        r.append("changed")
        p, w = changed(c)
        s += p
        r.extend(w)
    elif c.kind == "gone":
        s += 5
        r.append("gone")
    c.score = max(0, min(100, s))
    c.reasons = r
    return c


def sub(f: Finding):
    if f.kind != "subdomain": return 0, []
    h = f.key.lower()
    if INTERESTING.search(h): return 75, ["interesting subdomain"]
    if STATIC.search(h): return 5, ["static host"]
    return 25, ["subdomain"]


def port(f: Finding):
    if f.kind != "port": return 0, []
    p = f.value.get("port", 0)
    if p in DB: return 85, [f"db port {p}"]
    if p in ADMIN: return 60, [f"admin port {p}"]
    if p in WEB: return 5, [f"web port {p}"]
    return 45, [f"port {p}"]


def http(f: Finding):
    if f.kind != "http": return 0, []
    s, w = 0, []
    v = f.value
    if v.get("status") in (401, 403):
        s += 20; w.append("auth wall")
    if v.get("server"):
        s += 10; w.append(f"server {v['server']}")
    t = (v.get("title") or "").lower()
    for k in ("admin", "login", "dashboard", "portal", "jenkins"):
        if k in t:
            s += 30; w.append(f"title {k}"); break
    return s, w


def tls(f: Finding):
    if f.kind != "tls": return 0, []
    s, w = 25, ["tls"]
    v = f.value
    if v.get("expired"): s += 20; w.append("expired")
    if v.get("self_signed"): s += 25; w.append("self-signed")
    return s, w


def js(f: Finding):
    if f.kind != "js": return 0, []
    s, w = 20, ["js"]
    if f.value.get("hints"):
        s += 50; w.append(f"hints {f.value['hints'][:3]}")
    return s, w


def tech(f: Finding):
    if f.kind != "tech": return 0, []
    n = (f.value.get("name") or "").lower()
    if any(x in n for x in ("jenkins", "grafana", "kibana", "wordpress", "drupal")):
        return 55, [f"tech {n}"]
    return 20, [f"tech {n}"]


def robots(f: Finding):
    if f.kind != "robots": return 0, []
    d = f.value.get("disallow", [])
    s = [p for p in d if any(k in p.lower() for k in ("admin", "private", "backup", ".git"))]
    if s: return 60, [f"robots {s[:3]}"]
    return 15, ["robots"]


def bucket(f: Finding):
    if f.kind != "bucket": return 0, []
    if f.value.get("public"): return 80, ["public bucket"]
    return 40, ["bucket"]


def headers(f: Finding):
    if f.kind != "headers": return 0, []
    m = f.value.get("missing", [])
    return min(len(m) * 5, 30), [f"missing {x}" for x in m[:4]]


def takeover(f: Finding):
    if f.kind != "takeover": return 0, []
    return 95, [f"takeover {f.value.get('fingerprint')}"]


def wayback(f: Finding):
    if f.kind != "wayback": return 0, []
    u = f.key.lower()
    if any(k in u for k in ("admin", "config", "backup", ".git", ".env", "api")):
        return 70, ["wayback sensitive"]
    return 25, ["wayback"]


def favicon(f: Finding):
    if f.kind != "favicon": return 0, []
    return 15, ["favicon"]


def dns(f: Finding):
    if f.kind != "dns": return 0, []
    return 15, [f"dns {f.value.get('record', '')}"]


def waf(f: Finding):
    if f.kind != "waf": return 0, []
    return 5, [f"waf {f.value.get('name')}"]


def asn(f: Finding):
    if f.kind != "asn": return 0, []
    return 10, [f"asn {f.value.get('asn')}"]


def changed(c: Change):
    if c.old is None: return 0, []
    s, w = 0, []
    a, b = c.old.value, c.finding.value
    if c.finding.kind == "http":
        ah = {k.lower(): v for k, v in a.get("headers", {}).items()}
        bh = {k.lower(): v for k, v in b.get("headers", {}).items()}
        for k in bh:
            if k in ah and ah[k] != bh[k]:
                if k in ("server", "x-powered-by"):
                    s += 40; w.append(f"version {k}")
                else:
                    s += 20; w.append(f"header {k}")
        if a.get("status") != b.get("status"):
            s += 30; w.append("status")
    elif c.finding.kind == "js":
        s += 15; w.append("js deploy")
    elif c.finding.kind == "tls":
        s += 30; w.append("cert rotated")
    return s, w