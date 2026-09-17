# recon-diff

<img src="https://p16-tiktok-dm-sticker-sign-sg.ibyteimg.com/tos-alisg-i-dhq7zx4c1p-sg/d179a29e560642bba3707aa2ec9babd8~tplv-dhq7zx4c1p-full.awebp?rk3s=00edd399&x-expires=1792029789&x-signature=qrJ[...]">

**Passive attack surface change detector.**  
crt.sh · DNS · Wayback CDX — no wordlists

---

## Used

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

## Install

### Linux/macOS

```bash
git clone https://github.com/fevberr/recon-diff.git
cd recon-diff/rd
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

### Windows (PowerShell)

Run these commands from the parent directory. If `recon-diff` already exists, do not clone it again—just enter the existing directory.

```powershell
git clone https://github.com/fevberr/recon-diff.git
cd .\recon-diff\rd
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

Use `python -m pip`, not `pip`, because a stale Windows `pip.exe` launcher can still point to a previous location of the virtual environment.

> If `source` fails, you're in PowerShell, not Bash. Use `..\.venv\Scripts\Activate.ps1` from the `rd` directory instead.

> Install from the `rd/` directory, where the package configuration lives.

## Quick start

```bash
rd scan example.com --store ./snapshots
rd difftwo example.com --store ./snapshots
rd report example.com --out report.html
rd dashboard
```

Run `rd --help` for all available options.

### PowerShell note

PowerShell may treat `rd` as the built-in `Remove-Item` alias. Use the installed executable directly:

```powershell
.\.venv\Scripts\rd.exe scan example.com --store .\snapshots
```

Or remove the alias for the current session and then use `rd` normally:

```powershell
Remove-Item Alias:rd
rd scan example.com --store .\snapshots
```

## Fixing a broken or moved virtual environment

The error `Fatal error in launcher ... cannot find the file specified` means the `.venv` was created in a different folder or was moved with the project. Virtual environments are not portable; delete and recreate it from the current `rd` directory:

```powershell
cd C:\Users\11184581_clases\a\recon-diff\rd
deactivate  # ignore the error if no environment is active
Remove-Item -Recurse -Force .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
.\.venv\Scripts\rd.exe --help
```

If PowerShell blocks activation, run this once for the current PowerShell window, then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Commands

| Command | Description |
| --- | --- |
| `rd scan <domain>` | Save a snapshot of the domain's public attack surface |
| `rd difftwo <domain>` | Compare the two latest snapshots |
| `rd report <domain>` | Generate an HTML report |
| `rd dashboard` | Open the live dashboard |

`difftwo` requires at least two snapshots.

## Data sources

- Certificate transparency via [crt.sh](https://crt.sh/)
- DNS records
- Historical URLs via [Wayback CDX](https://web.archive.org/web/)

## License

[MIT](https://github.com/fevberr/recon-diff/blob/main/LICENSE) © 2026 [fevberr](https://github.com/fevberr)
