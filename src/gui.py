import customtkinter as ctk

class GUI:
	def __init__(self,colorscheme: dict = {}) -> None:
		
		root = ctk.CTk()
		root.title('LANhoot')
		root.geometry('500x500')
		root.minsize(500,500)
		root.configure(fg_color=colorscheme['DARK'])
		self.root = root
		self.stage = 'root'
		self.colorscheme = colorscheme

	def title_screen(self) -> None:
		def playbutton_event():
			self.stage = 'play'
		def hostbutton_event():
			self.stage = 'host'
		titlescreen = ctk.CTkFrame(master=self.root,width=500,height=500,fg_color='transparent')

		titlescreen.pack(anchor='center',fill='both')

		label = ctk.CTkLabel(
			master=titlescreen,text='LANhoot',font=('Consolas Bold', 100, 'bold'),text_color=self.colorscheme['TEXT']
			)

		label.place(relx=0.5,
					rely=0.2,
					anchor='center'
					)

		ctk.CTkButton(
			master=titlescreen,width=200,height=50,fg_color=self.colorscheme['SECOND'],text='PLAY',font=('Consolas Bold', 25, 'bold'),command=playbutton_event,hover_color=self.colorscheme['TEXT'],
			).place(relx=0.5,rely=0.5,anchor='center')

		ctk.CTkButton(
			master=titlescreen,width=200,height=50,fg_color=self.colorscheme['THIRD'],text='HOST',font=('Consolas Bold', 25, 'bold'),command=hostbutton_event,hover_color=self.colorscheme['TEXT'],
			).place(relx=0.5,rely=0.65,anchor='center')
		self.stage = 'title_screen'