#!/usr/bin/python
# Write a script that echoes itself to stdout, but backwards.

import sys

# We set slicing parameters like this: BEGIN and END for None, STEP for -1.as
#+So we have reverse order of string
print "".join(open(sys.argv[0]).readlines())[::-1]

print "\n-------------------------------------------------------"
print "-------------------------------------------------------\n"

# Or if you want just reversed string order:
print "".join(reversed(list(open(sys.argv[0]).readlines())))
