import tkinter as tk
from tkinter import ttk
from utils.files import FileFunctions as ff
import os

class Sidebar:
    def __init__(self,parent):
        parent.sidebar =  tk.Frame(parent.side_pane , width=100 , padx=2 , pady=2)
        parent.side_pane.add(parent.sidebar)
        parent.side_btn_frame = tk.Frame(parent.sidebar, bg='black' , width=100 )
        parent.side_btn_frame.pack()
        parent.side_tree = ttk.Treeview(parent.sidebar , show='tree')
        parent.tree_scroll = ttk.Scrollbar(parent.side_tree , orient=tk.VERTICAL)
        parent.tree_scroll.pack(side='right' , fill=tk.Y)
        parent.side_tree.config(yscrollcommand=parent.tree_scroll.set)
        parent.side_tree.pack(fill=tk.BOTH , expand=True)
        parent.tree_scroll.config(command=parent.side_tree.yview)

        class tab:
            def __init__(self , name , path):
                self.name = name
                self.path = path
                self.mtime = os.path.getmtime(path)
                self.buffer = None
                self.dirty = False

        def on_select(event):
            item = parent.side_tree.identify_row(event.y)
            if not item:
                return
            title = parent.side_tree.item(item, "text")
            if parent.all_tabs.get(title).get('type') == 'file':
                path = parent.all_tabs.get(title).get('path')
                parent.opened_tabs.append(tab(os.path.basename(path) , path))
                for i in parent.opened_tabs:
                    print(str(i))

        parent.side_tree.bind("<ButtonRelease-1>" , on_select)
        # self.populate_tree(parent)


