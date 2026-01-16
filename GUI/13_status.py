from tkinter import *

root = Tk()
root.geometry("450x450")
root.title("status bar")

statusVar = StringVar()
statusVar.set("Ready")

def Upload():
    statusVar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusVar.set("Ready Now")

def update():
    import time
    sbar.config(text=time.strftime("Ready | %H:%M:%S"))
    root.after(1000, update)

sbar = Label(root , text=" ", relief=SUNKEN , anchor=W)
sbar.pack(side=BOTTOM , fill=X)

b = Button(root ,text="upload files" , command=Upload)
b.pack()

update()

root.mainloop()