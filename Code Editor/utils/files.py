import tkinter.messagebox as msg
import tkinter.filedialog as fd
import tkinter as tk
from utils.Tabs import Tab_Functions as tf
import os

class FileFunctions:
    def __init__(self , parent):
        self.parent = parent
        self.a = tf(parent)
        self.parent.protocol("WM_DELETE_WINDOW" , self.saveBeforClose)

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

    def saveFile(self,title=None,path=None):
        try:
            current_tab = None
            if self.parent.mode == 'single':
                current_tab = self.parent.top_Bar.tab(
                    self.parent.top_Bar.select(), "text"
                )
                if not current_tab: return
                title = self.parent.opened_tabs.get(current_tab).name
                path = self.parent.opened_tabs.get(current_tab).path
            if not path:
                if self.parent.opened_tabs.get(title).T_AREA.get(1.0 , tk.END).strip() == '': return
                self.saveAsFile()
            if title:
                content = self.parent.opened_tabs.get(title).T_AREA.get(1.0 , tk.END)
            with open(path , "w" , encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(e)

    def saveAsFile(self,title=None):
        try:
            if self.parent.mode == 'single':
                current_tab = self.parent.top_Bar.tab(
                    self.parent.top_Bar.select(), "text"
                )
                if not current_tab: return
                title = self.parent.opened_tabs.get(current_tab).name
            file = fd.asksaveasfilename(
                title="Save As",
                initialfile="Untitled.txt" ,
                filetypes=[
                    ("All Files", "*.*"),
                    ("Text Files", "*.txt"),
                ]
            )
            if file:
                with open(file , 'w' , encoding='utf-8') as f:
                    f.write(self.parent.opened_tabs.get(title).T_AREA.get(1.0 , tk.END))
                    if title == "Untitled":
                        k=self.parent.opened_tabs.pop(title)
                        del k
                        self.parent.top_Bar.tab(self.parent.top_Bar.select(), text=os.path.basename(file))
                        self.parent.opened_tabs[os.path.basename(file)] = self.a.tab(os.path.basename(file), file, self.parent)
                if file.startswith(self.parent.folder):
                    self.makeTree(self.parent.folder)
        except Exception as e:
            print(e)

    def saveAllFiles(self):
        self.parent.mode = 'All'
        for i in self.parent.opened_tabs.keys():
            try:
                self.saveFile(self.parent.opened_tabs.get(i).name,self.parent.opened_tabs.get(i).path)
            except Exception as e:
                print(e)
        self.parent.mode = 'single'
    
    def saveBeforClose(self):
        self.saveAllFiles()
        self.parent.destroy()

    def exit(self):
        self.parent.destroy()