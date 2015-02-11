#!/bin/bash
# Given a list of filenames as input, this script queries each target file (parsing the output of the file command)
#+for the type of compression used on it. Then the script automatically invokes the appropriate decompression command
#+(gunzip, bunzip2, unzip, or whatever). If a target file is not compressed,
#+the script emits a warning message, but takes no other action on that particular file.
#
# Usage: list_of_files(ls command, for example) | ./06_automatically_decompressing_files.sh


uncompres()
{
    echo $fileinfo | grep "gzip" > /dev/null && tar xvfz $1 &> /dev/null && uncompressed=true && return 0
    echo $fileinfo | grep "bzip2" > /dev/null && tar xvfj $1 &> /dev/null && uncompressed=true && return 0
    echo $fileinfo | grep "Zip" > /dev/null && unzip -o $1 &> /dev/null && uncompressed=true && return 0
}


while read fname
do
    [[ ! -f $fname ]] && echo "$fname is not a regular file." && continue
    fileinfo=$(file $fname)

    uncompressed=false

    uncompres $fname

    if [[ $uncompressed = false ]]
    then
        echo "File $fname is not an archive."
    else
        echo "File $fname was decompressed in the current directory."
    fi
done

exit 0