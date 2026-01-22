import tkinter as tk
from utils.Run import RunFunctions as r

class Run_Menu:
    def __init__(self,parent):
        a = r(parent)
        parent.run_menu = tk.Menu(parent , tearoff=0)
        parent.run_menu.add_command(label="Run Code" , command=a.RunCode)
        parent.main_menu.add_cascade(label="Run" , menu=parent.run_menu)