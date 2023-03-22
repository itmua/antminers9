#!/bin/sh
#set -x
printf "Status: 200\r\n\r\n"

tz=`date +"%Z"`

echo -n ${tz//0}
