from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("400x400")
root.title("menu and submenu")

def myFunc():
    print("I am very amazibg")
    tmsg.showinfo("Hello"  , "I will help you")

def rate():
    tmsg.askquestion("How was your experience?")

# my_menu = Menu(root)
# my_menu.add_command(label="File" , command=myFunc)
# my_menu.add_command(label="Edit" , command=exit)
# my_menu.add_command(label="Exit" , command=exit)
# root.config(menu=my_menu)

mainmenu = Menu(root)
m1 = Menu(mainmenu , tearoff=0)
m1.add_command(label="File" , command=myFunc)
m1.add_command(label="File" , command=myFunc)
m1.add_separator()
m1.add_command(label="File" , command=myFunc)
m1.add_command(label="File" , command=myFunc)
m1.add_command(label="Exit" , command=exit)

m2 = Menu(mainmenu , tearoff=0)
m2.add_command(label="File" , command=myFunc)
m2.add_command(label="File" , command=myFunc)
m2.add_separator()
m2.add_command(label="File" , command=myFunc)
m2.add_command(label="File" , command=myFunc)
m2.add_command(label="Exit" , command=exit)
root.config(menu=mainmenu)

m3 = Menu(m2)
m3.add_command(label="Hello" , command=myFunc)
m2.add_cascade(label="Hello" , menu=m3)

mainmenu.add_cascade(label="File" , menu=m1)
mainmenu.add_cascade(label="Edit" , menu=m2)

root.mainloop()