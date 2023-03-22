#!/bin/sh
#set -x

printf "Status: 200\r\n\r\n"

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
		ant_url=${ant_var/_ant_url=/}
		;;
		1 )
		ant_user=${ant_var/_ant_user=/}
		;;
		2 )
		ant_pass=${ant_var/_ant_password=/}
		;;
		3 )
		ant_prec=${ant_var/_ant_prec=/}
		;;

		esac
	i=`expr $i + 1`
done


echo "{"					> /config/hotelfee.json
echo "\"url\" : \"${ant_url}\","		>> /config/hotelfee.json
echo "\"worker\" : \"${ant_user}\","		>> /config/hotelfee.json
echo "\"password\" : \"${ant_pass}\","		>> /config/hotelfee.json
echo "\"percent\" : ${ant_prec}"		>> /config/hotelfee.json
echo "}"					>> /config/hotelfee.json