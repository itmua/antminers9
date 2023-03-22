#!/bin/sh

printf "Status: 200\r\n\r\n"
iptables-save > /www/pages/firewall.txt

echo "OK"