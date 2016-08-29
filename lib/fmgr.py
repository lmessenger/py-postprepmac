import os
import shutil
import errno


def checkdirexists(dir):

    # check if the path exists
    if os.path.exists(dir) == True:

        # if true, check if the path is a directory
        if os.path.isdir(dir) == True:
            return True
        else:
            # path is not a directory, provide an error
            print("ERROR: " + dir + " already exists and is not a directory.")
            return True  # need to figure out a better returned value
    else:
        return False


def makedir(dir):

    # if the dir doesn't exist, built it
    if checkdirexists(dir) == False:
        os.mkdir(dir)


def removedir(dir):

    # if the directory exists, and it is a directory, remove it
    if checkdirexists(dir) == True:
        os.rmdir(dir)


def removefile(file):

    # remove file
    if os.path.exists(file) == True:
        os.remove(file)


def copy(src, dst):

    # let's try to copy the tree
    # if we get an exception, just copy reguarly
    try:
        shutil.rmtree(dst)
        shutil.copytree(src, dst)
    except OSError as exc:
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise
