#!/usr/bin/python
# Print (to stdout) all prime numbers between 60000 and 63000. The output should be nicely formatted in columns.

# Python realization is much more faster then Bash realization.

import math


def print_prime_numbers(start_number, end_number):
    count = 1
    for num in range(start_number, end_number):
        # We don't need go through every number. SQRT of "num" is enough.
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            print '%d ' % num,
            count += 1
        if count == 13:
            print
            count = 1


if __name__ == '__main__':
    print_prime_numbers(60000, 63000)