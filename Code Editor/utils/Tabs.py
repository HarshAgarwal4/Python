import tkinter as tk
from tkinter import ttk
import os


class Tab_Functions:
    class tab:
        def __init__(self, name, path, parent):
            self.name = name
            self.path = path
            self.mtime = os.path.getmtime(path) if path else None
            self.buffer = None
            self.dirty = False
            self.T_AREA = tk.Text(parent.T_frame, undo=True)
            if self.path:
                with open(path) as f:
                    self.T_AREA.insert(1.0, f.read())
            self.T_AREA.pack_forget()
            self.T_AREA.edit_reset()

    def __init__(self, parent):
        self.parent = parent
        self.current_text = None

    def open_tab(self, title, path):
        if self.parent.opened_tabs.get(title) and (title == 'Untitled' or self.parent.opened_tabs.get(title).path == path):
            self.switch_Tab(title)
            return
        if self.parent.opened_tabs.get(title) and self.parent.opened_tabs.get(title).path != path:
            title = title + '/' + os.path.basename(os.path.dirname(path))
        self.parent.opened_tabs[title] = self.tab(title, path, self.parent)
        t = ttk.Frame(self.parent.top_Bar)
        self.parent.top_Bar.add(t, text=title)
        self.switch_Tab(title)

    def switch_Tab(self, name):
        for tabId in self.parent.top_Bar.tabs():
            if self.parent.top_Bar.tab(tabId, "text") == name:
                self.parent.top_Bar.select(tabId)
                break

    def activateTab(self, current_tab):
        tab = self.parent.opened_tabs.get(current_tab)
        if not tab:
            return

        if self.current_text:
            self.current_text.pack_forget()

        tab.T_AREA.pack(fill=tk.BOTH, expand=True)
        self.current_text = tab.T_AREA

    def on_tab_change(self, event):
        current_tab = self.parent.top_Bar.tab(
            self.parent.top_Bar.select(), "text"
        )
        self.activateTab(current_tab)