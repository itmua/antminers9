#!/bin/sh
#set -x
action=
port=

DROPBEAR_PORT=`sed -n '/^DROPBEAR_PORT=/{s/^DROPBEAR_PORT=//;p}' /config/dropbear`
NO_START=`sed -n '/^NO_START=/{s/^NO_START=//;p}' /config/dropbear`

if [ -z $NO_START ]; then
	NO_START=1
fi

if [ -z $DROPBEAR_PORT ]; then
	DROPBEAR_PORT=22
fi


ant_input=`cat /dev/stdin`

ant_tmp=${ant_input//&/ }
i=0
for ant_var in ${ant_tmp}
do
	ant_var=${ant_var//+/ }
	ant_var=${ant_var//%23/#}
	ant_var=${ant_var//%24/$}
	ant_var=${ant_var//%25/%}
	ant_var=${ant_var//%26/&}
	ant_var=${ant_var//%2C/,}
	ant_var=${ant_var//%2B/+}
	ant_var=${ant_var//%3A/:}
	ant_var=${ant_var//%3B/;}
	ant_var=${ant_var//%3C/<}
	ant_var=${ant_var//%3D/=}
	ant_var=${ant_var//%3E/>}
	ant_var=${ant_var//%3F/?}
	ant_var=${ant_var//%40/@}
	ant_var=${ant_var//%5B/[}
	ant_var=${ant_var//%5D/]}
	ant_var=${ant_var//%5E/^}
	ant_var=${ant_var//%7B/\{}
	ant_var=${ant_var//%7C/|}
	ant_var=${ant_var//%7D/\}}
	ant_var=${ant_var//%2F/\/}
	#ant_var=${ant_var//%22/\"}
	#ant_var=${ant_var//%5C/\\}
	case ${i} in
		0 )
		action=${ant_var/action=/}
		;;
		1 )
		status=${ant_var/status=/}
		;;
		2 )
		port=${ant_var/port=/}
		;;

		esac
	i=`expr $i + 1`
done
if [ "${action}" == "0" ]; then

echo {
echo \"disabled\" : \"$NO_START\",
echo \"port\" : \"$DROPBEAR_PORT\"
echo }

fi


if [ "${action}" == "1" ]; then
if [ "${status}" == "1" ]; then
test -x /usr/sbin/beardrop && /etc/init.d/beardrop stop >/dev/null 2>&1
killall beardrop >/dev/null 2>&1
echo "Stop SSH"
fi

[ ! -z "${port##*[!0-9]*}" ] || port=22;
[ ! -z "${status##*[!0-9]*}" ] || status=1;

echo "NO_START=${status}" > /config/dropbear
echo "DROPBEAR_PORT=${port}" >> /config/dropbear

cp /config/dropbear /etc/default/dropbear
if [ "${status}" == "0" ]; then
test -x /usr/sbin/beardrop && /etc/init.d/beardrop force-reload >/dev/null 2>&1 || /etc/init.d/beardrop start >/dev/null 2>&1
echo "Start SSH"

fi


fi

sync &

