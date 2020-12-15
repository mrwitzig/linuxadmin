#!/bin/bash
ping -c 2 google.com >> networkstatus.txt
hostname >> networkstats.txt
tcptrack >> networkstats.txt
CURRENTDATE=$(date +'%A, %M %d %Y %H:%M')

echo "Network Info updated $CURRENTDATE" >> networkstats.txt 
