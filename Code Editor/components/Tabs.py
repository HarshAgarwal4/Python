import tkinter as tk
from tkinter import ttk

class Tabs:
    def __init__(self, parent):
        parent.top_Bar = ttk.Notebook(parent.left_frame)
        parent.top_Bar.pack(fill=tk.BOTH, expand=True)