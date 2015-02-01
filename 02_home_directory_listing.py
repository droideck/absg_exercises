#!/usr/bin/python
# Perform a recursive directory listing on the user's home directory and save the information to a file.
#+Compress the file, have the script prompt the user to insert a USB flash drive, then press ENTER.

import subprocess
import tarfile
import shutil

file_name = "/tmp/home_content"
with open(file_name, 'w') as home_content_file:
    sp = subprocess.Popen("ls -R ~", shell=True, universal_newlines=True, stdout=home_content_file)

user_completion = raw_input("Please, insert FlashDisk and push ENTER.\n")

archive_name = file_name + ".tar.gz"
with tarfile.open(archive_name, "w:gz") as tf:
    tf.addfile(tarfile.TarInfo(file_name.split("/")[-1]), file(file_name))

# There is can be your mount point for FlashDisks.
#+But for now we would work with previous working directory.
destination_dir = "/home/drozdek/"

shutil.copy(archive_name, destination_dir + archive_name.split("/")[-1])
