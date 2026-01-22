import tkinter as tk
from tkinter import ttk

class Pane:
    def __init__(self, parent):
        parent.side_pane = ttk.PanedWindow(parent, orient=tk.HORIZONTAL)
        parent.side_pane.pack(fill=tk.BOTH, expand=True)
