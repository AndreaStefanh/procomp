from parserArgs   import *
from parserConfig import *
from runForever   import *


def main():
    
    filePath = parserArgs()
    FileKeyword = parserConfig(filePath)
    compileExec(FileKeyword)


if __name__ == "__main__":
    main()