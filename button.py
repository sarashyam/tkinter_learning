from tkinter import *
import tkinter.messagebox as msg

root= Tk()
root.geometry("900x600")

Label(text="CUTE CUTE", bg="blue", font="sanserif 20 bold").pack(fill=X)
Label(text="verify",bg="lightblue", font="sanserif 10 bold").pack(fill=X)
Label().pack()
Label(text="How much cute are YOU? ").pack()

cvar = StringVar()
# cvar.set("radio")

def cfun():
    msg.askyesno("CUTIE PIE", "Are u sure ?")
    msg.askyesno("CUTIE PIE","Are you damn sure ?")
    msg.showinfo("CUTIE PIE", f" Maybe you are {cvar.get()}.... But YOU mean the WORLD for ME , my LOVE")
    

cute = ["SUPER CUTE", "ULTRA CUTE", "LITTLE BIT CUTE", " CUTEST" ]

for x in cute:
    radio = Radiobutton(root, text=f"{x}", value=f"{x}", variable=cvar, bg="pink").pack(anchor="nw", fill=X)

Button(root, text="LET'S SEE", command=cfun).pack()
root.mainloop()
