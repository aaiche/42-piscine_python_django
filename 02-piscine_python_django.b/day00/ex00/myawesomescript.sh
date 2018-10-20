#!/bin/sh

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 http://bit.ly/xxxxx" >&2
  exit 1
fi
#works as well
#curl -s $1 | grep "body" | cut -d'"' -f2- | cut -d'"' -f1

# - I ==> http command HEAD 
curl -I -s $1 | grep "Location:" | cut -d' ' -f2

#rep=$(curl -s $1 | grep "body" | cut -d'"' -f2- | cut -d'"' -f1)
#status=$?
#echo "rep"
#echo "$rep"
#echo "status"
#echo $status

