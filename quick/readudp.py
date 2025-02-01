import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('192.168.186.221', 65530)  # Replace with your desired address and port
sock.bind(server_address)

while True:
    # Receive data from the socket
    data, address = sock.recvfrom(4096)  # Adjust buffer size as needed

    # Decode the received data (assuming it's encoded in UTF-8)
    received_data = data.decode('utf-8')

    # Print the received data and sender address
    print(f'Received data from {address}: {received_data}')

    # Process the received data as needed

# Close the socket
sock.close()

