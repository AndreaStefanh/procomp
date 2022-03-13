import os
import sys
import time
import stat
import datetime

from parserConfig import *
from threading import Event


def clearScr() -> None:

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def compileExec(FileParsed :FileKeyword) -> None:

    for file in FileParsed.files:
        FileParsed.modificationTime.append(time.ctime(os.stat(file)[stat.ST_MTIME]))

    maFiles = len(FileParsed.files)
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
                
                for i in range(0, len(FileParsed.files)):

                    try: 
                        modificationTime = time.ctime(os.stat(FileParsed.files[i])[stat.ST_MTIME])
                    except FileNotFoundError:
                        continue
                    
                    if modificationTime != FileParsed.modificationTime[i]:
                        FileParsed.modificationTime[i] = modificationTime
                        findChanges = True
                
                if FileParsed.calledTime == True:
                    if FileParsed.time > 0:
                        
                        try:
                            time.sleep(FileParsed.time)
                        except KeyboardInterrupt:
                            print("\r   \r", end='') # remove ^C in output
                            sys.exit(0)
                        
                    else:
                        print("ERROR: you cannot pause with a number less than 0")
                        sys.exit(-1)
                else:

                    try:
                        time.sleep(0.5)
                    except KeyboardInterrupt:
                        print("\r   \r", end='') # remove ^C in output
                        sys.exit(0)

    except KeyboardInterrupt:
        print("\r   \r", end='') # remove ^C in output
        sys.exit(0)