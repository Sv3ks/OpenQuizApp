import customtkinter as ctk
from interface import play
from colorscheme import ColorScheme
from client import GameClient
from time import sleep

def game_client(colorscheme: ColorScheme, root: ctk.CTk, code):
	print(code)
	gameframe = ctk.CTkFrame(master=root,width=500,height=500,fg_color='transparent')
	gameframe.pack(anchor='center',fill='both')
	ctk.CTkLabel(
		master=gameframe,text='Connecting...',font=('Consolas Bold', 50, 'bold'),text_color=colorscheme.TEXT
		).place(anchor='center',relx=0.5,rely=0.5)
	game = GameClient(int(code))
	if not game.connect():
		gameframe.destroy()
		play.play(colorscheme,root)