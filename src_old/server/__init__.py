import socket
from threading import Thread
import time

from quiz import Quiz

from client_handler import ClientHandler

def server():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', 0))

	ip = socket.gethostbyname(socket.gethostname())
	code = f'{ip.split('.')[3]}-{s.getsockname()[1]}'

	print(f'Lanhoot code: {code}')

	s.listen()

	client_handler = ClientHandler(s, open=True)

	client_handler_thread = Thread(target=client_handler.listen)
	client_handler_thread.start()

	quiz = Quiz(open('example_quiz.yml'))

	input('Press enter to start quiz')
	thread = Thread(target=client_handler.send,args=('starting',))
	thread.start()
	for i in range(0,2):
		time.sleep(1)
		print(f'Starting in {3-i}')

	print(quiz.name)

	time.sleep(2)

	for question in quiz.questions:
		print(question.title)
		Thread(target=client_handler.send,args=(question.type,)).start()
		Thread(target=client_handler.collect_answers,args=[]).start()
		for i in range(5):
			print(f'Starting in {5-i}')
			time.sleep(1)
		for answer in client_handler.answers:
			print(client_handler.answers[answer])