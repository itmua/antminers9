#!/bin/sh

ip=
spass=
config=

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
		ip=${ant_var/ip=/}
		;;
		1 )
		spass=${ant_var/pass=/}
		;;
		2 )
		config=${ant_var/config=/}
		;;

		esac
	i=`expr $i + 1`
done
cd /config/deploy/
cp "${config}".conf bmminer.conf  >/dev/null 2>&1
cp "${config}".fee fee.conf >/dev/null 2>&1
tar cf ../deploy.tar bmminer.conf fee.conf >/dev/null 2>&1
rm -r fee.conf >/dev/null 2>&1
rm -r bmminer.conf >/dev/null 2>&1
curl --user root:"${spass}" -X POST -F "data=@/config/deploy.tar" "${ip}"/cgi-bin/upload_deploy.cgi --anyauth >/dev/null 2>&1
rm -r /config/deploy.tar
echo "OK"
