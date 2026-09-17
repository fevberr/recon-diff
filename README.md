# recon-diff

**Track changes to a domain's public attack surface over time.**

`recon-diff` uses passive sources—**crt.sh, DNS, and Wayback CDX**—to capture snapshots and show what changed. No wordlists. No active scanning.

## Install

```bash
git clone https://github.com/fevberr/recon-diff.git
cd recon-diff/rd
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -e .
```

> Install from the `rd/` directory, where the package configuration lives.

## Quick start

```bash
rd scan example.com --store ./snapshots
rd scan example.com --store ./snapshots
rd difftwo example.com --store ./snapshots
rd report example.com --out report.html
rd dashboard
```

Run `rd --help` for all available options.

### PowerShell

PowerShell may alias `rd` to `Remove-Item`. Use the executable directly:

```powershell
.\.venv\Scripts\rd.exe scan example.com --store .\snapshots
```

Or remove the alias for the current session:

```powershell
Remove-Item Alias:rd
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
- Historical URLs via [Wayback CDX](https://web.archive.org/cdx/)

## License

[MIT](LICENSE) © 2026 [fevberr](https://github.com/fevberr)
