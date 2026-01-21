import tkinter as tk
from tkinter import ttk

class Left_Frame:
    def __init__(self, parent):
        parent.left_frame = ttk.Frame(parent.side_pane)
        parent.side_pane.add(parent.left_frame)