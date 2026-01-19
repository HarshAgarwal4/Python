import tkinter as tk

class Text_Area:
    def __init__(self, parent):
        parent.T_AREA = tk.Text(parent , undo=True)
        parent.T_AREA.pack(fill=tk.BOTH ,expand=True)