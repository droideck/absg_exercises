#!/bin/bash
# Write a script that echoes itself to stdout, but backwards.

# rev - for reverse characters in line
# tac - for reverse line order
cat $0 | rev | tac

exit 0
