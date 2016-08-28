import requests
import os
import sys
import time


def downloader(url, fdir, filename):

    with open(fdir + filename, "wb") as f:
        r = requests.get(url, timeout=20, stream=True)
        start = time.clock()

        # filesize in MB
        filesize = int(int(r.headers['Content-Length'].strip()) / 1000000)
        fpath = os.path.realpath(fdir + filename)

        # write data out to file and show progress bar
        for data in r.iter_content(1024):
            f.write(data)
            currentsize = int(os.path.getsize(fpath) / 1000000)

            # determine the percentage of the way completed
            prog = (float(currentsize) / float(filesize)) * 50

            # determine how much data has been stored per second (Mbps)
            prog_time = "{0:.2f}".format(
                float(currentsize / (time.clock() - start) / 8), 2)
            sys.stdout.write("\r[%s%s] %s/%sMB (%s Mbps)" % ('=' * int(prog),
                                                             ' ' * int(50 - int(prog)), currentsize, filesize, prog_time))
            sys.stdout.flush()

        # print new line so next line doesn't get caught
        print ""
