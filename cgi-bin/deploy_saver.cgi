#!/bin/sh

config=
spass=

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
		config=${ant_var/config=/}
		;;
		1 )
		spass=${ant_var/pass=/}
		;;
		esac
	i=`expr $i + 1`
done
hostname=`cat /proc/sys/kernel/hostname | sed 's/\$//g' |  sed 's/ //g' | sed 's/\`//g'`


cd /config/deploy/
cp "${config}".conf bmminer.conf
echo "${spass}" > pass
if [ -f "/config/deploy/${config}.fee" ]; then
    mv /config/deploy/${config}.fee /config/deploy/fee.conf 
    tar cf deploy.tar bmminer.conf fee.conf
else
    tar cf deploy.tar bmminer.conf
fi

cp  /etc/confupdate.sh /config/deploy/
cp  /etc/confupdate.sh.sig /config/deploy/
tar -zcvf ../"${hostname}"_config.tar.gz deploy.tar confupdate.sh confupdate.sh.sig pass >/dev/null 2>&1
rm -r deploy.tar
rm -r bmminer.conf
rm -r confupdate.sh
rm -r confupdate.sh.sig
rm -r pass
mv /config/"${hostname}"_config.tar.gz /www/pages/
echo ${hostname}"_config.tar.gz"
