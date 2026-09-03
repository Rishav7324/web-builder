$ErrorActionPreference = 'Stop'
$Repo = 'https://github.com/Rishav7324/web-builder.git'
$Tmp = Join-Path $env:TEMP ("web-builder-install-" + [guid]::NewGuid().ToString())
try {
  if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'git is required.' }
  if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw 'Python 3 is required.' }
  Write-Host 'Installing Web Builder...'
  git clone --depth 1 --quiet $Repo $Tmp
  & python (Join-Path $Tmp 'installer/install.py') --global --targets all @args
  Write-Host 'Web Builder installed successfully.'
} finally {
  if (Test-Path $Tmp) { Remove-Item -Recurse -Force $Tmp }
}
