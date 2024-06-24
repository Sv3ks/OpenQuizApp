import customtkinter as ctk
from colorscheme import ColorScheme
from interface.host import host
from interface.play import play

def title_screen(colorscheme: ColorScheme, root: ctk.CTk):
	def playbutton_event():
		play(colorscheme,root)
		titlescreen.destroy()
	def hostbutton_event():
		host(colorscheme,root)
		titlescreen.destroy()

	titlescreen = ctk.CTkFrame(master=root,width=500,height=500,fg_color='transparent')

	titlescreen.pack(anchor='center',fill='both')

	label = ctk.CTkLabel(
		master=titlescreen,text='LANhoot',font=('Consolas Bold', 100, 'bold'),text_color=colorscheme.TEXT
		)

	label.place(relx=0.5,
				rely=0.2,
				anchor='center'
				)

	ctk.CTkButton(
		master=titlescreen,width=200,height=50,fg_color=colorscheme.SECOND,text='PLAY',font=('Consolas Bold', 25, 'bold'),command=playbutton_event,hover_color=colorscheme.TEXT,
		).place(relx=0.5,rely=0.5,anchor='center')

	ctk.CTkButton(
		master=titlescreen,width=200,height=50,fg_color=colorscheme.THIRD,text='HOST',font=('Consolas Bold', 25, 'bold'),command=hostbutton_event,hover_color=colorscheme.TEXT,
		).place(relx=0.5,rely=0.65,anchor='center')