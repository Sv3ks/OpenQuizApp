# stdlib Imports
import socket
from threading import Thread
from time import sleep

# LANhoot Imports
from client import Client
from gui import GUI


# GUI Colorscheme
colorscheme = {
	'TEXT':		'#A1A1A1',
	'LIGHT':	'#E8E6F4',
	'DARK':		'#2B2B2B',
	'FIRST':	'#82F500',
	'SECOND':	'#F57C00',
	'THIRD':	'#00C3F5',
	'FOURTH':	'#CA02E5',
}

client = Client(123)
gui = GUI(colorscheme)

class Main:
	def __init__() -> None:
		''
	def run():
		while gui.stage == 'root':
			sleep(0.1)
		gui.title_screen()
		print('Loaded title_screen')
		stage = 'title_screen'

		while True:
			sleep(.1)
			if gui.stage == stage: continue
			stage = gui.stage

Thread(target=Main().run).start()

gui.root.mainloop()