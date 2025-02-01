#!/usr/bin/sh

# Define the remote server details
REMOTE_USER=$ServerXia
REMOTE_HOST=$ServerXiaHost

# Loop through the provided arguments
if [ $# -ge 1 ]; then
	for file in "$@"; do
  		# Check if the file exists
  		if [ -f "$file" ]; then
    		# Copy the file to the remote server using scp
    		scp "$file" "$REMOTE_USER@$REMOTE_HOST:~/.njad/$file"
  		else
    		echo "Error: File '$file' not found."
  		fi
	done
else
	scp -r $PWD "$REMOTE_USER@$REMOTE_HOST:~/.njad/$(basename $(pwd))"
fi
