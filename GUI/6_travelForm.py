from tkinter import *

root = Tk()
root.geometry("450x500")
root.title("Travel Form")

head = Label(text="Welcome To Harsh Travels" ,padx=4 , pady=22 , font="Arial 15 bold")
head.pack(side=TOP , anchor="center")

form = Frame(root)
form.pack()

userData = {}
formFields = [
    ("name" , 0 , 0 , "string" , 0 , 1),
    ("phone" , 1 , 0 , "int", 1 , 1),
    ("gender" , 2 , 0 , "radio" , 2 , 1),
    ("emergenece contact" , 3 , 0 , "string", 3 , 1),
    ("payment Mode" , 4 , 0 , "string", 4 , 1),
    ("Do you want meal" , 5 , 0 , "checkbox" , 5 , 1)
]

for i in formFields:
    a = Label(form, text=i[0])
    a.grid(row=i[1], column=i[2])
    
    if i[3] == 'string':
        userData[i[0]] = StringVar()
        e = Entry(form, textvariable=userData[i[0]])
        e.grid(row=i[4], column=i[5])
    elif i[3] == 'int':
        userData[i[0]] = IntVar()
        e = Entry(form, textvariable=userData[i[0]])
        e.grid(row=i[4], column=i[5])
    elif i[3] == 'checkbox':
        userData[i[0]] = IntVar()
        e = Checkbutton(form, variable=userData[i[0]])
        e.grid(row=i[4], column=i[5])
    elif i[3] == 'radio':
        e = Frame(form)
        e.grid(row=i[4] , column=i[5])
        userData[i[0]] = StringVar(value='male')
        e1 = Radiobutton(e, text="male" , variable=userData[i[0]] , value='male')
        e1.grid(row=0,column=0)
        e2 = Radiobutton(e , text="female" , variable=userData[i[0]] , value='female')
        e2.grid(row=0,column=1)

bFrame = Frame(form ,pady=20)
bFrame.grid(row=6 ,columnspan=2)

def show():
    for (key , value) in userData.items():
        print(f"{key} = {value.get()}")

submitBtn = Button(bFrame , text="Submit" , command=show)
submitBtn.pack()

root.mainloop()