#!/bin/bash
# Print (to stdout) all prime numbers between 60000 and 63000. The output should be nicely formatted in columns.

print_prime_numbers()
{
local START_NUM=$1
local END_NUM=$2
local count=1

while [[ $START_NUM -le $END_NUM ]]
do
    number=$START_NUM
    prime=true
    i=2

    # We don't need go through every number. SQRT of $number is enough.
    #+(For Bash, I made some modifications by changing SQRT of "$number" to square number of $i.
    #+So now there is no need for external function)
    while [[ $(( i * i )) -lt $(( number - 1 )) ]]
    do
        if [[ $(( number % i )) -eq 0 ]]
        then
            prime=false
            break
        fi
        let i++
    done

    if [[ "$prime" = true ]]
    then
        printf "%d " $number
        let count++
    fi

    [[ $count -eq 13 ]] && count=1 && echo

    let START_NUM++
done
}

print_prime_numbers 60000 63000
