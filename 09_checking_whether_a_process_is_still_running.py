#!/usr/bin/python
# Given a process ID (PID) as an argument, this script will check,
#+at user-specified intervals, whether the given process is still running.

# You can interupt script by pushing CTRL-C

import subprocess
import sys
import time
import re

founded = False
err_wrong_args = 65
pid = ""
timeout = "4"
if len(sys.argv) == 2:
    pid = sys.argv[1]
elif len(sys.argv) == 3:
    pid = sys.argv[1]
    timeout = sys.argv[2]

if not pid.isdigit() or not timeout.isdigit():
    print "Usage: " + sys.argv[0] + " PID [TIMEOUT]"
    sys.exit(err_wrong_args)

re_pattern = '[ ]*' + pid + '$'
pid_search = re.compile(re_pattern)

while True:
    # "ps -eo pid" command produces output of every process, but PID only
    search_result = subprocess.check_output(["ps", "-eo", "pid"])

    for line in search_result.split("\n"):
        if pid_search.match(line):
            print "Process " + pid + " is running..."
            founded = True
            break

    if not founded:
        print "Can't find a process with " + pid + " PID"

    time.sleep(float(timeout))
