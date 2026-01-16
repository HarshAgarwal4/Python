from tkinter import *

root = Tk()
root.geometry("500x500")

f1 = Frame(root , bg='gray' , borderwidth=3 , relief='sunken')
f1.pack(side=LEFT , fill=Y)
l1 = Label(f1 , text="Hello sidebar")
l1.pack(side=LEFT,anchor=CENTER)

f2 = Frame(root , bg="gray" , borderwidth=3, relief='sunken')
f2.pack(fill=X)
l2 = Label(f2 , text="this is navbar")
l2.pack(anchor=CENTER)

root.mainloop()