import serial
import sys
import socket
import time
import json
import random as rd


# udp port no
GLOVE_APP = 1180
MPU_APP = 8051

# PARAMETERS
udp_port = MPU_APP
udp_client = '127.0.0.1' #"localhost"
ser_port = 'ttyACM0'
baudrate = 115200

# HELPER CONSOLE
# READ SCRIPT ARGUMENTS 
if len(sys.argv)>2 and args[0][0] == '--help':

	print('PARAMS: -udpp [port] -udpc [client] -sp [serial port] -br [baudrate]')
	print(f'python udp_serial.py -udpp {udp_port} -udpc {udp_client} -sp {ser_port} -br {baudrate}')
	exit(0)
args = sys.argv[1:]
for i in range(0, len(args), 2):
	v = args[i : i+2]

	if v[0] == '-udpp':
		udp_port = int(v[1])

	elif v[0] == 'udpc':
		udp_client = int(v[1]) if v[1] != 'localhost' else udp_client

	if v[0] == '-sp':
		ser_port = v[1]

	if v[0] == '-br':
		ser_port = int(v[1])


# UDP SERVER
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# SERIAL COMMUNICATION
ser = serial.Serial( port='/dev/'+ser_port, 
                        baudrate=baudrate,
                        bytesize=8,
                        parity="N",
                        stopbits=1)


print(f"Writing UDP ON port={udp_port}")

#	roll, pitch, yaw = [rd.randint(0, 360) for _ in range(3)]
#	msg = f"{roll},{pitch},{yaw}"
#	print(msg)
while True:

	data = ser.readline().decode('utf-8').strip()
	
	if data:
	
		float_array = [float(x) for x in data.split(',')]
		msg = {"data":float_array}
		print(msg)
	
		server.sendto(bytes(json.dumps(msg), 'utf-8') , (udp_client, udp_port))
		time.sleep(.1)
