from tkinter import *

root = Tk()
root.geometry("450x500")
root.title("Canvas")

canv = Canvas(root , width=450 , height=500)
canv.pack()

canv.create_line(0,0,450,500)
canv.create_line(0,500,450,0)

# Assuming 'my_frame' is a widget you created earlier
canv.create_window(50, 50)

root.mainloop()