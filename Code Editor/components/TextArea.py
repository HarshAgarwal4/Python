import tkinter as tk
from tkinter import ttk

class Text_Area:
    def __init__(self, parent):
        parent.T_frame = ttk.Frame(parent.left_frame)
        parent.T_frame.pack(fill="both", side="bottom" , expand=True)