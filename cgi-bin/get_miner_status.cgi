#!/bin/sh

echo {




######SUMMARY

ant_tmp=`echo -n "{\"command\":\"summary\"}" | nc 127.0.0.1 4028`


if [ "${ant_tmp}" != "Socket connect failed: Connection refused" ]; then
echo \"summary\":
echo $ant_tmp | jqs '.SUMMARY[0] + {"elapsed": .SUMMARY[0].Elapsed} + {"stale": .SUMMARY[0].Stale} + {"ghs5s": .SUMMARY[0]."GHS 5s"} + {"ghsav": .SUMMARY[0]."GHS av"} + {"foundblocks": .SUMMARY[0]."Found Blocks"} + {"getworks ": .SUMMARY[0]."Getworks"} + {"accepted": .SUMMARY[0]."Accepted"} + {"rejected": .SUMMARY[0]."Rejected"} + {"hw": .SUMMARY[0]."Hardware Errors"} + {"utility": .SUMMARY[0]."Utility"} + {"discarded": .SUMMARY[0]."Discarded"} + {"localwork": .SUMMARY[0]."Local Work"} + {"wu": .SUMMARY[0]."Work Utility"} + {"diffa": .SUMMARY[0]."Difficulty Accepted"} + {"diffr": .SUMMARY[0]."Difficulty Rejected"} + {"diffs": .SUMMARY[0]."Difficulty Stale"} + {"bestshare": .SUMMARY[0]."Best Share"}  | del(."Get Failures", ."Remote Failures", ."Network Blocks", ."Total MH", ."Device Hardware%", ."Device Rejected%", ."Pool Rejected%", ."Pool Stale%", ."Last getwork", ."Best Share", ."Difficulty Stale", ."Difficulty Rejected", ."Difficulty Accepted", ."Work Utility", ."Local Work",.Discarded, .Utility, ."Hardware Errors", .Accepted, .Rejected, .Stale, .Elapsed, ."GHS 5s",."GHS av", ."Found Blocks", .Getworks)'
#####POOLS
else 
echo \"summary\": [ ]
fi
echo ","


ant_tmp=`echo -n "{\"command\":\"pools\"}" | nc 127.0.0.1 4028`
if [ "${ant_tmp}" != "Socket connect failed: Connection refused" ]; then
echo \"pools\": [
length=`echo $ant_tmp | jqs .POOLS | jqs length`

for VARIABLE in `seq $length`
do
	echo {
	echo \"index\": $((VARIABLE-1)),
	echo \"url\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1].URL | sed "s/stratum+tcp:\/\///"`,
	echo \"user\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1].User`,
	echo \"status\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1].Status`,
	echo \"priority\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1].Priority`,
	echo \"getworks\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1].Getworks`,
	echo \"accepted\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1].Accepted`,
	echo \"rejected\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1].Rejected`,
	echo \"discarded\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1].Discarded`,
	echo \"stale\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1].Stale`,
	echo \"diff\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1].Diff`,
	echo \"diff1\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1]."\"Diff1 Shares\""`,
	echo \"diffa\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1]."\"Difficulty Accepted\""`,
	echo \"diffr\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1]."\"Difficulty Rejected\""`,
	echo \"diffs\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1]."\"Difficulty Stale\""`,
	echo \"lsdiff\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1]."\"Last Share Difficulty\""`,
	echo \"lstime\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1]."\"Last Share Time\""`,
	echo \"boost\":`echo $ant_tmp | jqs .POOLS[$VARIABLE-1].Boost`
	echo }

	if [ $VARIABLE -ne  $length ]; then
		echo ","
	else
		echo "]"
	fi
done
else 
echo \"pools\": [ ]
fi

#####DEVS
echo ","
echo \"devs\": [

ant_tmp=`echo -n "{\"command\":\"stats\"}" | nc 127.0.0.1 4028`
if [ "${ant_tmp}" != "Socket connect failed: Connection refused" ]; then

ant_tmp=`echo $ant_tmp | sed 's|}{|},{|g'`
first=1
	for i in 6 7 8
	do

			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi

			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"`echo $ant_tmp | jqs .STATS[1].chain_acn$i`\",
			echo \"freq\":\"`echo $ant_tmp | jqs .STATS[1].freq_avg$i`\",
			echo \"freqavg\":\"`echo $ant_tmp | jqs .STATS[1].total_freqavg`\",
			if [ $i == 6 ]; then
			echo \"fan1\":\"`echo $ant_tmp | jqs .STATS[1].fan1`\",
			echo \"fan2\":\"`echo $ant_tmp | jqs .STATS[1].fan2`\",
			echo \"fan3\":\"`echo $ant_tmp | jqs .STATS[1].fan3`\",
			echo \"fan4\":\"`echo $ant_tmp | jqs .STATS[1].fan4`\",
			echo \"fan5\":\"`echo $ant_tmp | jqs .STATS[1].fan5`\",
			echo \"fan6\":\"`echo $ant_tmp | jqs .STATS[1].fan6`\",
			echo \"fan7\":\"`echo $ant_tmp | jqs .STATS[1].fan7`\",
			echo \"fan8\":\"`echo $ant_tmp | jqs .STATS[1].fan8`\",
			fi
			echo \"temp\":\"`echo $ant_tmp | jqs .STATS[1].temp$i`\",
			echo \"temp2\":\"`echo $ant_tmp | jqs .STATS[1].temp2_$i`\",
			echo \"hw\":\"`echo $ant_tmp | jqs .STATS[1].chain_hw$i`\",
			echo \"rate\": `echo $ant_tmp | jqs .STATS[1].chain_rate$i`,
			echo \"rtideal\":\"`echo $ant_tmp | jqs .STATS[1].chain_rateideal$i`\",
			echo \"totalideal\":\"`echo $ant_tmp | jqs .STATS[1].total_rateideal`\",
			echo \"totalrate\":\"`echo $ant_tmp | jqs .STATS[1].total_rate`\",
			echo \"totalacn\":\"`echo $ant_tmp | jqs .STATS[1].total_acn`\",
			echo \"chain_acs\": `echo $ant_tmp | jqs .STATS[1].chain_acs$i`,
			echo \"chain_bchips\": `echo $ant_tmp | jqs .STATS[1].chain_bchips$i`,
			echo \"chain_vol\":\"`echo $ant_tmp | jqs .STATS[1].chain_vol$i`\",
			echo \"chain_consumption\":\"`echo $ant_tmp | jqs .STATS[1].chain_consumption$i`\"
			echo }
	
	done
fi
echo "]"
####DEVS
echo }