import socket
from client import Client

client = Client(123)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1',80))

if client.connect():
	print('YES!')
else:
	print('NO!')