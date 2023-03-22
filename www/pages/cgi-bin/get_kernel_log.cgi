#!/bin/sh
printf "Status: 200\r\n\r\n"
if [ -e /tmp/search ];then
	cat /tmp/search
fi

if [ -e /tmp/freq ];then
	cat /tmp/freq
fi

if [ -e /tmp/lasttemp ];then
	cat /tmp/lasttemp
fi
