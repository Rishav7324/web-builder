$ErrorActionPreference = 'Stop'
$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = Split-Path -Parent $ScriptRoot
$ArgsList = $args
if (Get-Command python -ErrorAction SilentlyContinue) {
  & python (Join-Path $ScriptRoot 'install.py') @ArgsList
  exit $LASTEXITCODE
}
if (Get-Command py -ErrorAction SilentlyContinue) {
  & py -3 (Join-Path $ScriptRoot 'install.py') @ArgsList
  exit $LASTEXITCODE
}
Write-Error 'Python 3 is required. Install Python 3 and run installer/install.py.'
