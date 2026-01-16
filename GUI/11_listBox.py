from tkinter import *

root = Tk()
root.geometry("450x450")
root.title("list box")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END , "first item")
i=0
def add():
    global i
    lbx.insert(ACTIVE , f"{i}")
    i=i+1

b = Button(root , text="Add Item" ,command=add).pack()

root.mainloop()