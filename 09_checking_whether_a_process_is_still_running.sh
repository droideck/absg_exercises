#!/bin/bash
# Given a process ID (PID) as an argument, this script will check,
#+at user-specified intervals, whether the given process is still running.

# You can interupt script by pushing CTRL-C

param_regexp="^[0-9]+$"
pid=$1
timeout=${2:-"4"} # Default value is 4 seconds
ERR_WRONG_ARGS=65

if ! [[ $pid =~ $param_regexp ]] || ! [[ $timeout =~ $param_regexp ]]
then
    echo "Usage: $(basename $0) PID [TIMEOUT]"
    exit $ERR_WRONG_ARGS
fi

while true
do
    # "ps -eo pid" command produces output of every process, but PID only
    if $(ps -eo pid | egrep " $pid$" &> /dev/null)
    then
        echo "Process $pid is running..."
    else
        echo "Can't find a process with $pid PID"
    fi
    sleep $timeout
done
