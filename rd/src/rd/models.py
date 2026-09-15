from __future__ import annotations
from datetime import datetime
from typing import Any, Literal
from pydantic import BaseModel, Field


class Finding(BaseModel):
    kind: str
    key: str
    value: dict[str, Any] = {}
    score: int = 0


class Snapshot(BaseModel):
    target: str
    timestamp: datetime
    duration_ms: int = 0
    findings: list[Finding] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)

    def idx(self) -> dict[str, Finding]:
        return {f"{f.kind}:{f.key}": f for f in self.findings}

    def kind(self, k: str) -> list[Finding]:
        return [f for f in self.findings if f.kind == k]


class Change(BaseModel):
    kind: Literal["new", "gone", "changed"]
    finding: Finding
    old: Finding | None = None
    score: int = 0
    reasons: list[str] = Field(default_factory=list)

    def label(self) -> str:
        t = {"new": "[+] ", "gone": "[-] ", "changed": "[~] "}[self.kind]
        return f"{t}{self.finding.kind}:{self.finding.key} ({self.score})"