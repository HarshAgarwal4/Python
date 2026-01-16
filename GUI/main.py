import tkinter as tk

root = tk.Tk()
root.title("My First App")
root.geometry("300x200")

def showText():
    print("Hello clicked")
    if(entry.get()):
        print(entry.get())

tk.Label(root, text="Username").grid(row=0, column=0)
entry = tk.Entry(root).grid(row=0, column=1)

# label = tk.Label(root, text="Hello, Python GUI!", font=("Arial", 16))
# label.pack()

# button = tk.Button(root , text="click me" , command=showText ,padx=4 ,pady=2)
# button.pack()

# entry = tk.Entry(root)
# entry.pack()

# button = tk.Button(root , text="Submit", command=showText , padx=8 , pady=2)
# button.pack()


root.mainloop()