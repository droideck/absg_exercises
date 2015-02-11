#!/bin/bash
# Inactive accounts on a network server waste disk space and may become a security risk.
#+Write an administrative script that checks for and deletes user accounts
#+that have not been accessed within the last 90 days.

ERR_NEED_ROOT=70

if (( $UID > 0 ))
then
    echo "Need to be root" && exit $ERR_NEED_ROOT
fi

for user in $(cat /etc/passwd | grep -v /bin/false | grep /home | awk 'BEGIN {FS=":"} {print $1}')
do
    # -s -90days - show lines since 90 days only
    # If there is no lines, then delete this account
    if (( $(last -s -90days $user | wc -l) == 2 ))
    then
        userdel $user
    fi
done

exit 0