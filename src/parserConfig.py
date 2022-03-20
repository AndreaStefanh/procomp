import json
import sys
import os

class FileKeyword:

    files = list()
    pushedFiles = bool()
    modificationTime = list()

    command = str()
    pushedCommand = bool()

    time = float()
    calledTime = bool()

    silent = bool()
    calledSilent = bool()


    def __init__(self) -> None:
        self.pushedFiles = False
        self.pushedCommand = False
        self.calledTime = False
        self.calledSilent = False

        self.silent = False
        pass

    def push(self, element :str, value) -> None:

        try:
            if element == "files":
                if self.pushedFiles == False:

                    for f in value:
                        if os.path.exists(f) == False:
                            print(f"ERROR: Unable to open: '{f}'")
                            sys.exit(1)
                        
                        if os.path.isfile(f) == False:
                            print(f"ERROR: '{f}' is not a file")
                            sys.exit(1)

                    self.pushedFiles = True
                    self.files = value
                else:
                    print(f"ERROR: '{element}' arredy exist")
                    sys.exit(1)
            
            elif element == "command":
                if self.pushedCommand == False:
                    self.pushedCommand = True
                    self.command = str(value)
                else:
                    print(f"ERROR: '{element}' arredy exist")
                    sys.exit(1)

            elif element == "time":
                if self.calledTime == False:
                    self.calledTime = True
                    self.time = float(value)
                else:
                    print(f"ERROR: '{element}' arredy exist")
                    sys.exit(1)
            
            elif element == "silent":
                if self.calledSilent == False:
                    self.calledSilent = True
                    self.silent = bool(value)
                else:
                    print(f"ERROR: '{element}' arredy exist")
                    sys.exit(1)
            
            else:
                print(f"ERROR: no such keyword: '{element}' in the configuration file")
                sys.exit(1)

        except ValueError:
            print(f"ERROR: unable to use '{value}' in '{element}'")
            sys.exit(1)
    

def parserConfig(path :str) -> FileKeyword:

    data = None

    with open(path, "r") as f:
        data = json.load(f)

    data = list(data.items())
    
    returnFileKeyword = FileKeyword()

    for i in range(0, len(data)):
        returnFileKeyword.push(data[i][0], data[i][1])

    return returnFileKeyword