

# recon-diff


<img src="https://p16-tiktok-dm-sticker-sign-sg.ibyteimg.com/tos-alisg-i-dhq7zx4c1p-sg/d179a29e560642bba3707aa2ec9babd8~tplv-dhq7zx4c1p-full.awebp?rk3s=00edd399&x-expires=1792029789&x-signature=qrJJe26DGlzonOoaKdczYDcF0BE%3D" alt="RAHHHH"> by fevber (super coolz guy btw)

Passive attack surface change detector. crt.sh, DNS, Wayback CDX. No wordlists.

## Install

<img src="https://cdn.simpleicons.org/python" alt="python" width="24"> pip install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

## Use

<img src="https://cdn.simpleicons.org/gnubash" alt="shell" width="24"> cli

```powershell
recon-diff scan example.com --store .\snapshots
recon-diff scan example.com --store .\snapshots
recon-diff diff example.com --store .\snapshots
recon-diff report example.com --out report.html
recon-diff dashboard
```

## Options

<img src="https://cdn.simpleicons.org/gnometerminal" alt="terminal" width="24"> flags

```powershell
recon-diff scan <domain> --store <path>     # snapshot target
recon-diff diff <domain> --store <path>     # compare last two snapshots
recon-diff report <domain> --out <file>     # export HTML report
recon-diff dashboard                        # launch live view
```

## Scan

<img src="https://cdn.simpleicons.org/cloudflare" alt="scan" width="24"> snapshot

```powershell
recon-diff scan example.com --store .\snapshots
```

## Diff

<img src="https://cdn.simpleicons.org/git" alt="diff" width="24"> compare

```powershell
recon-diff diff example.com --store .\snapshots
```

## Report

<img src="https://cdn.simpleicons.org/html5" alt="report" width="24"> html

```powershell
recon-diff report example.com --out report.html
```

## Dashboard

<img src="https://cdn.simpleicons.org/grafana" alt="dashboard" width="24"> live

```powershell
recon-diff dashboard
```
