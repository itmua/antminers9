#!/bin/sh
#set -x

ant_conf_loc="/config/bmminer.conf"
ant_pool1url=
ant_pool1user=
ant_pool1pw=
ant_pool2url=
ant_pool2user=
ant_pool2pw=
ant_pool3url=
ant_pool3user=
ant_pool3pw=
ant_nobeeper=
ant_notempoverctrl=
ant_fan_customize_value=
ant_fan_customize_switch=
ant_freq=
ant_freq1=
ant_freq2=
ant_freq3=
ant_voltage=
ant_voltage1=
ant_voltage2=
ant_voltage3=
ant_mod=
ant_mod1=
ant_mod2=
ant_mod3=
ant_fan_rpm_off=
ant_chip_freq=
ant_autodownscale=
ant_autodownscale_reboot=
ant_autodownscale_watch=
ant_autodownscale_watchtimer=
ant_autodownscale_timer=
ant_autodownscale_after=
ant_autodownscale_step=
ant_autodownscale_min=
ant_autodownscale_prec=
ant_autodownscale_profile=
ant_minhr=
ant_asicboost=
ant_tempoff=
ant_presave=
ant_warn=
ant_maxx=
ant_trigger_reboot=
ant_target_temp=
ant_silentstart=

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
		ant_pool1url=${ant_var/_ant_pool1url=/}
		;;
		1 )
		ant_pool1user=${ant_var/_ant_pool1user=/}
		;;
		2 )
		ant_pool1pw=${ant_var/_ant_pool1pw=/}
		;;
		3 )
		ant_pool2url=${ant_var/_ant_pool2url=/}
		;;
		4 )
		ant_pool2user=${ant_var/_ant_pool2user=/}
		;;
		5 )
		ant_pool2pw=${ant_var/_ant_pool2pw=/}
		;;
		6 )
		ant_pool3url=${ant_var/_ant_pool3url=/}
		;;
		7 )
		ant_pool3user=${ant_var/_ant_pool3user=/}
		;;
		8 )
		ant_pool3pw=${ant_var/_ant_pool3pw=/}
		;;
		9 )
		ant_nobeeper=${ant_var/_ant_nobeeper=/}
		;;
		10 )
		ant_notempoverctrl=${ant_var/_ant_notempoverctrl=/}
		;;
		11 )
		ant_fan_customize_switch=${ant_var/_ant_fan_customize_switch=/}
		;;
		12 )
		ant_fan_customize_value=${ant_var/_ant_fan_customize_value=/}
		;;
		13 )
		ant_freq=${ant_var/_ant_freq=/}
		;;
		14 )
		ant_freq1=${ant_var/_ant_freq1=/}
		;;
		15 )
		ant_freq2=${ant_var/_ant_freq2=/}
		;;
		16 )
		ant_freq3=${ant_var/_ant_freq3=/}
		;;
		17 )
		ant_voltage=${ant_var/_ant_voltage=/}
		;;
		18 )
		ant_voltage1=${ant_var/_ant_voltage1=/}
		;;
		19 )
		ant_voltage2=${ant_var/_ant_voltage2=/}
		;;
		20 )
		ant_voltage3=${ant_var/_ant_voltage3=/}
		;;
		21 )
		ant_fan_rpm_off=${ant_var/_ant_fan_rpm_off=/}
		;;
		22 )
		ant_chip_freq=${ant_var/_ant_chip_freq=/}
		;;
		23 )
		ant_autodownscale=${ant_var/_ant_autodownscale=/}
		;;
		24 )
		ant_autodownscale_watch=${ant_var/_ant_autodownscale_watch=/}
		;;
		25 )
		ant_autodownscale_watchtimer=${ant_var/_ant_autodownscale_watchtimer=/}
		;;
		26 )
		ant_autodownscale_timer=${ant_var/_ant_autodownscale_timer=/}
		;;
		27 )
		ant_autodownscale_after=${ant_var/_ant_autodownscale_after=/}
		;;
		28 )
		ant_autodownscale_step=${ant_var/_ant_autodownscale_step=/}
		;;
		29 )
		ant_autodownscale_min=${ant_var/_ant_autodownscale_min=/}
		;;
		30 )
		ant_autodownscale_prec=${ant_var/_ant_autodownscale_prec=/}
		;;
		31 )
		ant_autodownscale_profile=${ant_var/_ant_autodownscale_profile=/}
		;;
		32 )
		ant_minhr=${ant_var/_ant_minhr=/}
		;;
		33 )
		ant_asicboost=${ant_var/_ant_asicboost=/}
		;;
		34 )
		ant_tempoff=${ant_var/_ant_tempoff=/}
		;;
		35 )
		ant_altdf=${ant_var/_ant_altdf=/}
		;;
		36 )
		ant_presave=${ant_var/_ant_presave=/}
		;;
		37 )
		ant_name=${ant_var/_ant_name=/}
		;;
		38 )
		ant_warn=${ant_var/_ant_warn=/}
		;;
		39 )
		ant_maxx=${ant_var/_ant_maxx=/}
		;;
		40 )
		ant_trigger_reboot=${ant_var/_ant_trigger_reboot=/}
		;;
		41 )
		ant_target_temp=${ant_var/_ant_target_temp=/}
		;;
		42 )
		ant_silentstart=${ant_var/_ant_silentstart=/}
		;;
		43 )
		ant_altdfno=${ant_var/_ant_altdfno=/}
		;;
		44 )
		ant_autodownscale_reboot=${ant_var/_ant_autodownscale_reboot=/}
		;;
		45 )
		ant_hotel_fee=${ant_var/_ant_hotel_fee=/}
		;;
		46 )
		ant_lpm_mode=${ant_var/_ant_lpm_mode=/}
		;;
		47 )
		ant_dchain5=${ant_var/_ant_dchain5=/}
		;;
		48 )
		ant_dchain6=${ant_var/_ant_dchain6=/}
		;;
		49 )
		ant_dchain7=${ant_var/_ant_dchain7=/}
		;;
	esac
	i=`expr $i + 1`
done

if [ "${ant_presave}" == "2" ]; then
[ -d /config/deploy ] || mkdir /config/deploy
ant_conf_loc="/config/deploy/"${ant_name}".conf"
fi


echo "{"									>  ${ant_conf_loc}
echo "\"pools\" : ["								>> ${ant_conf_loc}
echo "{"									>> ${ant_conf_loc}
echo "\"url\" : \"${ant_pool1url}\","						>> ${ant_conf_loc}
echo "\"user\" : \"${ant_pool1user}\","						>> ${ant_conf_loc}
echo "\"pass\" : \"${ant_pool1pw}\""						>> ${ant_conf_loc}
echo "},"									>> ${ant_conf_loc}
echo "{"									>> ${ant_conf_loc}
echo "\"url\" : \"${ant_pool2url}\","						>> ${ant_conf_loc}
echo "\"user\" : \"${ant_pool2user}\","						>> ${ant_conf_loc}
echo "\"pass\" : \"${ant_pool2pw}\""						>> ${ant_conf_loc}
echo "},"									>> ${ant_conf_loc}
echo "{"									>> ${ant_conf_loc}
echo "\"url\" : \"${ant_pool3url}\","						>> ${ant_conf_loc}
echo "\"user\" : \"${ant_pool3user}\","						>> ${ant_conf_loc}
echo "\"pass\" : \"${ant_pool3pw}\""						>> ${ant_conf_loc}
echo "}"									>> ${ant_conf_loc}
echo "]"									>> ${ant_conf_loc}
echo ","									>> ${ant_conf_loc}
echo "\"api-listen\" : "true","							>> ${ant_conf_loc}
echo "\"api-network\" : "true","						>> ${ant_conf_loc}
echo "\"api-groups\" : \"A:stats:pools:devs:summary:version\","                          >> ${ant_conf_loc}
echo "\"api-allow\" : \"W:0/0\","                       >> ${ant_conf_loc}
if [ "${ant_nobeeper}" = "true" ]; then
	echo "\"bitmain-nobeeper\" : "true","					>> ${ant_conf_loc}
fi
if [ "${ant_notempoverctrl}" = "true" ]; then
	echo "\"bitmain-notempoverctrl\" : "true","				>> ${ant_conf_loc}
fi

if [ "${ant_fan_customize_switch}" = "true" ]; then
	echo "\"bitmain-fan-ctrl\" : "true","				>> ${ant_conf_loc}
	echo "\"bitmain-fan-pwm\" : \"${ant_fan_customize_value}\","	>> ${ant_conf_loc}

fi
echo "\"bitmain-use-vil\" : "true","				>> ${ant_conf_loc}
echo "\"bitmain-freq\" : \"${ant_freq}\","				>> ${ant_conf_loc}
echo "\"bitmain-minhr\" : \"${ant_minhr}\","			>> ${ant_conf_loc}

if [ "${ant_tempoff}" != "0" ]; then
echo "\"bitmain-tempoff\" : \"${ant_tempoff}\","			>> ${ant_conf_loc}
fi

if [ "${ant_asicboost}" = "true" ]; then
echo "\"asicboost\" : ${ant_asicboost},"				>> ${ant_conf_loc}
fi

if [ "${ant_hotel_fee}" = "true" ]; then
echo "\"hotel-fee\" : ${ant_hotel_fee},"	>> ${ant_conf_loc}
fi

if [ "${ant_dchain5}" = "true" ]; then
echo "\"dchain5\" : ${ant_dchain5},"	>> ${ant_conf_loc}
fi

if [ "${ant_dchain6}" = "true" ]; then
echo "\"dchain6\" : ${ant_dchain6},"	>> ${ant_conf_loc}
fi

if [ "${ant_dchain7}" = "true" ]; then
echo "\"dchain7\" : ${ant_dchain7},"	>> ${ant_conf_loc}
fi

if [ "${ant_lpm_mode}" = "true" ]; then
echo "\"lpm-mode\" : ${ant_lpm_mode},"	>> ${ant_conf_loc}
fi

if [ "${ant_altdf}" = "true" ]; then
echo "\"altdfno\" : \"${ant_altdfno}\","				>> ${ant_conf_loc}
fi
if [ "${ant_silentstart}" = "true" ]; then
echo "\"bitmain-silentstart\" : ${ant_silentstart},"			>> ${ant_conf_loc}
fi

if [ "${ant_autodownscale}" = "true" ]; then
echo "\"bitmain-autodownscale\" : ${ant_autodownscale},"			>> ${ant_conf_loc}
fi
if [ "${ant_autodownscale_reboot}" = "true" ]; then
echo "\"bitmain-autodownscale-reboot\" : ${ant_autodownscale_reboot},"			>> ${ant_conf_loc}
fi

if [ "${ant_autodownscale_watch}" = "true" ]; then
echo "\"bitmain-autodownscale-watch\" : ${ant_autodownscale_watch},"		>> ${ant_conf_loc}
fi
if [ "${ant_autodownscale_watchtimer}" = "true" ]; then
echo "\"bitmain-autodownscale-watchtimer\" : ${ant_autodownscale_watchtimer},"	>> ${ant_conf_loc}
fi
echo "\"bitmain-autodownscale-hw\" : \"${ant_warn}\","		>> ${ant_conf_loc}
echo "\"bitmain-maxx\" : \"${ant_maxx}\","		>> ${ant_conf_loc}
echo "\"bitmain-autodownscale-timer\" : \"${ant_autodownscale_timer}\","	>> ${ant_conf_loc}
echo "\"bitmain-autodownscale-after\" : \"${ant_autodownscale_after}\","	>> ${ant_conf_loc}
echo "\"bitmain-autodownscale-step\" : \"${ant_autodownscale_step}\","		>> ${ant_conf_loc}
echo "\"bitmain-autodownscale-min\" : \"${ant_autodownscale_min}\","		>> ${ant_conf_loc}
echo "\"bitmain-autodownscale-prec\" : \"${ant_autodownscale_prec}\","		>> ${ant_conf_loc}
echo "\"bitmain-autodownscale-profile\" : \"${ant_autodownscale_profile}\","	>> ${ant_conf_loc}
echo "\"bitmain-freq1\" : \"${ant_freq1}\","			>> ${ant_conf_loc}
echo "\"bitmain-freq2\" : \"${ant_freq2}\","			>> ${ant_conf_loc}
echo "\"bitmain-freq3\" : \"${ant_freq3}\","			>> ${ant_conf_loc}
echo "\"bitmain-voltage\" : \"${ant_voltage}\","			>> ${ant_conf_loc}
echo "\"bitmain-voltage1\" : \"${ant_voltage1}\","			>> ${ant_conf_loc}
echo "\"bitmain-voltage2\" : \"${ant_voltage2}\","			>> ${ant_conf_loc}
echo "\"bitmain-voltage3\" : \"${ant_voltage3}\","			>> ${ant_conf_loc}
echo "\"bitmain-chip-freq\" : \"${ant_chip_freq}\","			>> ${ant_conf_loc}
echo "\"bitmain-fan-rpm-off\" : \"${ant_fan_rpm_off}\","			>> ${ant_conf_loc}
echo "\"bitmain-trigger-reboot\" : \"${ant_trigger_reboot}\","			>> ${ant_conf_loc}
if [ "${ant_target_temp}" != "0" ]; then
echo "\"bitmain-target-temp\" : \"${ant_target_temp}\","	>> ${ant_conf_loc}
fi
echo "\"multi-version\" : \"1\"" 				>> ${ant_conf_loc}
echo "}"						>> ${ant_conf_loc}

sync &
sleep 1s

if [ "${ant_presave}" != "1" ] && [ "${ant_presave}" != "2" ]; then
/etc/init.d/bmminer.sh restart >/dev/null 2>&1
sleep 1s
fi

echo "ok"