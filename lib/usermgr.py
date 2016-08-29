import os


def checkuid():

    # if we check if we are root now, then we don't have to worry about using
    # sudo on shell commands
    if os.getuid() == 0:
        # root is active, yo!
        return True

    else:
        print("Script is not running as root. Please launch as root.")
        return False
