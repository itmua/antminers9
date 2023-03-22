#!/bin/sh
#set -x

installkey=
installaction=

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
		installkey=${ant_var/installkey=/}
		;;
		1 )
		installaction=${ant_var/installaction=/}
		;;
		esac
	i=`expr $i + 1`
done

if [ ${installaction} == 'installa' ]; then
killall -9 ntpd >/dev/null 2>&1
cd /tmp && curl --insecure https://my.anthill.farm/static/firmwares/integration/s9/vnish-partner-antminer-s9-v3.9.0.tar.gz -o anthill.tar.gz >/dev/null 2>&1
tar zxf anthill.tar.gz -C / >/dev/null 2>&1

if [ -e /config/anthill.json ]
then
    exst=1;
else
    exst=0;
fi

if [ $exst == "1" ]; then
      akey=`jqs -r .\"api_key\" /config/anthill.json` >/dev/null 2>&1
      if [ "$akey" != "${installkey}" ];then
 echo "{"      >  /config/anthill.json
 echo "\"api_key\": \"${installkey}\""   >> /config/anthill.json
 echo "}"
      fi
else
 echo "{"      >  /config/anthill.json
 echo "\"api_key\": \"${installkey}\""   >> /config/anthill.json
 echo "}"

fi     >> /config/anthill.json

    /etc/init.d/agent.sh start >/dev/null 2>&1
	/etc/init.d/agent-monitor.sh start >/dev/null 2>&1
    echo "Anthill monitoring installed"
    sync
fi

if [ ${installaction} == 'removea' ]; then
    /etc/init.d/agent-monitor.sh stop >/dev/null 2>&1
    /etc/init.d/agent.sh stop >/dev/null 2>&1
    rm /config/anthill.json >/dev/null 2>&1
    rm -r /opt/anthill >/dev/null 2>&1
    echo "Anthill monitoring removed"
    sync
fi

sleep 2s
