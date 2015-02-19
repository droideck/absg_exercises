#!/bin/bash
# Simulate the functionality of the deprecated banner command in a script.
#+Prints arguments as a large vertical banner to stdout, using an ASCII character (default '#').


setup_dict()
{
#######################################################
#                     Dictionary                      #
#######################################################
    D1="        "; Z1="        "
    D2=" #####  "; Z2=" ###### "
    D3=" #    # "; Z3="     #  "
    D4=" #    # "; Z4="    #   "
    D5=" #    # "; Z5="   #    "
    D6=" #    # "; Z6="  #     "
    D7=" #####  "; Z7=" ###### "
    D8="        "; Z8="        "
    R1="        "; E1="        "
    R2=" #####  "; E2=" ###### "
    R3=" #    # "; E3=" #      "
    R4=" #    # "; E4=" #####  "
    R5=" #####  "; E5=" #      "
    R6=" #   #  "; E6=" #      "
    R7=" #    # "; E7=" ###### "
    R8="        "; E8="        "
    O1="        "; K1="        "
    O2="  ####  "; K2=" #    # "
    O3=" #    # "; K3=" #   #  "
    O4=" #    # "; K4=" ####   "
    O5=" #    # "; K5=" #  #   "
    O6=" #    # "; K6=" #   #  "
    O7="  ####  "; K7=" #    # "
    O8="        "; K8="        "
}


draw_word()
{
    setup_dict
    for i in $(seq 1 8)
    do
        count=0
        # \U for upper AND \n for new line
        for char in $(echo "$1" | sed -e "s/\(.\)/\U\1\n/g")
        do
            let count++
            eval "echo -ne \"\$$char$i\""
            (( count == 10 )) && break
        done
        echo
    done
}


# Main()
draw_word "ok"
draw_word "drozDeK"

exit 0