import customtkinter as ctk
from colorscheme import ColorScheme
from interface import title_screen
from interface import game_client
from time import sleep

def play(colorscheme: ColorScheme, root: ctk.CTk,invalid_code: bool = False):
	def backbutton_event():
		playscreen.destroy()
		title_screen.title_screen(colorscheme,root)
	
	def joinbutton_event():
		playscreen.destroy()
		game_client.game_client(colorscheme,root,inputvar.get())

	playscreen = ctk.CTkFrame(master=root,width=500,height=500,fg_color='transparent')

	playscreen.pack(anchor='center',fill='both')
	inputvar = ctk.StringVar()
	inputentry = ctk.CTkEntry(
		master=playscreen,width=200,height=50,font=('Consolas Bold', 25, 'bold'),placeholder_text='Enter Code...',textvariable=inputvar
		)
	
	inputentry.place(anchor='center',relx=0.5,rely=0.4)

	ctk.CTkButton(
		master=playscreen,width=75,height=40,fg_color=colorscheme.FOURTH,text='BACK',font=('Consolas Bold', 20, 'bold'),command=backbutton_event,hover_color=colorscheme.TEXT,
		).place(relx=0.35,rely=0.55,anchor='center')
	
	ctk.CTkButton(
		master=playscreen,width=75,height=40,fg_color=colorscheme.SECOND,text='JOIN',font=('Consolas Bold', 20, 'bold'),command=joinbutton_event,hover_color=colorscheme.TEXT,
		).place(relx=0.65,rely=0.55,anchor='center')
