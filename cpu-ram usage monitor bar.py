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

        self.bar2 = ttk.LabelFrame(self, text = "Manual") #создание рамки, области, на которой будут размещаться кнопки
        self.bar2.pack(fill=tk.X)

        self.combo_win = ttk.Combobox(self.bar2,
                                        values=["hide","don`t hide", "min"],
                                        width=8, state="readonly")#выпадающий список
        self.combo_win.current(1) #текущее значение в списке для отображения по умолчанию
        self.combo_win.pack(side=tk.LEFT)

        ttk.Button(self.bar2, text="move").pack(side=tk.LEFT)
        ttk.Button(self.bar2, text=">>>").pack(side=tk.LEFT)

        self.bar2 = ttk.LabelFrame(self, text = "Power") 
        self.bar2.pack(fill=tk.BOTH)

        self.bind_class("Tk", "<Enter>", self.enter_mouse) #обработчик событий при наведении мыши, при срабатывании обработчика в метод должен передаваться параметр event
        self.bind_class("Tk", "<Leave>", self.leave_mouse) #обработчик событий при убирании курсора мыши

    def enter_mouse(self, event):
        if self.combo_win.current() == 0 or 1: #hide ot dont hide
            self.geometry("")

    def leave_mouse(self, event):
        if self.combo_win.current() == 0:
            self.geometry(f"{self.winfo_width()}x1") #получаем текущую ширину окна и меняем высоту на 1 пиксель     
        
        
    def app_exit(self):
        self.destroy() #разрушить окно
        sys.exit() #убить процесс


root = Appication()
root.mainloop()