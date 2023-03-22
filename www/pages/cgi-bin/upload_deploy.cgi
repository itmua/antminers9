#!/bin/sh -e

# POST upload format:
# -----------------------------29995809218093749221856446032^M
# Content-Disposition: form-data; name="file1"; filename="..."^M
# Content-Type: application/octet-stream^M
# ^M    <--------- headers end with empty line
# file contents
# file contents
# file contents
# ^M    <--------- extra empty line
# -----------------------------29995809218093749221856446032--^M

file=/tmp/$$


CR=`printf '\r'`

exec 2>/tmp/restore_result

IFS="$CR"
read -r delim_line
IFS=""

while read -r line; do
    test x"$line" = x"" && break
    test x"$line" = x"$CR" && break
done

mkdir $file
cd $file
tar xf -
source /config/network.conf

pool1=`jqs .pools[0].url /config/bmminer.conf`
user1=`jqs .pools[0].user /config/bmminer.conf`
pass1=`jqs .pools[0].pass /config/bmminer.conf`
pool2=`jqs .pools[1].url /config/bmminer.conf`
user2=`jqs .pools[1].user /config/bmminer.conf`
pass2=`jqs .pools[1].pass /config/bmminer.conf`
pool3=`jqs .pools[2].url /config/bmminer.conf`
user3=`jqs .pools[2].user /config/bmminer.conf`
pass3=`jqs .pools[2].pass /config/bmminer.conf`
chips1=`jqs .\"bitmain-chip-freq\" /config/bmminer.conf`
freq1=`jqs .\"bitmain-freq\" /config/bmminer.conf`
freqc1=`jqs .\"bitmain-freq1\" /config/bmminer.conf`
freqc2=`jqs .\"bitmain-freq2\" /config/bmminer.conf`
freqc3=`jqs .\"bitmain-freq3\" /config/bmminer.conf`
volt1=`jqs .\"bitmain-voltage\" /config/bmminer.conf`
voltc1=`jqs .\"bitmain-voltage1\" /config/bmminer.conf`
voltc2=`jqs .\"bitmain-voltage2\" /config/bmminer.conf`
voltc3=`jqs .\"bitmain-voltage3\" /config/bmminer.conf`
profile1=`jqs .\"bitmain-autodownscale-profile\" /config/bmminer.conf`

pool11=`jqs .pools[0].url bmminer.conf`
user11=`jqs .pools[0].user bmminer.conf`
pass11=`jqs .pools[0].pass bmminer.conf`
pool22=`jqs .pools[1].url bmminer.conf`
user22=`jqs .pools[1].user bmminer.conf`
pass22=`jqs .pools[1].pass bmminer.conf`
pool33=`jqs .pools[2].url bmminer.conf`
user33=`jqs .pools[2].user bmminer.conf`
pass33=`jqs .pools[2].pass bmminer.conf`
chips11=`jqs .\"bitmain-chip-freq\" bmminer.conf`
freq11=`jqs .\"bitmain-freq\" bmminer.conf`
freqc11=`jqs .\"bitmain-freq1\" bmminer.conf`
freqc22=`jqs .\"bitmain-freq2\" bmminer.conf`
freqc33=`jqs .\"bitmain-freq3\" bmminer.conf`
volt11=`jqs .\"bitmain-voltage\" bmminer.conf`
voltc11=`jqs .\"bitmain-voltage1\" bmminer.conf`
voltc22=`jqs .\"bitmain-voltage2\" bmminer.conf`
voltc33=`jqs .\"bitmain-voltage3\" bmminer.conf`
profile11=`jqs .\"bitmain-autodownscale-profile\" bmminer.conf`


is_substring(){
    case "$2" in
        *$1*) return 0;;
        *) return 1;;
    esac
}

orig=$(cat /config/bmminer.conf)

cp bmminer.conf temp.conf

######URL
if [ ${pool11} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[0].url = "${pool1}"" > "$tmp" && mv "$tmp" temp.conf
else
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[0].url = "${pool11}"" > "$tmp" && mv "$tmp" temp.conf
fi

if [ ${pool22} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[1].url = "${pool2}"" > "$tmp" && mv "$tmp" temp.conf
else
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[1].url = "${pool22}"" > "$tmp" && mv "$tmp" temp.conf
fi

if [ ${pool33} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[2].url = "${pool3}"" > "$tmp" && mv "$tmp" temp.conf
else
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[2].url = "${pool33}"" > "$tmp" && mv "$tmp" temp.conf
fi
##########USER
if [ ${user11} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[0].user = "${user1}"" > "$tmp" && mv "$tmp" temp.conf
elif [ ${user11} == "\"[addhostname]\"" ]; then
	tmp=$(mktemp)
	tempuser=`echo $user1 | tr -d '"' | cut -f 1 -d'.'`
	tempuser=\"${tempuser}.${hostname}\"
	cat temp.conf | jqs ".pools[0].user = ${tempuser}" > "$tmp" && mv "$tmp" temp.conf
elif [ ${user11} == "\"[addip]\"" ]; then
	tmp=$(mktemp)
	tempip=`ip route get 8.8.8.8 | head -1 | cut -d' ' -f8 | cut -d'.' -f2,3,4 | tr "." "x"`
	tempuser=`echo $user1 | tr -d '"' | cut -f 1 -d'.'`
	tempuser=\"${tempuser}.${tempip}\"
	cat temp.conf | jqs ".pools[0].user = ${tempuser}" > "$tmp" && mv "$tmp" temp.conf
elif [ "$user11" != "${user11%.\[addhostname\]*}" ]; then
	tmp=$(mktemp)
	tempuser=`echo $user11 | tr -d '"' | cut -f 1 -d'.'`
	tempuser=\"${tempuser}.${hostname}\"
	cat temp.conf | jqs ".pools[0].user = ${tempuser}" > "$tmp" && mv "$tmp" temp.conf
elif [ "$user11" != "${user11%.\[addip\]*}" ]; then
	tmp=$(mktemp)
	tempip=`ip route get 8.8.8.8 | head -1 | cut -d' ' -f8 | cut -d'.' -f2,3,4 | tr "." "x"`
	tempuser=`echo $user11 | tr -d '"' | cut -f 1 -d'.'`
	tempuser=\"${tempuser}.${tempip}\"
	cat temp.conf | jqs ".pools[0].user = ${tempuser}" > "$tmp" && mv "$tmp" temp.conf
else
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[0].user = "${user11}"" > "$tmp" && mv "$tmp" temp.conf
fi

if [ ${user22} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[1].user = "${user2}"" > "$tmp" && mv "$tmp" temp.conf
elif [ ${user22} == "\"[addhostname]\"" ]; then
	tmp=$(mktemp)
	tempuser=`echo $user2 | tr -d '"' | cut -f 1 -d'.'`
	tempuser=\"${tempuser}.${hostname}\"
	cat temp.conf | jqs ".pools[1].user = ${tempuser}" > "$tmp" && mv "$tmp" temp.conf
elif [ ${user22} == "\"[addip]\"" ]; then
	tmp=$(mktemp)
	tempip=`ip route get 8.8.8.8 | head -1 | cut -d' ' -f8 | cut -d'.' -f2,3,4 | tr "." "x"`
	tempuser=`echo $user2 | tr -d '"' | cut -f 1 -d'.'`
	tempuser=\"${tempuser}.${tempip}\"
	cat temp.conf | jqs ".pools[1].user = ${tempuser}" > "$tmp" && mv "$tmp" temp.conf
elif [ "$user22" != "${user22%.\[addhostname\]*}" ]; then
	tmp=$(mktemp)
	tempuser=`echo $user22 | tr -d '"' | cut -f 1 -d'.'`
	tempuser=\"${tempuser}.${hostname}\"
	cat temp.conf | jqs ".pools[1].user = ${tempuser}" > "$tmp" && mv "$tmp" temp.conf
elif [ "$user22" != "${user22%.\[addip\]*}" ]; then
	tmp=$(mktemp)
	tempip=`ip route get 8.8.8.8 | head -1 | cut -d' ' -f8 | cut -d'.' -f2,3,4 | tr "." "x"`
	tempuser=`echo $user22 | tr -d '"' | cut -f 1 -d'.'`
	tempuser=\"${tempuser}.${tempip}\"
	cat temp.conf | jqs ".pools[1].user = ${tempuser}" > "$tmp" && mv "$tmp" temp.conf
else
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[1].user = "${user22}"" > "$tmp" && mv "$tmp" temp.conf
fi

if [ ${user33} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[2].user = "${user3}"" > "$tmp" && mv "$tmp" temp.conf
elif [ ${user33} == "\"[addhostname]\"" ]; then
	tmp=$(mktemp)
	tempuser=`echo $user3 | tr -d '"' | cut -f 1 -d'.'`
	tempuser=\"${tempuser}.${hostname}\"
	cat temp.conf | jqs ".pools[2].user = ${tempuser}" > "$tmp" && mv "$tmp" temp.conf
elif [ ${user33} == "\"[addip]\"" ]; then
	tmp=$(mktemp)
	tempip=`ip route get 8.8.8.8 | head -1 | cut -d' ' -f8 | cut -d'.' -f2,3,4 | tr "." "x"`
	tempuser=`echo $user3 | tr -d '"' | cut -f 1 -d'.'`
	tempuser=\"${tempuser}.${tempip}\"
	cat temp.conf | jqs ".pools[2].user = ${tempuser}" > "$tmp" && mv "$tmp" temp.conf
elif [ "$user33" != "${user33%.\[addhostname\]*}" ]; then
	tmp=$(mktemp)
	tempuser=`echo $user33 | tr -d '"' | cut -f 1 -d'.'`
	tempuser=\"${tempuser}.${hostname}\"
	cat temp.conf | jqs ".pools[2].user = ${tempuser}" > "$tmp" && mv "$tmp" temp.conf
elif [ "$user33" != "${user33%.\[addip\]*}" ]; then
	tmp=$(mktemp)
	tempip=`ip route get 8.8.8.8 | head -1 | cut -d' ' -f8 | cut -d'.' -f2,3,4 | tr "." "x"`
	tempuser=`echo $user33 | tr -d '"' | cut -f 1 -d'.'`
	tempuser=\"${tempuser}.${tempip}\"
	cat temp.conf | jqs ".pools[2].user = ${tempuser}" > "$tmp" && mv "$tmp" temp.conf
else
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[2].user = "${user33}"" > "$tmp" && mv "$tmp" temp.conf
fi

################PASS
if [ ${pass11} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[0].pass = "${pass1}"" > "$tmp" && mv "$tmp" temp.conf
else
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[0].pass = "${pass11}"" > "$tmp" && mv "$tmp" temp.conf
fi

if [ ${pass22} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[1].pass = "${pass2}"" > "$tmp" && mv "$tmp" temp.conf
else
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[1].pass = "${pass22}"" > "$tmp" && mv "$tmp" temp.conf
fi

if [ ${pass33} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[2].pass = "${pass3}"" > "$tmp" && mv "$tmp" temp.conf
else
	tmp=$(mktemp)
	cat temp.conf | jqs ".pools[2].pass = "${pass33}"" > "$tmp" && mv "$tmp" temp.conf
fi
if [ ${chips11} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".\"bitmain-chip-freq\" = "${chips1}"" > "$tmp" && mv "$tmp" temp.conf
fi
if [ ${freq11} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".\"bitmain-freq\" = "${freq1}"" > "$tmp" && mv "$tmp" temp.conf
fi
if [ ${freqc11} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".\"bitmain-freq1\" = "${freqc1}"" > "$tmp" && mv "$tmp" temp.conf
fi
if [ ${freqc22} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".\"bitmain-freq2\" = "${freqc2}"" > "$tmp" && mv "$tmp" temp.conf
fi
if [ ${freqc33} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".\"bitmain-freq3\" = "${freqc3}"" > "$tmp" && mv "$tmp" temp.conf
fi
if [ ${volt11} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".\"bitmain-voltage\" = "${volt1}"" > "$tmp" && mv "$tmp" temp.conf
fi
if [ ${voltc11} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".\"bitmain-voltage1\" = "${voltc1}"" > "$tmp" && mv "$tmp" temp.conf
fi
if [ ${voltc22} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".\"bitmain-voltage2\" = "${voltc2}"" > "$tmp" && mv "$tmp" temp.conf
fi
if [ ${voltc33} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".\"bitmain-voltage3\" = "${voltc3}"" > "$tmp" && mv "$tmp" temp.conf
fi
if [ ${profile11} == "\"[skip]\"" ]; then
	tmp=$(mktemp)
	cat temp.conf | jqs ".\"bitmain-autodownscale-profile\" = "${profile1}"" > "$tmp" && mv "$tmp" temp.conf
fi



sed -i '/":/ s//" :/g; s/\s*"/"/g; s/\s*}/}/g; s/\s*{/{/g; s/\s*]/]/g; s/\s*:"/ : "/g; s/\s*],/]\n,/g' temp.conf
mv temp.conf /config/bmminer.conf
if [ -f fee.conf ];then
    mv fee.conf /config/hotelfee.json
fi

cd ..
rm -r $file

echo "OK"
