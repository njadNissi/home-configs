#!/bin/bash

python3 /home/njad/quick/readserial.py $1 $2 $3 $4 $5 $6 2>&1 | grep -v "Traceback"
if [ $? -ne 0 ]; then
	echo "Error occurred during script execution. Check the output above for details."
	echo "//----------------------------------------------------------------------\\\\"
  	echo "|| readserial -p <SERIAL PORT:str> -br <BAUDRATE:int> -cr <str>         ||"
	echo "|| e.g.: readserial -p ttyUSB0             (default baud_rate=9600)     ||"
	echo "|| e.g.: readserial -p ttyACM0 -br 115200  (default carriage_return='') ||"
	echo "|| e.g.: readserial -p ttyACM0 -br 115200 -cr '\r'                      ||"
	echo "\\\\______________________________________________________________________//"
  	exit 1
fi
#!/bin/bash

python3 /home/njad/quick/readserial.py $1 $2 $3 $4 $5 $6 2>&1 | grep -v "Traceback"
if [ $? -ne 0 ]; then
	echo "Error occurred during script execution. Check the output above for details."
	echo "//----------------------------------------------------------------------\\\\"
  	echo "|| readserial -p <SERIAL PORT:str> -br <BAUDRATE:int> -cr <str>         ||"
	echo "|| e.g.: readserial -p ttyUSB0             (default baud_rate=9600)     ||"
	echo "|| e.g.: readserial -p ttyACM0 -br 115200  (default carriage_return='') ||"
	echo "|| e.g.: readserial -p ttyACM0 -br 115200 -cr '\r'                      ||"
	echo "\\\\______________________________________________________________________//"
  	exit 1
fi
