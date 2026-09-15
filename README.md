
# recon-diff
<img src="https://p16-tiktok-dm-sticker-sign-sg.ibyteimg.com/tos-alisg-i-dhq7zx4c1p-sg/d179a29e560642bba3707aa2ec9babd8~tplv-dhq7zx4c1p-full.awebp?rk3s=00edd399&x-expires=1792029789&x-signature=qrJJe26DGlzonOoaKdczYDcF0BE%3D" alt="RAHHHH">

**Passive attack surface change detector.**  
crt.sh · DNS · Wayback CDX — no wordlists

---
**Used**

<p>
  <img src="https://cdn.simpleicons.org/python" alt="Python" width="20">
  <img src="https://cdn.simpleicons.org/gnubash" alt="Shell" width="20">
  <img src="https://cdn.simpleicons.org/git" alt="Git" width="20">
  <img src="https://cdn.simpleicons.org/sqlite" alt="SQLite" width="20">
  <img src="https://cdn.simpleicons.org/docker" alt="Docker" width="20">
  <img src="https://cdn.simpleicons.org/githubactions" alt="GitHub Actions" width="20">
  <img src="https://cdn.simpleicons.org/json" alt="JSON" width="20">
</p>

---

**Author** — [fevberr](https://github.com/fevberr) *(super coolz guy btw)*

---

> **Heads up:** The install path and CLI differ from what you might expect. The packaging file lives in `rd/`, the installed command is `rd` (not `recon-diff`), and the diff subcommand is `difftwo` (not `diff`). Details below.

---

## Install

<img src="https://cdn.simpleicons.org/python" alt="python" width="24">

```powershell
git clone https://github.com/fevberr/recon-diff.git
cd recon-diff\rd
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

> On macOS/Linux, activate with `source .venv/bin/activate` instead.
>
> Run `pip install -e .` from **inside `rd/`** — that's where `pyproject.toml` lives. From the repo root it fails with *"does not appear to be a Python project"*.

---

## Use

<img src="https://cdn.simpleicons.org/gnubash" alt="shell" width="24">

The installed command is **`rd`**, not `recon-diff`. PowerShell aliases `rd` to `Remove-Item`, so call the executable by full path (or remove the alias first).

```powershell
..\.venv\Scripts\rd.exe scan example.com --store .\snapshots
..\.venv\Scripts\rd.exe scan example.com --store .\snapshots
..\.venv\Scripts\rd.exe difftwo example.com --store .\snapshots
..\.venv\Scripts\rd.exe report example.com --out report.html
..\.venv\Scripts\rd.exe dashboard
```

> Prefer just `rd`? Run `Remove-Item Alias:rd` once per session.
> `python -m rd` will **not** work — the package has no `__main__.py`.

---

## Commands

<img src="https://cdn.simpleicons.org/gnometerminal" alt="terminal" width="24">

| Command | What it does |
|---|---|
| `rd scan <domain> --store <path>` | Snapshot the target's current attack surface |
| `rd difftwo <domain> --store <path>` | Compare the two most recent snapshots |
| `rd report <domain> --out <file>` | Export an HTML report |
| `rd dashboard` | Launch the live view |

> Run `rd --help` to list the actual available commands. The names above reflect the installed CLI; earlier docs listed `diff`, which the tool rejects in favor of `difftwo`.

---

## Scan

<img src="https://cdn.simpleicons.org/cloudflare" alt="cloudflare" width="24">

```powershell
..\.venv\Scripts\rd.exe scan example.com --store .\snapshots
```

Writes a timestamped snapshot to `snapshots\<domain>\<UTC-timestamp>.json`.

---

## Diff

<img src="https://cdn.simpleicons.org/git" alt="git" width="24">

```powershell
..\.venv\Scripts\rd.exe difftwo example.com --store .\snapshots
```

Compares the two most recent snapshots. Requires at least two scans.

---

## Report

<img src="https://cdn.simpleicons.org/html5" alt="html" width="24">

```powershell
..\.venv\Scripts\rd.exe report example.com --out report.html
```

---

## Dashboard

<img src="https://cdn.simpleicons.org/grafana" alt="grafana" width="24">

```powershell
..\.venv\Scripts\rd.exe dashboard
```

---

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

MIT © 2026 fevberr

```
MIT License

Copyright (c) 2026 fevberr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
