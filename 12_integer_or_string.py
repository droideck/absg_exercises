#!/usr/bin/python
# Write a script function that determines if an argument passed to it is an integer or a string.
#+The function will return TRUE (0) if passed an integer, and FALSE (1) if passed a string.

import re


def is_int_or_str(value):
    ''' Check if "value" variable contains
    only int digits or it is just string '''

    TRUE = 0
    FALSE = 1
    int_regexp = '^[0-9]+$'

    if re.match(int_regexp, value):
        return TRUE
    if value.isalpha():
        return FALSE


if __name__ == '__main__':
    chk = is_int_or_str("12")
    chk = is_int_or_str("Simple_string")

    if chk == 0:
        print "We pass an integer to the function and result is 0"
    else:
        print "We pass a string to the function and result is 1"