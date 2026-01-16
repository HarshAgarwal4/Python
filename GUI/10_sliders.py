from tkinter import *

root = Tk()
root.geometry("450x450")
root.title("sliders")

def val(value):
    print(value)

# myslider1 = Scale(root , from_=0 ,to=100, command=val)
# myslider1.pack()
a=Label(root , text="How many dollars do you want")
myslider2 = Scale(root , from_=0 ,to=100, command=val , orient=HORIZONTAL , tickinterval=50)
myslider2.set(50)
myslider2.pack()

print(myslider2.get())

root.mainloop()