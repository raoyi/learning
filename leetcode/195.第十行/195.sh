#!/bin/bash
# Read from the file file.txt and output the tenth line to stdout.
lineno=`cat file.txt | wc -l`
if [ "$lineno" -lt "10" ];then
  echo "Line 10 not exist!"
else
  echo `sed -n 10p file.txt`
fi