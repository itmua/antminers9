#!/bin/sh

[ -f /config/autofreq.conf ] || cp /etc/autofreq.conf.default /config/autofreq.conf
source /config/autofreq.conf

echo {

echo \"conf_enabled\":\"${enabled}\",
echo \"conf_min\":\"${min}\",
echo \"conf_step\":\"${step}\",
echo \"conf_timeas\":\"${timeas}\"

echo }
