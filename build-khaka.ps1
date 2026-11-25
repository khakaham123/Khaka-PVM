$ErrorActionPreference = 'Stop'
$Root = $PSScriptRoot
$Source = Join-Path $Root 'cpython-src'
$Build = Join-Path $Source 'PCbuild\build.bat'
if (-not (Test-Path $Build)) { throw "CPython source/build files are missing." }
if (-not (Get-Command cl.exe -ErrorAction SilentlyContinue)) {
    Write-Host "MSVC environment not detected." -ForegroundColor Yellow
    Write-Host "Install Visual Studio 2022 Build Tools + Desktop development with C++ + Windows 10/11 SDK."
    Write-Host "Then open 'x64 Native Tools Command Prompt for VS 2022' and run this script again."
    exit 2
}
Push-Location $Source
try {
    & cmd.exe /c "PCbuild\build.bat -p x64 -c Release"
    if ($LASTEXITCODE -ne 0) { throw "CPython build failed: $LASTEXITCODE" }
} finally { Pop-Location }
$Python = Join-Path $Source 'PCbuild\amd64\python.exe'
if (-not (Test-Path $Python)) { throw "Build finished but python.exe was not found." }
@'
@echo off
"%~dp0cpython-src\PCbuild\amd64\python.exe" %*
exit /b %errorlevel%
'@ | Set-Content -Encoding ASCII (Join-Path $Root 'khaka-python.cmd')
Write-Host "Khaka PVM built successfully." -ForegroundColor Green
Write-Host "Run: .\khaka-python.cmd .\demo_khaka.py"
& $Python (Join-Path $Root 'demo_khaka.py')
