from tkinter import *

root = Tk()
root.geometry("500x500")

def submit():
    print(userValue.get())
    print(passwordValue.get())
    userValue.set(' ')
    passwordValue.set(' ')

uuse_label = Label(root , text="Username")
uuse_label.grid()
pass_Label = Label(root , text="Password")
pass_Label.grid(row=1)

userValue = StringVar()
passwordValue = StringVar()

u = Entry(root , textvariable=userValue)
u.grid(column=1 , row=0)
p = Entry(root , textvariable=passwordValue)
p.grid(column=1 ,row=1)

b = Button(text='submit' , command=submit)
b.grid(row=2)

root.mainloop()