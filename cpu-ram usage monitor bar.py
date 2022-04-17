import tkinter as tk
from tkinter import ttk
import sys

class Appication(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes("-alpha",1)
        self.attributes("-topmost", True)
        self.overrideredirect(True)
        self.resizable(False, False)
        self.title("CPU_RAM usage monitor bar") 

        self.set_ui()

    def set_ui(self):
        exit_button = ttk.Button(self, text = "Exit", command = self.app_exit)
        exit_button.pack(fill=tk.X) #pack() упаковщик, который собирает кнопку и размещает на окне, fill=tk.X - растянуть по горизонтали

    def app_exit(self):
        self.destroy() #разрушить окно
        sys.exit() #убить процесс


root = Appication()
root.mainloop()