#!/bin/sh

[ -d /config/profiles ] || mkdir /config/profiles

tree -J /config/profiles/ -P *.conf

sync &
