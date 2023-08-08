# This is used for creating a status bar 
# there is no default function to implement a status bar
# but it can be created with the help of label and methods

from tkinter import *
from time import sleep
root = Tk()
root.geometry("900x600")

def updating():
    statusvar.set("running")
    sbar.update()  # takes new value and updates it
    sleep(3)
    statusvar.set("all set")


statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root,textvariable=statusvar, relief=GROOVE, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="updating", command=updating).pack()

root.mainloop()