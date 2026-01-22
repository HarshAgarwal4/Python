import tkinter as tk
from tkinter import ttk
from utils.files import FileFunctions as ff
from utils.Tabs import Tab_Functions as tf
import os

class Sidebar:
    def __init__(self, parent):
        a = tf(parent)
        parent.sidebar = tk.Frame(parent.side_pane, width=220)
        parent.sidebar.pack_propagate(False)
        parent.side_pane.add(parent.sidebar)

        tree_container = tk.Frame(parent.sidebar)
        tree_container.pack(fill=tk.BOTH, expand=True)

        parent.side_tree = ttk.Treeview(tree_container, show="tree")
        parent.side_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        parent.tree_scroll = ttk.Scrollbar(tree_container, orient=tk.VERTICAL)
        parent.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        parent.side_tree.config(yscrollcommand=parent.tree_scroll.set)
        parent.tree_scroll.config(command=parent.side_tree.yview)

        def on_select(event):
            item = parent.side_tree.identify_row(event.y)
            if not item:
                return
            title = parent.side_tree.item(item, "text")
            if parent.all_tabs.get(str(item)).get("type") == "file":
                path = parent.all_tabs.get(item).get("path")
                a.open_tab(title,path if path else None)
                

        parent.side_tree.bind("<ButtonRelease-1>", on_select)
