#!/bin/sh
echo -n "Masukkan website > "
read web;
sleep 2
echo "\033[1;32mTekan ctrl+z untuk hentikan\033[1;36m"
ping $web

