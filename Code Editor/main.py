from tkinter import *
from core.build import AppLayout

class code_editor(Tk):
    def __init__(self):
        super().__init__()
        self.title("Code Editor - by Harsh Agarwal")
        self.geometry("544x444")
        AppLayout(self)

if __name__ == "__main__":
    App = code_editor()
    App.mainloop()
