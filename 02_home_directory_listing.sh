#!/bin/bash
# Perform a recursive directory listing on the user's home directory and save the information to a file.
#+Compress the file, have the script prompt the user to insert a USB flash drive, then press ENTER.

TEMPFILE=/tmp/home_content

ls -R ~ > $TEMPFILE
cd /tmp

tar cfz $(basename ${TEMPFILE}).tar.gz $(basename $TEMPFILE) > /dev/null

echo "Please, insert FlashDisk and push ENTER."
read enter

# There is can be your mount point for FlashDisks.
#+But for now we would work with previous working directory.
cd -

cp ${TEMPFILE}.tar.gz ./

exit 0
