# recon-diff

**Passive attack-surface change detector.**

`recon-diff` collects passive signals from certificate transparency, DNS, and Wayback CDX, then stores timestamped snapshots so that changes can be reviewed over time.

> Use this tool only on domains you own or are authorized to assess.

## Requirements

- Windows PowerShell, macOS, or Linux
- Python 3.10 or newer
- Git
- Network access for the passive data sources

## Installation

The Python package is located in the `rd` directory, so install it from there.

### Windows PowerShell

Run these commands from any directory:

```powershell
git clone https://github.com/fevberr/recon-diff.git
Set-Location .\recon-diff\rd

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

If PowerShell blocks activation, you can either run the executable directly or allow scripts for your user account:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
git clone https://github.com/fevberr/recon-diff.git
cd recon-diff/rd

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

## Run the CLI

The installed command is `rd`. The package does **not** provide a `recon-diff` command.

### Windows PowerShell

When the virtual environment is activated, use `rd.exe`:

```powershell
rd.exe --help
rd.exe scan example.com --store .\snapshots
```

You can also use the executable without activating the environment:

```powershell
.\.venv\Scripts\rd.exe scan example.com --store .\snapshots
```

PowerShell has a built-in `rd` alias for `Remove-Item`, so `rd.exe` is intentional. Do not type the PowerShell prompt itself (`(.venv) PS ...>`) as part of the command.

### macOS/Linux

```bash
./.venv/bin/rd --help
./.venv/bin/rd scan example.com --store ./snapshots
```

## Commands

| Command | Description |
|---|---|
| `rd scan <domain> --store <path>` | Collect and save a snapshot of the target's passive attack surface. |
| `rd difftwo <domain> --store <path>` | Compare the two most recent snapshots. Requires at least two scans. |
| `rd targets` | Show the targets supported by the installed CLI. |

Run `rd.exe --help` on Windows or `rd --help` on macOS/Linux to see the commands available in your installed version.

## Example workflow

Run two scans at different times, then compare them:

```powershell
# Windows PowerShell
rd.exe scan example.com --store .\snapshots
# Wait, then run another scan
rd.exe scan example.com --store .\snapshots
rd.exe difftwo example.com --store .\snapshots
```

A successful scan prints the snapshot path, for example:

```text
-> snapshots\example.com\20260917T034631Z.json
```

## Windows troubleshooting

### `Fatal error in launcher` refers to the wrong Python path

If the error contains a path such as:

```text
C:\Users\...\a\rd\.venv\Scripts\python.exe
```

but your project is actually under:

```text
C:\Users\...\a\recon-diff\rd
```

then the virtual environment was moved or was created at a different location. Virtual environments contain launchers with absolute paths and should be recreated after moving them.

From `recon-diff\rd`, run:

```powershell
# Leave the old environment, if it is active
deactivate

# Remove only the broken local virtual environment
Remove-Item -Recurse -Force .\.venv

# Create a new environment at the current project location
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Use python -m pip so the pip executable cannot point at another environment
python -m pip install --upgrade pip
python -m pip install -e .

# Confirm the interpreter and CLI use this .venv
python -c "import sys; print(sys.executable)"
Get-Command rd.exe
rd.exe --help
```

The interpreter path should end with:

```text
recon-diff\rd\.venv\Scripts\python.exe
```

### `pip install -e .` fails with a launcher error

Use this instead of `pip install -e .`:

```powershell
python -m pip install -e .
```

This explicitly runs pip from the Python interpreter in the active environment.

### A directory path is reported as an unknown command

This is not a valid command:

```powershell
C:\Users\...\recon-diff\rd
```

Change directories with `cd` or `Set-Location`:

```powershell
cd C:\Users\...\recon-diff\rd
# or
Set-Location C:\Users\...\recon-diff\rd
```

### `rd` invokes `Remove-Item`

Use the executable extension:

```powershell
rd.exe --help
```

Alternatively, remove the alias for the current PowerShell session:

```powershell
Remove-Item Alias:rd -ErrorAction SilentlyContinue
rd --help
```

### Do not paste the prompt

Only paste the command after the prompt. For example, paste this:

```powershell
rd.exe scan example.com --store .\snapshots
```

Do not paste this entire displayed line:

```text
(.venv) PS C:\Users\...\recon-diff\rd> rd.exe scan example.com --store .\snapshots
```

## Development

The project uses an editable install, so source changes are immediately available after installation:

```powershell
python -m pip install -e .
```

The CLI entry point is defined in `pyproject.toml` as `rd = "rd.cli:app"`.

## License

MIT © 2026 fevberr

See [LICENSE](LICENSE) for the complete license text.
