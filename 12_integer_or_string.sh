#!/bin/bash
# Write a script function that determines if an argument passed to it is an integer or a string.
#+The function will return TRUE (0) if passed an integer, and FALSE (1) if passed a string.

is_int_or_str()
{
    TRUE=0
    FALSE=1
    expr $1 + 0 &> /dev/null
    if (( $? == 0 ))
    then
        return $TRUE
    else
        return $FALSE
    fi
}

is_int_or_str 2
echo "We pass an integer to the function and result is $?"

is_int_or_str some_string
echo "We pass a string to the function and result is $?"
