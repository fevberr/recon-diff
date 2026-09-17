# recon-diff

<img src="https://p16-tiktok-dm-sticker-sign-sg.ibyteimg.com/tos-alisg-i-dhq7zx4c1p-sg/d179a29e560642bba3707aa2ec9babd8~tplv-dhq7zx4c1p-full.awebp?rk3s=00edd399&x-expires=1792029789&x-signature=qrJJe26DGlzonOoaKdczYDcF0BE%3D" alt="RAHHHH">

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

[MIT](https://github.com/fevberr/recon-diff/blob/main/LICENSE) © 2026 [fevberr](https://github.com/fevberr)
