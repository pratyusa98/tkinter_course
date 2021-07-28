# 1. Geometry
# 2. Label
#3. Maxsize & Minsize

from tkinter import *

root = Tk()

# geometry("W x H")
root.geometry("500x300")

#fix the size
#width,height
root.minsize(500,300)
root.maxsize(500,300)

#label
mylabel = Label(text="Hello Tkinter")

mylabel.pack()

root.mainloop()