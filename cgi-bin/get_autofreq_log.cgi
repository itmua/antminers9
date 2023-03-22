#!/bin/sh
printf "Status: 200\r\n\r\n"

if [ -e /config/autolog ];then
	sed '1!G;h;$!d' /config/autolog
else
	echo "Create new log" > /config/autolog;
fi
