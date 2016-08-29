import os
from fmgr import copy



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
    for fname in os.listdir(dir):
        if fname.endswith('.app'):
            return fname


def installer(dir, cmd):

    # if there is not .pkg in the directory
    # install from a different method
    if findpkg(dir) == False:

        fname = findapp(dir)
        sdir = dir + "/" + fname

        print(cmd)

        # if no command is designated in the json
        if cmd == None:

            ddir = "/Applications/" + fname

            # copy the .app to the applications folder
            copy(sdir, ddir)
        else:

            # execute the custom command from the json
            os.system(sdir + cmd)
