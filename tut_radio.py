# This code display some BTS members name and gives a choice to select and then displays a message box

from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("900x600")

Label(root, text="BTS - Bangtan Suneondan", font="sanserif 25 bold", bg="purple").pack(fill=X)
Label(root, text="Favourite member of BTS", fg="purple", font="sanserif 15 italic").pack()


def love():
    msg.showinfo("loveeeee", f" I love {var.get()} tooo , Saranghae")


var = StringVar()  # this will get the value that we submitted in the radio
var.set("radio")

bl = ["rm", "jin", "suga", "j-hope"]

for i in range(len(bl)):
    radio = Radiobutton(root, text=f"{bl[i]}", variable=var, value=f"{bl[i]}", font="sanserif 15 italic", pady=20).pack(
        anchor="w")

Button(root, text="Aigesso", command=love, padx=20, bg="pink").pack(anchor="w")
# radio = Radiobutton(root, text="RM", variable=var, value=1).pack()
# radio = Radiobutton(root, text="Jin", variable=var, value=2).pack()


root.mainloop()
