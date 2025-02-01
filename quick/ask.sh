#!/bin/bash

# activate proxy
export https_proxy=http://localhost:7890/

pyfiglet -c green -f standard  n j a d - AI

echo "/--------------------------------------------\\"
echo "|(#) Please type your muliline prompt below  |"
echo "|   (-) press ENTER to create new line       |"
echo "|(*) Press below command followed by ENTER   |"
echo "|   (-) ESC    (on separate line) to send    |"
echo "|   (-) CTRL+C (on separate line) to quit    |"
echo "\\--------------------------------------------/"

num=1
while true; do

	pyfiglet -c green -f bigfig "Prompt # $num"

	out_file=$(mktemp)
	exit_flag=0

	trap 'exit_flag=1' SIGINT

	while read -r line; do
		# ESC: close 'cat' interactive input
		if [[ "${line:0:1}" == $'\e' ]]; then
			break	
		# Ctrl+c: close app
		elif [ $exit_flag -eq 1 ]; then
			echo "Bye-Bye"
			exit 0
		fi
		echo "$line" >> "$out_file"
	done

	content=$(cat "$out_file")
	if [[ "$content" != "" ]]; then
		pyfiglet -c green -f bigfig "Response # $num"
		python3 ~/quick/gemini.py "$content"
		((num++))
	else
		echo "+-----------------------------------------------------+"
		echo "|Empty prompt ignored, Please say something (*_*)     |"
		echo "+-----------------------------------------------------+"
	fi

	rm -f "$out_file"
	echo "+---------------------| */|\* |-------------------------+"

done
