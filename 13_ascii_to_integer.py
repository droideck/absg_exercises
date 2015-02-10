#!/usr/bin/python
# The atoi function in C converts a string character to an integer.
#+Write a shell script function that performs the same operation.
#+Likewise, write a shell script function that does the inverse,
#+mirroring the C itoa function which converts an integer into an ASCII character.

import re


# Use a little modified version of exercise 12 function
def is_int(value):
    ''' Check if "value" variable contains
    only int digits or it is just string '''

    int_regexp = '^[0-9]+$'

    if not isinstance(value, basestring):
        return False

    if re.match(int_regexp, value):
        return True
    else:
        return False


def atoi(string):
    num_pattern = re.compile('^[0-9]+')
    if re.match(num_pattern, string):
        return int(re.findall(num_pattern, string)[0])
    else:
        return 0


def itoa(int_num, base=10):
    if is_int(int_num):
        return "This is not integer"

    if base not in (2, 8, 10, 16):
        return "Wrong base format"

    if base == 2:
        return bin(int_num)[2:]

    if base == 8:
        return oct(int_num)[1:]

    if base == 10:
        return int(int_num)

    if base == 16:
        return hex(int_num)[2:]


if __name__ == '__main__':
    number = atoi("0123.2d1sd23d")
    print number            # return 123
    print itoa(number, 2)   # return 1111011
    print itoa(number, 8)   # return 173
    print itoa(number, 10)  # return 123
    print itoa(number, 16)  # return 7b
