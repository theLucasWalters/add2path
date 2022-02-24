# add2path program
# This program will allow you to add any directory to your Windows path with a single command

# imports
import os
import sys

# variable for sys.argv
sysargs = sys.argv
# variable for os.system
osys = os.system

# main
def main() -> None:
    if len(sysargs) <= 2:
        getpath()

    elif len(sysargs) > 2:
        # placeholder to handle tags down the line
        print(sysargs)

    else:
        # if there's an error, for some reason
        raise Exception(f"Command error: {sysargs}")

# get the path
def getpath() -> None:
    """Gets the string to be added to the path"""

    # get the path
    try:
        dir_string = str(sysargs[1])

    except:
        # if there's no sys.argv[1], the help/usage will be displayed
        print(help())
        quit()

    addpath(dir_string)

# add to the path
def addpath(path) -> None:
    """At the moment, this function just lists the dir of the path"""

    # build the command
    cmd = f'dir "{path}"'
    # run the command
    osys(cmd)

# help/usage
def help() -> str:
    """Returns the program usage

        Displays as:

            Usage:
                python main.py "C:/path/to/target/directory"
    """

    return "\nUsage:\n\tpython main.py \"C:/path/to/target/directory\"\n"

# run main
if __name__ == "__main__":
    main()
