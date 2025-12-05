<#
PowerShell helper to build the single-file exe and create an NSIS installer.

How to use:
- Ensure you have NSIS installed (makensis on PATH). If not, download from https://nsis.sourceforge.io/Download
- Run this script from the project root in PowerShell:
  .\.venv\Scripts\Activate.ps1
  .\build_installer.ps1

This script:
- Runs PyInstaller to produce `dist\BibliotecaApp.exe` (windowed)
- Runs `makensis installer.nsi` to produce `dist\BibliotecaAppInstaller.exe` (if makensis is available)
#>

Set-StrictMode -Version Latest

Write-Host "Building single-file executable with PyInstaller..."

# Activate venv if available
if (Test-Path ".\.venv\Scripts\Activate.ps1") {
    Write-Host "Activating .venv"
    & .\.venv\Scripts\Activate.ps1
}

# Build argument array and call Python with splatting to avoid quoting issues
$pyArgs = @(
    '-m',
    'PyInstaller',
    '--onefile',
    '--windowed',
    '--name=BibliotecaApp',
    '--add-data',
    'firebase-credentials.json;.',
    '--add-data',
    'guiBuild;guiBuild',
    'main.py'
)
Write-Host "Running: python $($pyArgs -join ' ')"
& python @pyArgs

if ($LASTEXITCODE -ne 0) {
    Write-Error "PyInstaller build failed (exit code $LASTEXITCODE). Fix errors above and retry."
    exit $LASTEXITCODE
}

Write-Host "PyInstaller build succeeded. Checking for NSIS (makensis)..."

try {
    $nsis = Get-Command makensis -ErrorAction Stop
    Write-Host "Found makensis at: $($nsis.Path)"
    Write-Host "Running makensis installer.nsi..."
    & makensis installer.nsi
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Installer created: dist\\BibliotecaAppInstaller.exe"
    } else {
        Write-Error "makensis exited with code $LASTEXITCODE"
    }
} catch {
    Write-Warning "makensis (NSIS) not found on PATH. Install NSIS from https://nsis.sourceforge.io/Download and re-run this script to produce the installer."
    Write-Host "Alternatively, open 'installer.nsi' in the NSIS editor and build manually."
}
