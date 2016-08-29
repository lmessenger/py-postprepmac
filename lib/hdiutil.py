import os
from fmgr import makedir, removedir, checkdirexists


def diskmounter(fpath, mountpoint, fullname):

    # let's build the mountpoint
    makedir(mountpoint)

    # the reason for -mountpoint allows us to force the directory to mount to
    # a specific location we own
    os.system("hdiutil attach -mountpoint " +
              mountpoint + " " + fpath + " -nobrowse -quiet")
    print(fullname + " mounted.")


def diskunmounter(mountpoint, fullname):

    if checkdirexists(mountpoint) == True:

        # it's a good thing we know the mountpoint
        os.system("hdiutil detach " + mountpoint + " -quiet")

        removedir(mountpoint)

        print(fullname + " unmounted.")
    else:
        print(mountpoint + " not found.")
