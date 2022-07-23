import socket 
import threading 

IP = '0.0.0.0'
Port = 80

def main():
	server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((IP, Port))
	server.listen(5)
	print(f'[*] Listening on {IP}:{Port}')
	
	while True:
		client, add = server.accept()
		print(f'[*] Accepted connection from {add[0]}:{add[1]}')
		client_handler = threading.Thread(target=handle_client, args=(client,))
		client_handler.start()

def handle_client(client_socket):
	with client_socket as sock:
		request= sock.recv(1024)
		print(f'[*]Recieved: {request.decode("utf-8")}')
		sock.send(b'Gotcha')

if __name__=='__main__':
	main()
