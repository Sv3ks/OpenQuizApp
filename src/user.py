import socket
from threading import Thread
from sci import SCI
import json

class User:
    def __init__(self,
                 username: str = ''
                 ) -> None:
        self.userdata = {
            'username': username
        }
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self,
                ip: str,
                port: int = 12345,
                ) -> None:
        s = self.s

        print(f'Connecting to host at {ip}:{port}')
        s.connect((ip,port))
        print(f'Established connection to host')
        accepted = s.recv(1024)
        if accepted != SCI[0]:
            print(f'Server declined')
            return
        print(f'Server accepted')
        s.send(json.dumps(self.userdata).encode())
        if s.recv(1024) != SCI[8]:
            print('unknown response')
        s.send(SCI[9])
        question = json.loads(s.recv(1024))
        print(question)
        s.send('correct answer'.encode())

if __name__ == '__main__':
    user = User(username='bad_username')
    user.connect(ip='127.0.0.1')
