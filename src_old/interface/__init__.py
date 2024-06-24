import customtkinter as ctk
from colorscheme import ColorScheme

from interface.title_screen import title_screen
from interface.play import play
from interface.host import host
from interface.game_client import game_client


def init_gui(colorscheme: ColorScheme):
	gui = ctk.CTk()
	gui.title('LANhoot')
	gui.geometry('500x500')
	gui.minsize(500,500)
	gui.configure(fg_color=colorscheme.DARK)
	return gui