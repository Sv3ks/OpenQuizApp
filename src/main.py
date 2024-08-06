import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("OpenQuizApp")
root.geometry('700x500')
root.resizable(False,False)

def clear_screen():
    for child in root.winfo_children():
        child.destroy()

def play():
    clear_screen()

    def back():
        host()

    back_button = tk.Button(master=root,text='Back',command=back)
    back_button.pack(padx=20,pady=20)


def host():
    clear_screen()
    def dialog():
        path = filedialog.askopenfilename(title='Select quiz file',filetypes=[("OpenQuizApp JSON", "*.json")])
        if not path:
            return
        
        select_button.configure(text=f'Selected file: {path}')
        play_button.configure(state=tk.ACTIVE)
    
    def play_button():
        play()
        
    select_button = tk.Button(master=root,text='Select quiz file', command=dialog)
    select_button.pack(padx=20,pady=20)
    
    play_button = tk.Button(master=root,text='Play',command=play_button,state=tk.DISABLED)
    play_button.pack(padx=20,pady=20)

if __name__ == '__main__':
    host()
    root.mainloop()