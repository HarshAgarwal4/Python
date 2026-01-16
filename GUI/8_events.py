from tkinter import *

root = Tk()
root.geometry("450x500")

widget = Button(root , text="Click Me")
widget.pack()

def harsh(event):
    print(f"clicked at {event.x} , {event.y}")

widget.bind('<Button-1>' , harsh)
widget.bind('<Double-1>' , quit)

root.mainloop()