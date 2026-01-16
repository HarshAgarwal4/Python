from tkinter import *

root = Tk()
root.geometry("450x450")
root.title("scroll bar")

#for connecting scroll bar to widget
# 1. widgetr(yscrollcommand) = scrollbar.set()
# 2. scrollbar.config(command = widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y , side=RIGHT)

list = Listbox(root , yscrollcommand=scrollbar.set)
for i in range(344):
    list.insert(END , f"Item {i}")

scrollbar.config(command=list.yview)
list.pack(fill=BOTH)

root.mainloop()