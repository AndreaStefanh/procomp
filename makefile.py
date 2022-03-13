#!/usr/bin/python3
# -*- using: utf-8 -*-
import os
import shutil

try:
    import PyInstaller.__main__
except ImportError:
    print("WARNING: Unable to find pyinstall")
    os.system("python3 -m pip install -r requirements.txt")
    import PyInstaller.__main__

PyInstaller.__main__.run([
    'src/main.py',
    '--onefile',
])

if os.path.exists("main.spec") == True:
    os.remove("main.spec")
if os.path.exists("build") == True:
    shutil.rmtree("build")
if os.path.exists("src/__pycache__") == True:
    shutil.rmtree("src/__pycache__")
if os.path.exists("dist") == True:
    os.makedirs("bin", exist_ok=True)
    shutil.move("dist/main", "bin/procomp")
    shutil.rmtree("dist")