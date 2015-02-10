#!/usr/bin/python
# List, one at a time, all files larger than 100K in the /home/username directory tree.
#+Give the user the option to delete or compress the file, then proceed to show the next one.
#+Write to a logfile the names of all deleted files and the deletion times.

import subprocess
import os
import tarfile
from datetime import datetime


# You can set any directory here. (even Win dir, script is cross-platform)
home_dir = subprocess.check_output('echo ~', shell=True)[:-1]

for root, dirs, files in os.walk(home_dir):
    for fname in files:
        try:
            fpath = os.path.join(root, fname)
            st = os.stat(fpath)
            fsize = st.st_size.real
            if fsize > 100*1024:
                print "Please, select what do you want to do with file " + fpath + "?"
                print "1) Compress\n2) Remove\n3) Nothing"
                answer = input("Make a choice: ")

                if answer == 1:  # Compress
                    with tarfile.open(fname+".tar.gz", "w:gz") as tf:
                        tf.add(fpath)

                if answer == 2:  # Remove
                    os.remove(fpath)
                    today = datetime.now()
                    with open("delfiles.log", "a") as df:
                        df.write("\n" + today.strftime("%a %b %d %H:%M:%S %Z %Y") + "\n" + fpath + "\n")

                if answer == 3:  # Nothing
                    continue
        except OSError:
            continue
