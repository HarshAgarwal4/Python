import tkinter as tk
from tkinter import ttk

class Text_Area:
    def __init__(self, parent):
        parent.T_AREA = tk.Text(parent.left_frame , undo=True)
        parent.T_AREA.pack(fill=tk.BOTH, expand=True)