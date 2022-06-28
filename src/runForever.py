import os
import sys
import time
import stat
import datetime

from parserConfig import *


def clearScr() -> None:

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def reloadConfig(FileParsed :FileKeyword, maFiles :int) -> FileKeyword:

    if maFiles == 0:
        print("ERROR: no files were passed")
        sys.exit(1)

    for file in FileParsed.files:
        FileParsed.modificationTime.append(time.ctime(os.stat(file)[stat.ST_MTIME]))

    if FileParsed.calledTime == False:
        FileParsed.time = 0.5
    else:
        if FileParsed.time < 0:
            print("ERROR: you cannot pause with a number less than 0")
            sys.exit(1)

    if FileParsed.silent == True:
        FileParsed.command = FileParsed.command + " >/dev/null 2>/dev/null"
    
    return FileParsed

def compileExec(FileParsed :FileKeyword, nameConfigFile :str) -> None:

    maFiles = len(FileParsed.files)
    FileParsed = reloadConfig(FileParsed, maFiles)

    if maFiles == 1:
        maFiles = str(maFiles) + " file"
    else:
        maFiles = str(maFiles) + " files"

    try:
        while True:
        
            clearScr()
    
            exitCode = os.system(FileParsed.command)

            if exitCode == 0:
                print(f"\r\33[92mAll good \33[97m({maFiles}, at {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second})", end='')
            else:
                print(f"\r\33[91mSomething went wrong\33[97m (error code {exitCode}, {maFiles}, at {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second})", end='')


            findChanges = False
            while findChanges != True:
                
                for i in range(0, len(FileParsed.files) - 1):

                    try: 
                        modificationTime = time.ctime(os.stat(FileParsed.files[i])[stat.ST_MTIME])
                    except FileNotFoundError:
                        continue
                    
                    if modificationTime != FileParsed.modificationTime[i]:
                        FileParsed.modificationTime[i] = modificationTime
                        if FileParsed.files[i] == nameConfigFile:

                            FileParsed = parserConfig(nameConfigFile)

                            maFiles = len(FileParsed.files)
                            FileParsed = reloadConfig(FileParsed, maFiles)

                            if maFiles == 1:
                                maFiles = str(maFiles) + " file"
                            else:
                                maFiles = str(maFiles) + " files"

                        findChanges = True
                
                try:
                    time.sleep(FileParsed.time)
                except KeyboardInterrupt:
                    print("\r   \r", end='') # remove ^C in output
                    sys.exit(0)

    except KeyboardInterrupt:
        print("\r   \r", end='') # remove ^C in output
        sys.exit(0)