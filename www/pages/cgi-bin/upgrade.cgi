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

trap atexit 0

atexit() {
	rm -rf $file
	umount $file.boot 2>/dev/null || true
	rmdir $file.boot 2>/dev/null || true
	sync
	if [ $ok == 1 ]; then
	    echo "System Upgrade Successed"
		sleep 5
		reboot
	else
		cat /tmp/upgrade_result
	fi
}
CR=`printf '\r'`

exec 2>/tmp/upgrade_result

IFS="$CR"
read -r delim_line
IFS=""

while read -r line; do
    test x"$line" = x"" && break
    test x"$line" = x"$CR" && break
done

mkdir $file
cd $file

error_handling()
{
    rm $$.tgz
    exit 1
}

#### validity check
cat > $$.tgz
if [ -f $$.tgz ]
then
    tar ztvf $$.tgz | grep "^l" >& /dev/null
    if [ $? -eq 0 ]
    then
        echo "tar ball contains symbol link" >>/tmp/upgrade_new.log
        error_handling
    fi
    echo "no symbol link found" >>/tmp/upgrade_new.log
else
    echo "unkown error occurs, can't find tar ball" >>/tmp/upgrade_new.log
    error_handling
fi

tar zxf $$.tgz
rm $$.tgz


if [ -f confupdate.sh ]; then
	openssl dgst -sha256 -verify /etc/vnish.pem -signature  confupdate.sh.sig  confupdate.sh >/dev/null  2>&1
	res=$?
	if [ $res -ne 0 ]; then
		echo "Config Not Signtured!!!"
	else
		sh confupdate.sh
		/etc/init.d/bmminer.sh restart >/dev/null 2>&1
		ok=1
		exit
	fi
fi


if [ ! -f runme.sh.sig ]; then
    echo "Cannot Find Signature!!!">> /tmp/upgrade_result
	ok=0
else    
    openssl dgst -sha256 -verify /etc/vnish.pem -signature  runme.sh.sig  runme.sh >/dev/null  2>&1
    res=$?
		if [ $res -ne 0 ]; then
            openssl dgst -sha256 -verify /etc/bitmain-pub.pem -signature  runme.sh.sig  runme.sh >/dev/null  2>&1
            res=$?
        fi
		if [ $res -ne 0 ]; then
		    echo "Installer Not Signtured!!!" >> /tmp/upgrade_result
			ok=0
		else
		    if [ ! -f ubi_info ]; then
				    echo "Incorrect firmware no ubi_info!!!" >> /tmp/upgrade_result
					ok=0
				else

					if [ ! -d /mnt/config ];then
					    mkdir /mnt/config
					fi
				

					ubiattach /dev/ubi_ctrl -m 2
					mount -t ubifs ubi1:rootfs /mnt/config

					if [ ! -d /mnt/config/home/usr_config ];then
					    mkdir /mnt/config/home/usr_config
					fi
					cp -r /config/* /mnt/config/home/usr_config/
					#umount /dev/mtdblock2
					umount /mnt/config
					ubidetach -d 1 /dev/ubi_ctrl
					if [ -f /etc/init.d/firewall.sh ]; then					
						awk '{print $4}' /etc/init.d/firewall.sh | sed '/^$/d' > /config/iplist
					sync
                    fi
					if [ -f runme.sh ]; then					
					   sh runme.sh
					   ok=1
                    else
					    echo "Incorrect firmware!!!!" >> /tmp/upgrade_result
						ok=0
					fi
			 fi
		fi
fi
