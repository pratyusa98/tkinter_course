from tkinter import *

root = Tk()
root.geometry("655x333")
f1 = Frame(root,bg="gray")

f1.pack(side=TOP)

l = Label(f1,text="1st Frame")
l.pack()

root.mainloop()