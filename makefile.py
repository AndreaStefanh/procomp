#!/usr/bin/python3
# -*- using: utf-8 -*-
import os
import sys
import stat
import shutil

try:
    import PyInstaller.__main__
except ImportError:
    print("WARNING: Unable to find pyinstall")
    os.system("python3 -m pip install -r requirements.txt")
    import PyInstaller.__main__


def compile() -> None:

    PyInstaller.__main__.run([
        'src/main.py',
        '--onefile',
    ])

    return

def clearAll() -> None:

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
    
    return

def parseArgs() -> None:

    if len(sys.argv) > 1:
        for i in range(0, len(sys.argv)):

            if i == 0:
                continue

            if sys.argv[i] == "install":
                if os.getuid() != 0:
                    print("\33[91mERROR:\033[0m For this operation need root permition")
                    exit(1)
                
                if os.path.exists("bin/procomp") == True:
                    shutil.copyfile("bin/procomp", "/usr/bin/procomp")

                    if os.path.exists("/usr/bin/procomp") == True:
                        os.chmod(
                            "/usr/bin/procomp",
                            stat.S_IXUSR |
                            stat.S_IXGRP |
                            stat.S_IXOTH |
                            stat.S_IRUSR |
                            stat.S_IRGRP |
                            stat.S_IROTH
                        )
                    else:
                        print("\33[91mERROR:\033[0m unable to find '/usr/bin/procomp'")
                        exit(1)
                else:
                    print("\33[91mERROR:\033[0m unable to find 'bin/procomp'")
                    exit(1)
            else:
                print(f"\33[91mERROR:\033[0m '{sys.argv[i]}' invalid option")

    return


def main() -> None:

    compile()
    clearAll()
    parseArgs()
    return


if __name__ == "__main__":
    main()