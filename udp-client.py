import socket 

target_host = "localhost"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"This is the client", (target_host,target_port))

data,add = client.recvfrom(4096)

print(data)
