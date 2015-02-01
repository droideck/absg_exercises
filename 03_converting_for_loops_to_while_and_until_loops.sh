#!/bin/bash
# Convert the for loops in Example 11-1 to while loops.
# Having already done the "heavy lifting," now convert the loops in the example to until loops.

planets=(Mercury Venus Earth Mars Jupitor Saturn Uranus Neptu Pluton)
i=0

while (( i <= ${#planets} ))
do
    echo ${planets[$i]}
    let i+=1
done

echo
i=0

until (( i > ${#planets} ))
do
    echo ${planets[$i]}
    let i+=1
done

exit 0
