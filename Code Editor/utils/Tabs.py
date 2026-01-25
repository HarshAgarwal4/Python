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

    def _get_tab_by_path(self, path):
        for title, tab in self.parent.opened_tabs.items():
            if tab.path == path:
                return title
        return None

    def open_tab(self, title, path):
        existing_title = self._get_tab_by_path(path)
        if existing_title:
            self.switch_Tab(existing_title)
            return

        if title in self.parent.opened_tabs:
            folder = os.path.basename(os.path.dirname(path))
            title = f"{title}/{folder}"

        self.parent.opened_tabs[title] = self.tab(title, path, self.parent)
        frame = ttk.Frame(self.parent.top_Bar)
        self.parent.top_Bar.add(frame , text=f'{title}')
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
        try:
            if len(self.parent.top_Bar.tabs()) != 0:
                if self.parent.Home_Frame.winfo_ismapped() : self.parent.Home_Frame.pack_forget()
                current_tab = self.parent.top_Bar.tab(
                    self.parent.top_Bar.select(), "text"
                )
                if current_tab:
                    self.activateTab(current_tab)
            else:
                self.parent.Home_Frame.pack(fill=tk.BOTH , expand=True)
        except Exception as e:
            print(e)
    
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


    def closeTab(self, event):
        notebook = event.widget
        try:
            index = notebook.index(f"@{event.x},{event.y}") 
        except tk.TclError: 
            return
        tab_id = notebook.tabs()[index] 
        title=notebook.tab(tab_id, "text") 
        tab = self.parent.opened_tabs.get(title) 
        if not tab: return self.saveFile(title, tab.path) 
        notebook.forget(tab_id) 
        a=self.parent.opened_tabs.pop(title)
        b=a.T_AREA.pack_forget()
        del b
        del a