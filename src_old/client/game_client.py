import socket

class GameClient:
	def __init__(self,code: int) -> None:
		self.code = code
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	def connect(self) -> bool:
		ip = socket.gethostbyname(socket.gethostname()).split('.')
		server_ip = f'{ip[0]}.{ip[1]}.{ip[2]}.{self.code}'
		server_port = 15000
		try:
			self.s.connect((server_ip, server_port))
		except:
			return False
		return True
	def start(self):
		response = self.s.recv(1024).decode()
		if response != 'starting': return

		while True:
			response = s.recv(1024).decode()
			if response == 'finished': return
			if response == 'QUAD':
				s.send(int(input('QUAD: ')).to_bytes())
			if response == 'BOOL':
				s.send(bool(input('BOOL: ')).to_bytes())