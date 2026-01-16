from tkinter import *

root = Tk()
root.geometry("500x500")

def hello() :
    print("Hello")

f1 = Frame(root , bg='gray' , borderwidth=2 , relief=SUNKEN)
f1.pack(side='left' , anchor='nw' , fill=X)
b1 = Button(f1 , text="Click me" , command=hello , padx=6 ,pady=2)
b1.pack(side=LEFT , padx=10)
b1 = Button(f1 , text="Click me" , command=hello , padx=6 ,pady=2)
b1.pack(side=LEFT , padx=10)
b1 = Button(f1 , text="Click me" , command=hello , padx=6 ,pady=2)
b1.pack(side=LEFT , padx=10)
b1 = Button(f1 , text="Click me" , command=hello , padx=6 ,pady=2)
b1.pack(side=LEFT , padx=10)

root.mainloop()