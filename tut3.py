from tkinter import *

#only for jpg not require in png

from PIL import ImageTk, Image

root = Tk()

root.geometry("500x300")

#for jpg
img = ImageTk.PhotoImage(file="col_balls.jpg")

#for png

img2 = PhotoImage(file="lambo.png")

labell = Label(image=img)
labell2 = Label(image=img2)

labell.pack()
labell2.pack()
root.mainloop()