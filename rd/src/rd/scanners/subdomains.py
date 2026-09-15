from __future__ import annotations
import re
import httpx
from ..models import Finding
from .base import Scanner


class Subdomains(Scanner):
    name = "subdomains"

    async def scan(self, target: str) -> list[Finding]:
        s = {target, f"www.{target}"}
        s |= await self._crtsh(target)
        return [Finding(kind="subdomain", key=x.lower(), value={"host": x.lower()})
                for x in sorted(s)]

    async def _crtsh(self, target: str) -> set[str]:
        url = f"https://crt.sh/?q=%25.{target}&output=json"
        try:
            async with httpx.AsyncClient(timeout=25.0,
                                         headers={"User-Agent": self.cfg.user_agent},
                                         follow_redirects=True) as c:
                r = await c.get(url)
                if r.status_code != 200:
                    return set()
                data = r.json()
        except Exception:
            return set()
        out: set[str] = set()
        for row in data:
            names = (row.get("name_value") or "").splitlines()
            names += (row.get("common_name") or "").splitlines()
            for n in names:
                n = n.strip().lower().lstrip("*.").rstrip(".")
                if not n or " " in n: continue
                if not n.endswith("." + target) and n != target: continue
                if re.match(r"^[a-z0-9._-]+$", n):
                    out.add(n)
        return out