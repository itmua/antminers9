#!/bin/sh -e

file=antminer_vnish_backup_`date +%Y-%m-%d_%H%M%S`.tar
dir=/tmp/backup$$
bkup_files="advanced.conf \
    dropbear \
    dropbear_rsa_host_key \
    led-blink.conf \
    lighttpd-htdigest.user \
    network.conf \
    shadow \
    shadow.factory \
    vnish.conf \
    bmminer.conf \
    bmminer.conf.factory"


exec 2>&1

mkdir $dir
cd $dir

for f in $bkup_files ; do
    if [ -f /config/$f ] ; then  
	cp /config/$f .
    fi
done


> ./restoreConfig.sh
echo 'mkdir -p /config/.old_config'                      >> ./restoreConfig.sh
echo 'rm -rf /config/.old_config/*'                      >> ./restoreConfig.sh
echo 'cd /config/'                                       >> ./restoreConfig.sh
echo "for f in $bkup_files ; do"                         >> ./restoreConfig.sh
echo '    if [ -f $f ] ; then'                           >> ./restoreConfig.sh
echo '	    cp $f /config/.old_config/'                  >> ./restoreConfig.sh
echo '    fi'                                            >> ./restoreConfig.sh
echo 'done'                                              >> ./restoreConfig.sh
echo 'cd - >> /dev/null'                                 >> ./restoreConfig.sh
echo 'cp * /config/'                                     >> ./restoreConfig.sh
echo 'sync'                                              >> ./restoreConfig.sh

tar cf /www/pages/$file *

echo $file
