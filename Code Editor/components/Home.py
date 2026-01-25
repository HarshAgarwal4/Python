from tkinter import ttk
import tkinter as tk

def Home(parent):
        HomeFrame = tk.Frame(parent.T_frame)
        title = tk.Label(
            HomeFrame,
            text="Welcome 👋",
            font=("Segoe UI", 22, "bold")
        )
        subtitle = tk.Label(
            HomeFrame,
            text="Start by opening a folder or creating a new file.",
            font=("Segoe UI", 12),
            fg="#555555"
        )
        title.pack(pady=(60, 10))
        subtitle.pack(pady=(0, 25))
        parent.Home_Frame = HomeFrame