#!/bin/bash

# Check if anything else is still running
if [[ `pgrep -f $0` != "$$" ]]; then
	echo "Another instance of script already exist! Exiting"
	exit
fi

# Script to upload to dakboard
cd /root/personal-app/dakboard

# Load .env
set -a
. .env
set +a

echo "Publish IP: ${PUBLISH_IP}."

# Generate image
echo "Running main..."
python3 main.py

# Rotate the image
echo "Rotating image..."
convert result.jpg -rotate 90 out.jpg

# Copy over the image
echo "Copying over image..."
echo "scp out.jpg root@$PUBLISH_IP:/home/ubuntu/result.jpg"
scp out.jpg root@$PUBLISH_IP:/home/ubuntu/result.jpg

# Run the ssh 
echo "Starting fb command..."
echo "ssh root@$PUBLISH_IP /home/ubuntu/start.sh"
ssh root@$PUBLISH_IP /home/ubuntu/start.sh 
