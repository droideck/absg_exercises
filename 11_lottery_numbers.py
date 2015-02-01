#!/usr/bin/python
# One type of lottery involves picking five different numbers, in the range of 1 - 50.
#+Write a script that generates five pseudorandom numbers in this range, with no duplicates.
#+The script will give the option of echoing the numbers to stdout or saving them to a file,
#+along with the date and time the particular number set was generated.

import random
import re
import sys
from datetime import datetime

today = datetime.now()
random_list = random.sample(xrange(1, 50), 5)

# Unix file can have any symbol in their paths, except "\0"(null symbol).
file_regexp = '^[^\0]+$'

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""

# Date format is in the UNIX-style
if re.search(file_regexp, file_name):
    with open(file_name, 'a') as fl:
        fl.write("\n" + today.strftime("%a %b %d %H:%M:%S %Z %Y") + "\n" + " ".join(map(str, random_list)) + "\n")
else:
    print today.strftime("%a %b %d %H:%M:%S %Z %Y") + "\n" + " ".join(map(str, random_list))

