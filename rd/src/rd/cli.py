from __future__ import annotations
import asyncio
from pathlib import Path
import typer
from rich.console import Console
from rich.table import Table

from . import scanners
from .store import save, load, list_targets
from .differ import diff
from .score import annotate
from .notify import slack, discord
from .config import load as load_config

app = typer.Typer(no_args_is_help=True)
console = Console()


@app.command()
def scan(
    target: str,
    store: Path = typer.Option(Path("./snapshots"), "--store", "-s"),
    slack_webhook: str = typer.Option("", "--slack-webhook"),
    discord_webhook: str = typer.Option("", "--discord-webhook"),
    min_score: int = typer.Option(0, "--min-score"),
):
    cfg = load_config(Path("rd.yaml"))
    cfg.store = store
    prev = load(store, target, limit=1)
    with console.status(f"scanning {target}..."):
        snap = asyncio.run(scanners.run(target, cfg))
    path = save(store, snap)
    console.print(f"-> {path}")
    console.print(f"{len(snap.findings)} findings in {snap.duration_ms} ms")
    for e in snap.errors:
        console.print(f"[yellow]! {e}[/yellow]")

    if not prev:
        console.print("[yellow]baseline created[/yellow]")
        _baseline(snap)
        return

    cs = annotate(diff(prev[0], snap))
    if not cs:
        console.print("[green]no changes[/green]")
        return
    _print(target, cs, min_score)
    filtered = [c for c in cs if c.score >= min_score]
    if slack_webhook:
        slack(slack_webhook, target, filtered)
    if discord_webhook:
        discord(discord_webhook, target, filtered)


@app.command()
def difftwo(
    target: str,
    store: Path = typer.Option(Path("./snapshots"), "--store", "-s"),
    min_score: int = typer.Option(0, "--min-score"),
):
    ss = load(store, target, limit=2)
    if len(ss) < 2:
        console.print("[red]need two snapshots[/red]")
        raise typer.Exit(1)
    _print(target, annotate(diff(ss[0], ss[1])), min_score)


@app.command()
def targets(store: Path = typer.Option(Path("./snapshots"), "--store", "-s")):
    for t in list_targets(store):
        console.print(t)


def _baseline(snap) -> None:
    from collections import Counter
    counts = Counter(f.kind for f in snap.findings)
    t = Table(title=f"baseline - {snap.target}")
    t.add_column("layer")
    t.add_column("count", justify="right")
    for k, v in sorted(counts.items()):
        t.add_row(k, str(v))
    console.print(t)


def _print(target: str, changes, min_score: int) -> None:
    t = Table(title=f"rd - {target}")
    t.add_column("")
    t.add_column("kind")
    t.add_column("key")
    t.add_column("score", justify="right")
    t.add_column("reasons", overflow="fold")
    color = {"new": "green", "gone": "red", "changed": "yellow"}
    mark = {"new": "+", "gone": "-", "changed": "~"}
    shown = 0
    for c in sorted(changes, key=lambda x: -x.score):
        if c.score < min_score:
            continue
        shown += 1
        t.add_row(f"[{color[c.kind]}]{mark[c.kind]}[/]",
                  c.finding.kind, c.finding.key, str(c.score),
                  "; ".join(c.reasons[:3]))
    if shown == 0:
        console.print("[green]nothing above threshold[/green]")
        return
    console.print(t)


if __name__ == "__main__":
    app()