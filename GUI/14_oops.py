from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.status = Label(self ,  textvariable=self.var , relief=SUNKEN , anchor=W)
        self.status.pack(side=BOTTOM , fill='x')
    
    def click(self):
        print("Clicked")

    def createButton(self , text):
        Button(self , text=text , padx=4 , pady=2 , relief=SUNKEN , command=self.click).pack()


if __name__ == "__main__":
    window = GUI()
    window.status()
    window.createButton("status")
    window.mainloop()