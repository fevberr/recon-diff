# recon-diff

**Passive attack-surface change detector for domains.**

recon-diff collects public information from certificate transparency, DNS, and the Wayback Machine, then compares snapshots so you can see what changed over time.

## Install

Choose the instructions for your operating system.

### Windows PowerShell

```powershell
git clone https://github.com/fevberr/recon-diff.git
Set-Location .\recon-diff\rd
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

If PowerShell does not allow the activation script, run this once in the same window and activate again:

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

Create a first snapshot:

### Windows PowerShell

PowerShell uses `rd` as an alias for `Remove-Item`, so run the executable directly:

```powershell
.\.venv\Scripts\rd.exe scan example.com --store .\snapshots
```

### Linux/macOS

```bash
rd scan example.com --store ./snapshots
```

Run the scan again later to compare it with the previous snapshot:

```text
rd scan example.com --store ./snapshots
```

On Windows, use `.\.venv\Scripts\rd.exe` instead of `rd` in the command above.

## Commands

| Command | What it does |
| --- | --- |
| `rd scan <domain>` | Collect a snapshot and compare it with the previous one |
| `rd difftwo <domain>` | Compare the two most recent snapshots |
| `rd targets` | List domains with saved snapshots |

All commands support a custom snapshot directory:

```text
--store ./snapshots
```

On Windows PowerShell, use:

```powershell
--store .\snapshots
```

Run the help command to see every available option.

### Windows

```powershell
.\.venv\Scripts\rd.exe --help
```

### Linux/macOS

```bash
rd --help
```

## Data sources

- Certificate transparency via [crt.sh](https://crt.sh/)
- DNS records
- Historical URLs via [Wayback CDX](https://web.archive.org/cdx/)

## License

[MIT](https://github.com/fevberr/recon-diff/blob/main/LICENSE) © 2026 [fevberr](https://github.com/fevberr)
