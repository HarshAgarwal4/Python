import tkinter as tk

calculator = tk.Tk()
calculator.title("Simple calculator")
calculator.geometry("500x300")
calculator.configure(bg="black")

expression = ''
screen = tk.Frame(calculator , border=2 , relief="solid", width=480 ,height=50 , bg='lightgray')
screen.pack(expand=True)
screen.pack_propagate(False)
label = tk.Label(screen , text=expression , font=("Arial", 14))
label.pack(expand=True)
buttonFrame  = tk.Frame(calculator , border=1 , relief="solid" ,width=480 , height=240 , bg="gray" , )
buttonFrame.pack(expand=True)
buttonFrame.pack_propagate(False)

buttonArray = [ 
    (7,0,0) , (8,0,1) , (9,0,2) , ('/',0,3),
    (4,1,0) , (5,1,1) , (6,1,2) , ('+',1,3),
    (1,2,0) , (2,2,1) , (3,2,2) , ('-',2,3),
    ('.',3,0) , (0,3,1) , ('=',3,2) , ('x',3,3),
]

def show(value):
    global expression
    expression+=str(value)
    print(expression)
    label.config(text=expression)

def calaculate():
    global expression
    try:
        result = eval(expression)
        print(result)
        label.config(text=result)
        expression = str(result)
    except Exception as e:
        print('Invalid syntax ' , e)
        label.config(text='Invalid Syntax')


for i in buttonArray:
    if (i[0] == '='):
        button = tk.Button(buttonFrame , text=str(i[0]) , command=calaculate  , font=("Arial" , 12) ,width=12 , height=2)
        button.grid(row=i[1] ,column=i[2])
    else:
        button = tk.Button(buttonFrame , text=str(i[0]) , command=lambda t=i[0]: show(t) , font=("Arial" , 12) ,width=12 , height=2)
        button.grid(row=i[1] ,column=i[2])


calculator.mainloop()