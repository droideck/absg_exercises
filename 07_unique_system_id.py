#!/usr/bin/python
# Generate a "unique" 6-digit hexadecimal identifier for your computer. Do not use the flawed hostid command.

import random

print "".join([random.choice('0123456789abcdef') for i in range(0, 6)])
