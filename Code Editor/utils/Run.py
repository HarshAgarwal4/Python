import tkinter as tk
import subprocess
import sys
from utils.files import FileFunctions as f

import os
import sys

def get_run_command(path):
    ext = os.path.splitext(path)[1].lower()
    base = os.path.splitext(os.path.basename(path))[0]

    if ext == ".py":
        return ["cmd", "/k", 'python' ,path ]

    if ext == ".js":
        return ["cmd", "/k", 'node' ,path]

    if ext == ".c":
        folder = os.path.dirname(os.path.abspath(path))
        base = os.path.splitext(os.path.basename(path))[0] 
        exe = base + ".exe"
        try:
            compile_cmd = ["gcc", os.path.basename(path), "-o", exe]
            compile_proc = subprocess.run( compile_cmd, cwd=folder, shell=False ) 
            if compile_proc.returncode != 0: 
                print("Compilation failed") 
                return
            subprocess.Popen( ["cmd", "/k", exe], cwd=folder, creationflags=subprocess.CREATE_NEW_CONSOLE )
        except Exception as e:
            print(e)

    if ext == ".cpp":
        folder = os.path.dirname(os.path.abspath(path))
        base = os.path.splitext(os.path.basename(path))[0] 
        exe = base + ".exe"
        try:
            compile_cmd = ["g++", os.path.basename(path), "-o", exe]
            compile_proc = subprocess.run( compile_cmd, cwd=folder, shell=False ) 
            if compile_proc.returncode != 0: 
                print("Compilation failed") 
                return
            subprocess.Popen( ["cmd", "/k", exe], cwd=folder, creationflags=subprocess.CREATE_NEW_CONSOLE )
        except Exception as e:
            print(e)
    
    return None

class RunFunctions:
    def __init__(self, parent):
        self.parent = parent
        self.process = None
        self.file = f(parent)

    def RunCode(self):
        # path = r"C:\Users\Dell\Desktop\Harsh\python\temp.py"
        self.file.saveAllFiles()
        current_tab = self.parent.top_Bar.tab(
            self.parent.top_Bar.select(), "text"
        )
        tab = self.parent.opened_tabs.get(current_tab)
        print(tab , tab.path)
        if not tab or not tab.path:
            return
        ext = os.path.splitext(tab.path)[1].lower()

        cmd = get_run_command(tab.path)
        if ext != '.c' and ext != '.cpp':
            if not cmd:
                print("No runner available for this file type")
                return
            self.process = subprocess.Popen(
                cmd,
                cwd=self.parent.folder,
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )