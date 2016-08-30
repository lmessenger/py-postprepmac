import os
import glob
from fmgr import copy



def installpkg(path):

    # use installer for .pkg files
    # hey, /dev/null isn't great, but it keeps it quiet
    os.system("sudo installer -pkg " + path + " -target / >> /dev/null")


def findpkg(dir):

    # need to check if the directory contains a .pkg file
    fname = glob.glob(dir + "/*.pkg")

    # if found only one pkg, then go install it
    if len(fname) == 1:
        installpkg(fname[0])
        return True

    # I'm not sure how frequently this might happen, but might as well write a case for it
    elif len(fname) > 1:
        print("ERROR: " + dir +
              " contains more than one installable package. Please install manually:")
        for f in fname:
            print(f)
            return True

    # if you fail and life miserably, and there is no installable package, return False
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
