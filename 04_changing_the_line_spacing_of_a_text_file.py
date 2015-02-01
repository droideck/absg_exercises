#!/usr/bin/python
# Write a script that reads each line of a target file, then writes the line back to stdout,
#+but with an extra blank line following. This has the effect of double-spacing the file.
#
# Include all necessary code to check whether the script gets the necessary command-line argument (a filename),
#+and whether the specified file exists.
#
# When the script runs correctly, modify it to triple-space the target file.
# Finally, write a script to remove all blank lines from the target file, single-spacing it.

import sys
import os

err_wrong_args = 65

if len(sys.argv) == 1 or not os.path.isfile(sys.argv[1]):
    print "Usage: " + os.path.basename(sys.argv[0]) + " file"
    sys.exit(err_wrong_args)

text_file = sys.argv[1]
fl = open(text_file)

for line in fl.readlines():
    if len(line) > 1:
        print line,
# For now, script remove all blank lines from file.
# For double-spacing: uncomment two lines below.
# For triple-spacing: uncomment three lines below.
#       print
#       print
#       print
