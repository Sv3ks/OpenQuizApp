import socket
from threading import Thread
from sci import SCI
import json
import time


class Host:
    open_for_players: bool
    port: int
    s: socket.socket
    clients: list[dict] = []
    answers: dict[str,str] = {}

    def __init__(self,
                 port: int = 12345,
                 open: bool = False,
                 ) -> None:
        self.port = port
        self.open = open

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', port))
        self.s = s
        Thread(target=self.listen_for_clients).start()

    def listen_for_clients(self) -> None:
        s = self.s
        while True:
            print('Listening')
            s.listen()
            Thread(target=self.handle_client,args=(s.accept(),)).start()
            time.sleep(.5)
    
    def handle_client(self,
                      client: tuple[socket.socket, tuple[str,int]],
                      ) -> None:
        conn = client[0]
        addr = client[1]
        client_id = f'{addr[0]}:{addr[1]}'

        print(f'Established connection to client {client_id}')

        if not self.open:
            conn.send(SCI[1])
            conn.close()
            print(f'Declined client {client_id}')
            return
        
        conn.send(SCI[0])
        print(f'Accepted client {client_id}')
        client_info = json.loads(conn.recv(1024))
        client_data = {
            'conn': conn,
            'ip': addr[0],
            'port': addr[1],
            'username': client_info['username'],
        }
        self.clients.append(client_data)
        is_leaving = conn.recv(1024)
        if is_leaving == SCI[10]:
            print('Client disconnected')
            self.clients.remove(client_data)
        elif is_leaving == SCI[9]:
            print('Client is still here')
        else:
            print('Client is malicious, removing')
            self.clients.remove(client_data)

if __name__ == '__main__':
    host = Host(open=True)
    while True:
        time.sleep(2)
        print(host.clients)
