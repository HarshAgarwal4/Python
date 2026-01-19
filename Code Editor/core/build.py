import tkinter as tk
from menu.FileMenu import File_Menu
from menu.EditMenu import Edit_menu
from components.TextArea import Text_Area

class AppLayout:
    def __init__(self , parent):
        self.mainmenu(parent)
        self.build(parent)

    def mainmenu(self, parent):
        parent.main_menu = tk.Menu(parent)
        parent.config(menu=parent.main_menu)
        File_Menu(parent)
        Edit_menu(parent)

    def build(self , parent):
        Text_Area(parent)