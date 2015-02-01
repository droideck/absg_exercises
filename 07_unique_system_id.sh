#!/bin/bash
# Generate a "unique" 6-digit hexadecimal identifier for your computer. Do not use the flawed hostid command.

passwd_sum=$(md5sum /etc/passwd)

echo ${passwd_sum::6}

exit 0
