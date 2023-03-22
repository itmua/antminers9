#!/bin/sh

ip=
spass=
config=
action=
status=
port=
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
		action=${ant_var/action=/}
		;;
		3 )
		status=${ant_var/status=/}
		;;
		4 )
		port=${ant_var/port=/}
		;;

		esac
	i=`expr $i + 1`
done

curl --user root:"${spass}" -d "action=${action}&status=${status}&port=${port}" -X POST "${ip}"/cgi-bin/ssh.cgi --anyauth

echo "OK"