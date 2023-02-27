#!/bin/sh
# killall fbi
# fbi -d /dev/fb0 -a --autorotate 1  -T 1 --noverbose /home/ubuntu/result.jpg

#fbi -d /dev/fb1 -T 1 out1.jpg


# Display the second image in the back buffer
fbi -d /dev/fb0 -noverbose -T 1 -a /home/ubuntu/result.jpg

# Set the display to use the back buffer
fbset -fb /dev/fb0 -buf 1

# Display the back buffer with the second image
fbi -d /dev/fb0 -noverbose -T 1
