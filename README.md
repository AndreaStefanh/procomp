# PROCOMP

Procomp is a [ghcid](https://github.com/ndmitchell/ghcid) clone but supports all programming languages

## How to use it

for procomp to work you need a configuration file called **.procomp.json**
```json5
{
    "files": ["main.c"], // Files that will be checked for changes
    "command": "gcc -Wall main.c -o main", // The command that should be run if a change is found to a file
    "time": 5, // (not mandatory) when it has to wait to check for file changes. default 0.5 seconds
    "silent": false // (not mandatory) if true it does not print on the screen any output of the commands executed in "command"
    // btw json doesn't support comments so you can't put comments in a real .procomp.json
}
```

## Compile

```sh
$ chmod +x makefile.py
$ ./makefile.py
```

## Credits
[ghcid](https://github.com/ndmitchell/ghcid)
