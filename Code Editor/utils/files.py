import tkinter.messagebox as msg
import tkinter.filedialog as fd
import tkinter as tk
from utils.Tabs import Tab_Functions as tf
import os

class FileFunctions:
    def __init__(self , parent):
        self.parent = parent
        self.a = tf(parent)

    def makeTree(self, p, parent_node=""):
        
        if parent_node == '':
            self.parent.side_tree.delete(*self.parent.side_tree.get_children())
            self.parent.all_tabs = {}

        if not p:
            return

        try:
            items = os.listdir(p)
        except PermissionError:
            return

        for item in items:
            if item == ".git":
                continue

            full_path = os.path.join(p, item)

            node = self.parent.side_tree.insert(
                parent_node,
                "end",
                text=item,
            )
            self.parent.all_tabs[str(node)] = {
                "path" : full_path,
                "type" : "file" if os.path.isfile(full_path) else ("folder" if os.path.isdir(full_path) else None),
            }
            if os.path.isdir(full_path):
                self.makeTree(full_path, node)      

    def openFolder(self):
        folder = fd.askdirectory()
        self.parent.folder = folder
        if self.parent.folder:
            self.makeTree(self.parent.folder)
        
    def newFile(self):
        self.a.open_tab("Untitled" , None)

    def openFile(self):
        file = fd.askopenfilename(
            title="Open File",
            filetypes=(
                ("All Files", "*.*"),
                ("Python files" ,  '.py')
            )
        )
        if file:
            self.a.open_tab(os.path.basename(file) , file)  

    def saveFile(self):
        pass

    def saveAsFile(self):
        pass
        
    def exit(self):
        self.parent.destroy()

