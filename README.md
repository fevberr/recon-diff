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

## Install

### Windows PowerShell

The Python project is inside the `rd` folder. Copy and paste these commands from the folder that contains `recon-diff`:

```powershell
git clone https://github.com/fevberr/recon-diff.git
cd .\recon-diff\rd
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

After the install finishes, verify it:

```powershell
.\.venv\Scripts\rd.exe --help
```

If you already cloned the repository, do not run `git clone` again. Start here instead:

```powershell
cd .\recon-diff\rd
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

If you are already inside `C:\Users\...\recon-diff`, use this instead:

```powershell
cd .\rd
```

If PowerShell blocks activation, run this once in the current PowerShell window and then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
git clone https://github.com/fevberr/recon-diff.git
cd recon-diff/rd
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

## Quick start

### Windows PowerShell

PowerShell has a built-in `rd` alias for `Remove-Item`. Use the installed executable so PowerShell does not run the wrong command:

```powershell
.\.venv\Scripts\rd.exe scan example.com --store .\snapshots
```

Run the command again later to compare the new snapshot with the previous one:

```powershell
.\.venv\Scripts\rd.exe scan example.com --store .\snapshots
```

### Linux/macOS

```bash
rd scan example.com --store ./snapshots
```

Run the command again later to compare the new snapshot with the previous one:

```bash
rd scan example.com --store ./snapshots
```

## Commands

| Command | What it does |
| --- | --- |
| `rd scan <domain>` | Collect a snapshot and compare it with the previous one |
| `rd difftwo <domain>` | Compare the two most recent snapshots |
| `rd targets` | List domains with saved snapshots |

On Windows, replace `rd` with `.\.venv\Scripts\rd.exe`.

Run the help command to see every available option:

```powershell
.\.venv\Scripts\rd.exe --help
```

## Data sources

- Certificate transparency via [crt.sh](https://crt.sh/)
- DNS records
- Historical URLs via [Wayback CDX](https://web.archive.org/cdx/)

## License

[MIT](https://github.com/fevberr/recon-diff/blob/main/LICENSE) © 2026 [fevberr](https://github.com/fevberr)
