import tkinter as tk
from menu.FileMenu import File_Menu
from menu.EditMenu import Edit_menu
from menu.RunMenu import Run_Menu
from components.TextArea import Text_Area
from components.SidebarPane import Pane
from components.Sidebar import Sidebar
from components.leftFrame import Left_Frame
from components.Tabs import Tabs

class AppLayout:
    def __init__(self , parent):
        self.variables(parent)
        self.mainmenu(parent)
        self.build(parent)

    def variables(self , parent):
        parent.folder = None
        parent.side_tree = None
        parent.opened_tabs = {}
        parent.all_tabs = {}

    def mainmenu(self, parent):
        parent.main_menu = tk.Menu(parent)
        parent.config(menu=parent.main_menu)
        File_Menu(parent)
        Edit_menu(parent)
        Run_Menu(parent)

    def build(self , parent):
        Pane(parent)
        Sidebar(parent)
        Left_Frame(parent)
        Text_Area(parent)
        Tabs(parent)