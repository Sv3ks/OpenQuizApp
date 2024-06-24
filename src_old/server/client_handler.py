import socket
from threading import Thread
from quiz import Question

class Client:
	def __init__(self, client: tuple[socket.socket, tuple]) -> None:
		self.client = client
		self.conn = client[0]
		self.addr = client[1]
		self.ip = client[1][0]
		self.port = client[1][1]

class ClientHandler:
	def __init__(self, s: socket.socket, open: bool = False) -> None:
		self.s = s
		self.open = open
		self.clients = []
		self.answers = {}
	
	def listen(self):
		print('Listening')
		s = self.s
		s.listen()
		while self.open:
			client = Client(s.accept())
			print(f'Accepted client...')
			self.clients.append(client)
			self.answers[f'{client.ip}:{client.port}'] = None
			print(f'Accepted client {client.addr[0]}:{client.addr[1]}')
	
	def send_client(self,msg: str, client: Client):
		client.conn.send(msg.encode())
	
	def send(self,msg: str):
		for client in self.clients:
			Thread(target=self.send_client,args=(msg, client)).start()
	
	def collect_answer_client(self, client: Client):
		self.answers[f'{client.ip}:{client.port}'] = client.conn.recv(1024)
	
	def collect_answers(self):
		for client in self.clients:
			Thread(target=self.collect_answer_client,args=(client,)).start()
	
	def reset_answers(self):
		for client in self.clients:
			self.answers[f'{client.ip}:{client.port}'] = None