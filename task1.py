#make pycharm start screen

from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("733x434")
blank_space =" "
root.title(80*blank_space+"Welcome To Pycharm Community Edition")

image = Image.open("logo.png")
resize_image = image.resize((100,100))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)

label2 = Label(text="PyCharm",font=("Helvetica", 30))
label3 = Label(text="Version 29.1.11.25",font=("Helvetica", 10))


label4 = Label(text="Create New Project\n\nOpen\n\nCheck Out From Version Control",
               font=("Helvetica", 10), anchor="e",justify= LEFT)


bottom = Label(text="Configure   Get Help",font=("Helvetica", 10, "bold"))




label1.pack(padx=35,pady=15)
label2.pack()
label3.pack(pady=10)
label4.pack()
bottom.pack(side=BOTTOM,anchor='se',padx=35,pady=15)

root.mainloop()