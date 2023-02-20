#!/bin/sh
killall fbi
fbi -d /dev/fb0 -a --autorotate 1  -T 1 --noverbose /home/ubuntu/result.jpg
