import tkinter as tk
from tkinter import ttk
from components.Sidebar import Sidebar as s
from utils.Tabs import Tab_Functions as tf

class Tabs:
    def __init__(self, parent):
        a=tf(parent)
        self.parent = parent
        parent.top_Bar = ttk.Notebook(parent.left_frame)
        parent.top_Bar.pack(fill=tk.BOTH, expand=False)
        a.open_tab("Untitled" , None)
        parent.prev_tab = parent.top_Bar.tab(parent.top_Bar.select(), "text")
        parent.top_Bar.bind("<<NotebookTabChanged>>", a.on_tab_change)