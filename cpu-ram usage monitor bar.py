import tkinter as tk

class Appication(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes("-alpha",1)
        self.attributes("-topmost", True)
        self.overrideredirect(True)
        self.resizable(False, False)

root = Appication()
root.mainloop()