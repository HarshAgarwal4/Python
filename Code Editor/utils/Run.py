import tkinter as tk
import subprocess
import sys

class RunFunctions:
    def __init__(self, parent):
        self.parent = parent
        self.process = None

    def RunCode(self):
        # path = r"C:\Users\Dell\Desktop\Harsh\python\temp.py"

        current_tab = self.parent.top_Bar.tab(
            self.parent.top_Bar.select(), "text"
        )

        tab = self.parent.opened_tabs.get(current_tab)
        if not tab or not tab.path:
            return

        # with open(path, "w", encoding="utf-8") as f:
        #     f.write(self.parent.T_AREA.get("1.0", tk.END))

        self.process = subprocess.Popen(
            ['cmd' , '/k',sys.executable, tab.path],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )