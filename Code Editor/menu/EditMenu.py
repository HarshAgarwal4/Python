import tkinter as tk
from utils.operations import operationsClass as op

class Edit_menu:
    def __init__(self, parent):
        a = op(parent)
        parent.edit_menu = tk.Menu(parent.main_menu , tearoff=0)
        parent.edit_menu.add_command(label="Cut" , command=a.cut )
        parent.edit_menu.add_command(label="Copy" , command=a.copy )
        parent.edit_menu.add_command(label="Paste" , command=a.paste )
        parent.edit_menu.add_separator()
        parent.edit_menu.add_command(label="Undo" , command=a.undo )
        parent.edit_menu.add_command(label="Redo" , command=a.redo )
        parent.edit_menu.add_command(label="Select All" , command=a.selectAll )
        parent.main_menu.add_cascade(label = "Edit" , menu = parent.edit_menu)