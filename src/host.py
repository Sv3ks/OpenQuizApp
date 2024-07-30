import socket
from threading import Thread
from sci import SCI
import json
import time
from datetime import datetime
import math


class Host:
    open_for_players: bool
    port: int
    s: socket.socket
    clients: list[dict] = []
    answers: dict[str,str] = {}
    times: dict[str,datetime] = {}
    points: dict[str,int] = {}
    disconnected_users: list[str] = []

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

    def send_bytes_client(self,
                         client: dict,
                         bytes_message: bytes
                         ):
        Thread(target=client['conn'].sendall,args=(bytes_message,)).start()
        #print('started sending bytes to client')

    def broadcast_clients(self,
                          message: str | bytes
                          ):
        if type(message) == str:
            message = bytes(message)
        for client in self.clients:
            self.send_bytes_client(client,message)

    def collect_answer_client(self,
                              client: dict,
                              ):
        try:
            self.answers[client['username']] = client['conn'].recv(1024).decode()
            self.times[client['username']] = datetime.now()
        except:
            self.clients.remove(client)
            self.disconnected_users.append(client['username'])
            print('CLIENT DISCONNECTED')

    def collect_answers(self,):
        for client in self.clients:
            Thread(target=self.collect_answer_client,args=(client,)).start()

    def calculate_points(self,
                         question_time: datetime,
                         question: dict,
                         ) -> dict:
        points = {}
        for username, answer in self.answers.items():
            print(f'{username}:{answer}')
            if answer == b'' or username in self.disconnected_users or question['answers'][answer] != True:
                points[username] = 0
                continue
            else:
                difference = self.times[username] - question_time
                #? MAX POINTS - DIFFERENCE * 100 (FOR ACCURACY) / TOTAL TIME TO ANSWER QUESTION * (100 + MINIMUM POINTS FOR CORRECT ANSWER SAFETY) * 1000
                points[username] = 1000 - int(math.floor(difference.total_seconds() * 100) / (question['time']*200) * 1000)
        return points

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

    def start(self,
              quiz: dict
              ):
        self.open = False

        for client in self.clients:
            self.points[client['username']] = 0

        self.broadcast_clients(SCI[8])
        for question in quiz['questions']:
            self.answers = {}
            print(f'Prompting question "{question['title']}"')

            question_time = datetime.now()

            question_json = {
                'type': question['type'].upper(),
                'answers': []
            }

            for answer in question['answers']:
                question_json['answers'].append(answer)

            self.broadcast_clients(json.dumps(question_json).encode())

            self.collect_answers()

            time.sleep(question['time']) #* ≈time for users to answer

            for username, points in self.calculate_points(question_time,question).items():
                self.points[username] += points

            print(self.points)
            time.sleep(5) #* wait for next question
        
        print('quiz finished')

        

if __name__ == '__main__':
    import keyboard
    host = Host(open=True)
    while True:
        time.sleep(2)
        if keyboard.is_pressed('s'):
            print('Starting')
            with open('./test_quiz.json') as f:
                host.start(json.load(f))
        #print(f'Clients: {len(host.clients)}')
