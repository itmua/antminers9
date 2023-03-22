#!/bin/sh

[ -d /config/deploy ] || mkdir /config/deploy 

tree -J /config/deploy/ -P *.conf

sync &
