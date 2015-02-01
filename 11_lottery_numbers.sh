#!/bin/bash
# One type of lottery involves picking five different numbers, in the range of 1 - 50.
#+Write a script that generates five pseudorandom numbers in this range, with no duplicates.
#+The script will give the option of echoing the numbers to stdout or saving them to a file,
#+along with the date and time the particular number set was generated.

ERR_WRONG_ARGS=65

gen_number()
{
local num_regexp='^[0-9]+$'

if ! [[ $1 =~ $num_regexp ]] || ! [[ $2 =~ $num_regexp ]]
then
    echo "Usage: $(basename $0) start_number end_number."
    return $ERR_WRONG_ARGS
fi

return_num=0

while (( $return_num < $1 ))
do
    return_num=$(( $RANDOM % $2 ))
done
}

count=0

while [[ $count < 5 ]]
do
    # Setting seed for RANDOM
    RANDOM=$(( $$ + $count ))
    gen_number 1 50
    if ! echo $result | grep -w $return_num > /dev/null
    then
        result=$result" "$return_num
        let count++
    fi
done

# UNIX file can have any symbol in their paths, except "\0"(null symbol)
file_regexp="^[^\0]+$"
if [[ $1 =~ $file_regexp ]]
then
    {
    echo
    date
    echo $result
    } >> $1
else
    date
    echo $result
fi

exit 0
