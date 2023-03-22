#!/bin/sh
#set -x

profilename=
action=

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
		profilename=${ant_var/profilename=/}
		;;
		1 )
		action=${ant_var/action=/}
		;;
		esac
	i=`expr $i + 1`
done



if [ ${action} == 0 ]; then
savepath="/config/profiles/"${profilename}".conf"
DATE=`date +%d.%m.%Y_%H.%M.%S`
[ -f /config/profiles/"${profilename}".conf ] && savepath=/config/profiles/"${profilename}_${DATE}".conf
cp /config/bmminer.conf ${savepath}
fi
if [ ${action} == 1 ]; then
cp /config/profiles/"${profilename}".conf /config/bmminer.conf
echo "Profile activated, restarting.."
sleep 2s
/etc/init.d/bmminer.sh restart >/dev/null 2>&1
exit
fi
if [ ${action} == 2 ]; then
profilepath="/config/profiles/"${profilename}".conf"
rm -r $profilepath

echo "Profile deleted"
fi
sync &
sleep 2s

echo "Done!"