import sys
import os
import shutil


def installpkg(path):

    # use installer for .pkg files
    # hey, /dev/null isn't great, but it keeps it quiet
    os.system("sudo installer -pkg " + path + " -target / >> /dev/null")


def findpkg(dir):

    # need to check if the directory contains a .pkg file
    for fname in os.listdir(dir):
        if fname.endswith('.pkg'):
            installpkg(dir + "/" + fname)
            return True
        else:
            return False


def findapp(dir):

    # need to check if the directory contains a .app file
    for fname in os.list(dir):
        if fname.endswith('.app')
            return dir + "/" + fname


def installer(dir, *cmd):

    # if there is not .pkg in the directory
    # install from a different method
    if findpkg(dir) == False:

        # if no command is designated in the json
        if cmd == null:

            # copy the .app to the applications folder
            shutil.copy(findapp(dir), "/Applications")
        else

        # execute the custom command from the json
            os.system(findapp(dir) + cmd)
