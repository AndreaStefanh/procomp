import os
import sys


def printUsage() -> None:

    print("ProComp v1.0.0 - Copyright © 2022 Andrea Stefan")
    print("License GPLv3: GNU GPL version 3 <https://gnu.org/licenses/gpl.html>")
    print("The source is hosted in github <https://github.com/AndreaStefanh/procomp>")
    print("usage: procomp [options] <configFile>")
    return

def printHelp() -> None:
    print("\noptions:")
    print("  -h, --help, -? |   Print this help screen in stdout")
    print("   -f,  --file   |   Change the default configuration file name")
    print("")
    return


def parserArgs() -> str:

    if len(sys.argv) < 2:

        if os.path.exists(".procomp.json") == True:
            return ".procomp.json"
        else:
            print("ERROR: unable to find '.procomp.json'")
            sys.exit(1)
    
    for i in range(0, len(sys.argv)):

        if i == 0:
            continue

        if sys.argv[i] == "-h" or sys.argv[i] == "--help" or sys.argv[i] == "-?":

            printUsage()
            printHelp()
            sys.exit(0)
        
        elif sys.argv[i] == "-f" or sys.argv[i] == "--file":

            if len(sys.argv) - i > 1:
                i += 1

                if os.path.exists(sys.argv[i]) == True:
                    return sys.argv[i]
                else:
                    print(f"ERROR: unable to find '{sys.argv[i]}'")
                    sys.exit(1)
                
            else:
                print("ERROR: the file was not specified")
                sys.exit(1)
        
        else:
            printUsage()
            print(f"ERROR: '{sys.argv[i]}' invalid option")
            sys.exit(1)

    return