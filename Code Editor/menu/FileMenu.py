import tkinter as tk
from utils.files import FileFunctions as ff

class File_Menu:
    def __init__(self, parent):
        a = ff(parent)
        parent.filemenu = tk.Menu(parent.main_menu , tearoff=0)
        parent.filemenu.add_command(label="New" , command=a.newFile)
        parent.filemenu.add_command(label="Open", command=a.openFile)
        parent.filemenu.add_command(label="Open Folder", command=a.openFolder)
        parent.filemenu.add_command(label="Save" , command=a.saveFile)
        parent.filemenu.add_command(label="Save As" , command=a.saveAsFile)
        parent.filemenu.add_command(label="Save All files" , command=a.saveAllFiles)
        parent.filemenu.add_command(label="Exit" , command=a.exit)
        parent.main_menu.add_cascade(label="File" , menu=parent.filemenu)