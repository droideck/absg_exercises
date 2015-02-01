#!/usr/bin/python
# Write a script that backs itself up, that is, copies itself to a file named backup.sh.

import sys

with open(sys.argv[0], 'r') as fl:
    with open('backup.py', 'w') as bu:
        bu.write(fl.read())
