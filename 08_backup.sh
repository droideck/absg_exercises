#!/bin/bash
# Archive as a "tarball" (*.tar.gz file) all the files in your home directory tree (/home/your-name)
#+that have been modified in the last 24 hours.

# Python and Bash tar result sizes differ with each other in 0.1% only.

find ~ -mtime -1 -type f -print0 | tar cvfz home.tar.gz --null -T - > /dev/null

exit 0
