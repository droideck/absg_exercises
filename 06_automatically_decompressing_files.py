#!/usr/bin/python
# Given a list of filenames as input, this script queries each target file (parsing the output of the file command)
#+for the type of compression used on it. Then the script automatically invokes the appropriate decompression command
#+(gunzip, bunzip2, unzip, or whatever). If a target file is not compressed,
#+the script emits a warning message, but takes no other action on that particular file.
#
# Usage: list_of_files(ls command, for example) | ./06_automatically_decompressing_files.py

import sys
import os
import subprocess
import tarfile
import zipfile


def archive_processor(archive_file):
    uncompressed = False

    if not os.path.isfile(archive_file):
        print archive_file + " is not a regular file."
        return

    file_info = subprocess.check_output(["file", archive_file])

    if file_info.find("gzip") >= 0:
        tar_type = "gz"
        uncompressed = True

    if file_info.find("bzip2") >= 0:
        tar_type = "bz2"
        uncompressed = True

    if uncompressed:
        cf = tarfile.open(archive_file, 'r:' + tar_type)
        cf.extractall()
        cf.close()

    if file_info.find("Zip") >= 0:
        with zipfile.ZipFile(archive_file, 'r') as cf:
            cf.extractall()
            uncompressed = True

    if uncompressed is False:
        print "File " + archive_file + " is not an archive."
    else:
        print "File " + archive_file + " was decompressed in the current directory."


if __name__ == '__main__':
    for fname in sys.stdin.readlines():
        archive_processor(fname[:-1])