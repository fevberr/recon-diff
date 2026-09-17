
# recon-diff

<img src="https://p16-tiktok-dm-sticker-sign-sg.ibyteimg.com/tos-alisg-i-dhq7zx4c1p-sg/d179a29e560642bba3707aa2ec9babd8~tplv-dhq7zx4c1p-full.awebp?rk3s=00edd399&x-expires=1792029789&x-signature=qrJJe26DGlzonOoaKdczYDcF0BE%3D" alt="RAHHHH" />

Passive attack surface change detection.

crt.sh • DNS • Wayback CDX — no wordlists.

---

## Overview

`recon-diff` watches a target over time and reports what changed in its exposed attack surface without needing a wordlist or active enumeration workflow.

It tracks changes across public data sources like:

- crt.sh
- DNS records
- Wayback CDX entries

This makes it useful for monitoring drift in a target’s external footprint over time.

---

## Built with

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

## Author

[fevberr](https://github.com/fevberr)

> super coolz guy btw

---

## Important setup note

The package layout and installed command names differ from the repo name:

- the Python package lives in `rd/`
- the installed CLI command is `rd`
- the diff subcommand is `difftwo` (not `diff`)

This is intentional and important for correct usage.

---

## Installation

<img src="https://cdn.simpleicons.org/python" alt="python" width="24">

```powershell
git clone https://github.com/fevberr/recon-diff.git
cd recon-diff\rd
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

On macOS/Linux:

```bash
git clone https://github.com/fevberr/recon-diff.git
cd recon-diff/rd
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

> Run `pip install -e .` from inside `rd/`.  
> The project configuration is located there, and running it from the repository root will fail with:
> “does not appear to be a Python project”

---

## Usage

<img src="https://cdn.simpleicons.org/gnometerminal" alt="terminal" width="24">

The installed command is `rd`, not `recon-diff`.

If you are on PowerShell, `rd` may be aliased to `Remove-Item`, so use the full executable path or remove the alias first.

```powershell
.\.venv\Scripts\rd.exe scan example.com --store .\snapshots
.\.venv\Scripts\rd.exe scan example.com --store .\snapshots
.\.venv\Scripts\rd.exe difftwo example.com --store .\snapshots
.\.venv\Scripts\rd.exe report example.com --out report.html
.\.venv\Scripts\rd.exe dashboard
```

If you want to use `rd` directly, run:

```powershell
Remove-Item Alias:rd
```

once in the session.

> `python -m rd` will not work because the package does not include a `__main__.py`.

---

## Commands

| Command | Description |
|---|---|
| `rd scan <domain> --store <path>` | Capture the current attack surface for a target |
| `rd difftwo <domain> --store <path>` | Compare the two most recent snapshots |
| `rd report <domain> --out <file>` | Export the results to an HTML report |
| `rd dashboard` | Launch the live dashboard view |

> Use `rd --help` to see the full available command list.  
> The names above reflect the installed CLI behavior. Older docs may mention `diff`, but the actual command is `difftwo`.

---

## Scan

```powershell
.\.venv\Scripts\rd.exe scan example.com --store .\snapshots
```

This creates a timestamped snapshot at:

```text
snapshots\<domain>\<UTC-timestamp>.json
```

---

## Diff

```powershell
.\.venv\Scripts\rd.exe difftwo example.com --store .\snapshots
```

This compares the two most recent snapshots for the target domain. At least two scans are required.

---

## Report

```powershell
.\.venv\Scripts\rd.exe report example.com --out report.html
```

Exports a generated HTML report for the target.

---

## Dashboard

```powershell
.\.venv\Scripts\rd.exe dashboard
```

Launches the dashboard for live monitoring and inspection.

---

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

MIT © 2026 fevberr

```text
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
```

If you want, I can also make it:
- more “hacker / offensive-security” styled,
- more minimal and clean,
- or more polished like a typical GitHub project landing page.
