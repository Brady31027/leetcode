#!/bin/bash

# Read from the file file.txt and output the tenth line to stdout.

filename='file.txt'
cnt=1
exec < $filename
while read line; do
    if [ $cnt == 10 ]; then
        echo $line
    fi
    let "cnt++"
done
