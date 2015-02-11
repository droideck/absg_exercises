#!/usr/bin/python
# Inactive accounts on a network server waste disk space and may become a security risk.
#+Write an administrative script that checks for and deletes user accounts
#+that have not been accessed within the last 90 days.

import os
import sys
import subprocess

err_need_root = 70

if os.geteuid() != 0:
    sys.exit(err_need_root)

user_list = subprocess.check_output("cat /etc/passwd | grep -v /bin/false | grep /home |\
                                    awk 'BEGIN {FS=\":\"} {print $1}'", shell=True)

for user in user_list.split():
    # -s -90days - show lines since 90 days only
    # If there is no lines, then delete this account
    last_login = subprocess.check_output(["last", "-s", "-90days", user])
    if last_login.count(user) == 0:
        user_del = subprocess.call(["userdel", user])