# recon-diff
<img src="https://p16-tiktok-dm-sticker-sign-sg.ibyteimg.com/tos-alisg-i-dhq7zx4c1p-sg/d179a29e560642bba3707aa2ec9babd8~tplv-dhq7zx4c1p-full.awebp?rk3s=00edd399&x-expires=1792029789&x-signature=qrJJe26DGlzonOoaKdczYDcF0BE%3D" alt="RAHHHH">

**Passive attack surface change detector.**  
crt.sh · DNS · Wayback CDX — no wordlists

---

**Stack**

<p>
  <img src="https://cdn.simpleicons.org/python" alt="Python" width="20">
  <img src="https://cdn.simpleicons.org/gnubash" alt="Shell" width="20">
  <img src="https://cdn.simpleicons.org/git" alt="Git" width="20">
  <img src="https://cdn.simpleicons.org/html5" alt="HTML5" width="20">
  <img src="https://cdn.simpleicons.org/cloudflare" alt="Cloudflare" width="20">
  <img src="https://cdn.simpleicons.org/grafana" alt="Grafana" width="20">
  <img src="https://cdn.simpleicons.org/gnometerminal" alt="Terminal" width="20">
  <img src="https://cdn.simpleicons.org/json" alt="JSON" width="20">
</p>

---

**Author** — [fevberr](https://github.com/fevberr) *(super coolz guy btw)*

---

## Install

<img src="https://cdn.simpleicons.org/python" alt="python" width="24">

```powershell
git clone https://github.com/fevberr/recon-diff.git
cd recon-diff
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

---

## Use

<img src="https://cdn.simpleicons.org/gnubash" alt="shell" width="24">

```powershell
recon-diff scan example.com --store .\snapshots
recon-diff scan example.com --store .\snapshots
recon-diff diff example.com --store .\snapshots
recon-diff report example.com --out report.html
recon-diff dashboard
```

---

## Commands

<img src="https://cdn.simpleicons.org/gnometerminal" alt="terminal" width="24">

| Command | What it does |
|---|---|
| `recon-diff scan <domain> --store <path>` | Snapshot the target's current attack surface |
| `recon-diff diff <domain> --store <path>` | Compare the two most recent snapshots |
| `recon-diff report <domain> --out <file>` | Export an HTML report |
| `recon-diff dashboard` | Launch the live view |

---

## Scan

<img src="https://cdn.simpleicons.org/cloudflare" alt="cloudflare" width="24">

```powershell
recon-diff scan example.com --store .\snapshots
```

---

## Diff

<img src="https://cdn.simpleicons.org/git" alt="git" width="24">

```powershell
recon-diff diff example.com --store .\snapshots
```

---

## Report

<img src="https://cdn.simpleicons.org/html5" alt="html" width="24">

```powershell
recon-diff report example.com --out report.html
```

---

## Dashboard

<img src="https://cdn.simpleicons.org/grafana" alt="grafana" width="24">

```powershell
recon-diff dashboard
```

---

## Data sources

<img src="https://cdn.simpleicons.org/json" alt="json" width="24">

- **crt.sh** — certificate transparency logs, for subdomain discovery
- **DNS** — A / AAAA / CNAME / MX / TXT / NS records
- **Wayback CDX** — historical URL enumeration

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
