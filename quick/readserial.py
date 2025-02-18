import serial, sys

port = '/dev/ttyUSB0'
br =  9600
cr = "" # carriage_return

args = sys.argv[1:]
for i in range(0, len(args), 2):
	v = args[i : i+2]

	if v[0] == '-p':
		port = '/dev/' + v[1]
	elif v[0] == '-br':
		br = int(v[1])
	elif v[0] == '-cr':
		cr = "\r"


print(f"Raeading FROM : port={port}, Baud-Rate={br}")

ser = serial.Serial(port, br)

while True:
	bs = str(ser.readline(), 'utf-8').strip('/n/r')
	print(bs, end='\r')
