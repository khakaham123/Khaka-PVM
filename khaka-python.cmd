@echo off
if not exist "%~dp0cpython-src\PCbuild\amd64\python.exe" (
  echo Khaka PVM is not built yet. Run build-khaka.ps1 first.
  exit /b 2
)
"%~dp0cpython-src\PCbuild\amd64\python.exe" %*
exit /b %errorlevel%
