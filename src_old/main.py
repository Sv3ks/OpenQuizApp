import interface

from colorscheme import ColorScheme

# COLOR SCHEME

def main():
	GUI = interface.init_gui(ColorScheme())
	GUI.resizable(False,False)
	interface.title_screen(ColorScheme(),GUI)
	GUI.mainloop()

if __name__ == '__main__':
	main()