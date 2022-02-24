# add2path program
# This program will allow you to add any directory to your Windows path with a single command

# imports
import os
import sys

# main
def main() -> None:
    # get the path
    try:
        dir_string = str(sys.argv[1])
    except:
        print(help())
        quit()

    run(dir_string)

# run
def run(path) -> None:
    """At the moment, this function just lists the dir of the path"""

    cmd = f'cmd /c "dir \"{path}"'

    os.system(cmd)

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
