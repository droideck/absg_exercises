#!/bin/bash
# Write a script that reads each line of a target file, then writes the line back to stdout,
#+but with an extra blank line following. This has the effect of double-spacing the file.
#
# Include all necessary code to check whether the script gets the necessary command-line argument (a filename),
#+and whether the specified file exists.
#
# When the script runs correctly, modify it to triple-space the target file.
# Finally, write a script to remove all blank lines from the target file, single-spacing it.

ERR_WRONG_ARGS=65

[[ ! -f $1 ]] && echo "Usage: $(basename $0) FILE" && exit $ERR_WRONG_ARGS

while read line
do
    if [[ -n $line ]]
    then
        echo $line
# For now, script remove all blank lines from file.
# For double-spacing: uncomment two lines below.
# For triple-spacing: uncomment three lines below.
#       echo
#       echo
#       echo
    fi
done < $1

exit 0