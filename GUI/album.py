from tkinter import *

root = Tk()
root.geometry("400x400")

def change():
    print(hentry.get() , ventry.get())
    root.geometry(f"{ventry.get()}x{hentry.get()}")

height = Label(root , text="Enter Height")
height.grid(row=0,column=0)
width = Label(root , text="Enter width")
width.grid(row=1,column=0)
hval = IntVar(value='')
wval = IntVar(value='')
hentry = Entry(root , textvariable=hval)
hentry.grid(row=0,column=1)
ventry = Entry(root , textvariable=wval)
ventry.grid(row=1,column=1)
b = Button(root ,text='change size',command=change)
b.grid(row=2,column=1)

root.mainloop()