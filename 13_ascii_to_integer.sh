#!/bin/bash
# The atoi function in C converts a string character to an integer.
#+Write a shell script function that performs the same operation.
#+Likewise, write a shell script function that does the inverse,
#+mirroring the C itoa function which converts an integer into an ASCII character.


# Use function from exercise 12
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


atoi()
{
return_num=$(expr match "$1" '\(^[0-9]\+\)')
if [[ -z $return_num ]]
then
    return_num=0
else
    # Removing leading zeros
    return_num=$(expr $return_num + 0)
fi
}


itoa()
{
err_wrong_args=65

is_int_or_str $1 || return $err_wrong_args
num=$1
base=${2:-10}
is_int_or_str $2 || return $err_wrong_args

return_ascii=$(echo "obase=$base; $num" | bc)
}

#                           main
#=============================================================#
atoi 0123.2d1sd23d
echo $return_num   # return 123

itoa $return_num 2
echo $return_ascii # return 1111011

itoa $return_num 8
echo $return_ascii # return 173

itoa $return_num 10
echo $return_ascii # return 123

itoa $return_num 16
echo $return_ascii # return 7B
#=============================================================#
