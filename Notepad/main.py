from tkinter import *
import tkinter.messagebox as msg
from tkinter import filedialog
import os
import sys, os

def resource_path(path):
    try:
        base = sys._MEIPASS
    except:
        base = os.path.abspath(".")
    return os.path.join(base, path)

class NotePad(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("655x444")
        self.title("Untitled - Notepad by Harsh Agarwal")
        icon = resource_path("assets/logo.ico")
        self.wm_iconbitmap(icon)
        self.protocol("WM_DELETE_WINDOW" , self.checkOnClose)

    def TextArea(self):
        self.T_AREA = Text(self ,undo=True)
        self.T_AREA.pack(fill=BOTH , expand=True)

    def menu(self):
        self.main_menu = Menu(self)
        self.configure(menu=self.main_menu)

    file_path = None
    content = ''

    def openFile(self):
        file = filedialog.askopenfilename(
            title="Open File",
            defaultextension=".txt",
            filetypes=[
                ("All Files", "*.*"),
                ("Text Files", "*.txt"),
            ]
        )
        if file:
            a=str(file).split('/')
            try:
                with open(file , 'r' , encoding='utf-8') as f:
                    self.T_AREA.delete(1.0 , END)
                    self.T_AREA.insert(END , f.read())
                    self.content = f.read()
                    self.file_path = file
                    self.title(str(a[len(a) - 1]) +' - Notepad by Harsh Agarwal')
                    self.T_AREA.edit_reset()
            except Exception as e:
                print(e)
                msg.showerror("Error" , "Error in opening file")

    def newFile(self):
        self.content = ''
        self.T_AREA.delete(1.0 , END)
        self.file_path = None
        self.title("Untitled - Notepad by Harsh Agarwal")
        self.T_AREA.edit_reset()
        
    def saveFile(self):
        print("saving")
        if self.file_path:
            try:
                a=str(self.file_path).split('/')
                with open(self.file_path , "w" , encoding="utf-8") as f:
                    f.write(self.T_AREA.get(1.0 , END))
                self.title(a[len(a)-1] + " - Notepad by Harsh Agarwal")
                self.content = self.T_AREA.get(1.0 , END)
            except Exception as e:
                print(e)
                msg.showerror("Error" , "Error in saving file")
        else:
            self.saveAsFile()

    def saveAsFile(self):
        file = filedialog.asksaveasfilename(
            title="Save As",
            initialfile="Untitled.txt" ,
            filetypes=[
                ("All Files", "*.*"),
                ("Text Files", "*.txt"),
            ])
        if file:
            try:
                with open(file , 'w' , encoding='utf-8') as f:
                    f.write(self.T_AREA.get(1.0 , END))
                self.file_path = file
                self.title(os.path.basename(file) + " - Notepad by Harsh Agarwal")
                self.content = self.T_AREA.get(1.0 , END)
            except Exception as e:
                print(e)
                msg.showerror("Error" , "Error i n saving file")

    def exit(self):
        self.destroy()

    def FileMenu(self):
        self.File_menu = Menu(self.main_menu , tearoff=0)
        self.File_menu.add_command(label="New" , command=self.newFile)
        self.File_menu.add_command(label="Open" , command=self.openFile)
        self.File_menu.add_command(label="Save" , command=self.saveFile)
        self.File_menu.add_command(label="Save As" , command=self.saveAsFile)
        self.File_menu.add_separator()
        self.File_menu.add_command(label="Exit" , command=self.exit)
        self.main_menu.add_cascade(label="File" , menu=self.File_menu)

    def cut(self):
        self.T_AREA.event_generate("<<Cut>>")

    def Copy(self):
        self.T_AREA.event_generate("<<Copy>>")

    def Paste(self):
        self.T_AREA.event_generate("<<Paste>>")
    
    def Undo(self):
        self.T_AREA.event_generate("<<Undo>>")

    def Redo(self):
        self.T_AREA.event_generate("<<Redo>>")

    def selectall(self):
        self.T_AREA.event_generate("<<SelectAll>>")

    def EditMenu(self):
        self.Edit_Menu = Menu(self.main_menu , tearoff=0)
        self.Edit_Menu.add_command(label="Cut" , command=self.cut)     
        self.Edit_Menu.add_command(label="Copy" , command=self.Copy)     
        self.Edit_Menu.add_command(label="Paste" , command=self.Paste)   
        self.Edit_Menu.add_separator()
        self.Edit_Menu.add_command(label="Undo" , command=self.Undo)     
        self.Edit_Menu.add_command(label="Redo" , command=self.Redo)     
        self.Edit_Menu.add_command(label="Select All" , command=self.selectall)     
        self.main_menu.add_cascade(label="Edit" , menu=self.Edit_Menu)

    def scrollBar(self):
        self.scroll = Scrollbar(self.T_AREA)
        self.scroll.pack(side=RIGHT , fill=Y)
        self.scroll.config(command=self.T_AREA.yview)
        self.T_AREA.config(yscrollcommand=self.scroll.set)

    def checkOnClose(self):
        if self.content.strip() != self.T_AREA.get(1.0 , END).strip():
            a = msg.askyesnocancel("Save File" , "There are some unsaved changes. Do you want to save?")
            if a:
                self.saveFile()
                self.destroy()
            elif not a:
                self.destroy()
            else:
                return
        else:
            self.destroy()
            

if __name__ == "__main__":
    window = NotePad()
    window.menu()
    window.FileMenu()
    window.EditMenu()
    window.TextArea()
    window.scrollBar()
    window.mainloop()