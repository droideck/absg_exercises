#!/bin/bash
# List, one at a time, all files larger than 100K in the /home/username directory tree.
#+Give the user the option to delete or compress the file, then proceed to show the next one.
#+Write to a logfile the names of all deleted files and the deletion times.

# Seting up system variables withing our subprocess
PS3="Make a choice: "
OIFS=$IFS
IFS='
'

for fname in $(find ~ -size +100k 2> /dev/null)
do
    echo "Please, select what do you want to do with file ${fname}?"
    select answer in "Compress" "Remove" "Nothing"
    do
        case $answer in
            "Compress") tar czvf "$(basename $fname).tar.gz" "$fname" ;;
            "Remove") rm -rf "$fname" && echo -e "$(date)\n$fname" >> delfiles.log ;;
            "Nothing") break ;;
        esac
    break
    done
done

exit 0
