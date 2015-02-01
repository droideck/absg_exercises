#!/usr/bin/python
# Convert the for loops in Example 11-1 to while loops.
# Having already done the "heavy lifting," now convert the loops in the example to until loops.

planets = ("Mercury", "Venus", "Earth", "Mars", "Jupitor", "Saturn", "Uranus", "Neptu", "Pluton")


# For this exercise I made decision to encapsulate part of my script into a function.
def print_array_with_loops(array):
    for element in array:
        print element

    print
    i = 0

    while i < len(array):
        print array[i]
        i += 1


if __name__ == '__main__':
    print_array_with_loops(planets)
