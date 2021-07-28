from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("My Title For Gui")

# important label options
# 1. text
# 2. bd - background
# 3. fg - foreground
# 4. font - set font
# 5. padx,pady
# 6. relief - border style - SUNKEN, RAISED,GROOVE,RIDGE

title_label = Label(text="""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
\nLorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown
\nprinter took a galley of type and scrambled it to make a type specimen book.
\nIt has survived not only five centuries,but also the leap into electronic typesetting, 
\nremaining essentially unchanged.
""", bg='red',fg='white',padx=23,pady=80,font=20,
                    borderwidth=3,relief=GROOVE)

#importnat pack option
# 1. anchor - northwest(nw),ne,se,sw
# 2. side - top,bottom,left,right
# 3. fill
# 4. padx,pady


title_label.pack(side=BOTTOM,anchor='sw',fill=X)
root.mainloop()