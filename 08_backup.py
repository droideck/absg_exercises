#!/usr/bin/python
# Archive as a "tarball" (*.tar.gz file) all the files in your home directory tree (/home/your-name)
#+that have been modified in the last 24 hours.

# Python and Bash tar result sizes differ with each other in ~0.1% only.

import tarfile
import os
import subprocess
import datetime as dt

day_ago = dt.datetime.now() - dt.timedelta(days=1)

tf = tarfile.open('home.tar.gz', 'w:gz')

# By this we get current user home directory.
home_dir = subprocess.check_output('echo ~', shell=True)[:-1]
os.chdir(home_dir)

for root, dirs, files in os.walk(home_dir):
    for fname in files:
        try:
            fpath = os.path.join(root, fname)
            st = os.stat(fpath)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > day_ago:
                tf.add(fpath)
        except OSError:
            # Here we have "No such file" exceptions. Mostly, it is broken symlinks. So we don't need them.
            continue
tf.close()