import tkinter as tk

class Run_Menu:
    def run(self):
        print("running")

    def __init__(self,parent):
        parent.edit_menu = tk.Menu(parent , tearoff=0)
        parent.edit_menu.add_command(label="Run Code" , command=self.run)
        parent.main_menu.add_cascade(label="Run" , menu=parent.edit_menu)