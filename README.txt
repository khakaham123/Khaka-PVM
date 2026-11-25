KHAKA DICTCAP PVM — WINDOWS x64 BUILD PACKAGE
=============================================

This is Khaka's own modified CPython source tree. It is NOT SafeSleep PVM
and does not copy SafeSleep's feature or flavour.

Khaka's feature: configurable maximum number of entries in dictionaries.

Interpreter API:
  sys.set_max_dict_size(n)
  sys.get_max_dict_size()

Rules:
  positive n = cap dictionary size
  0 or negative = disable cap
  updating an existing key is allowed
  inserting a new key beyond the cap raises ValueError

WINDOWS BUILD REQUIREMENT
-------------------------
The supplied Khaka archive has modified CPython source, not a precompiled
Windows Khaka interpreter. This package builds the native Windows interpreter.
WSL is NOT used.

Install Visual Studio 2022 Build Tools (or full Visual Studio) with:
  - Desktop development with C++
  - Windows 10/11 SDK

Build:
  1. Open "x64 Native Tools Command Prompt for VS 2022".
  2. Change directory to this extracted folder.
  3. Run: powershell -ExecutionPolicy Bypass -File .\build-khaka.ps1

Or open the folder in VS Code and run the same command in its terminal,
provided the terminal has the Visual Studio C++ build environment loaded.
The first build may take several minutes.

Run after build:
  .\khaka-python.cmd .\demo_khaka.py
  .\khaka-python.cmd your_script.py

Files:
  cpython-src/             CPython source with Khaka modifications applied
  dictcap.patch            Original source patch
  demo_khaka.py            Small feature demonstration
  original-demo_dictcap.py Full supplied test/demo
  build-khaka.ps1          Native Windows build script
  khaka-python.cmd         Launcher after successful build

No WSL/Linux environment is used. MSVC is required for the native build.
