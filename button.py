from tkinter import *
import tkinter.messagebox as msg

root= Tk()
root.geometry("900x600")

def cfun():
    msg.askyesno("CUTIE PIE", "Are u sure ?")
    msg.askyesno("CUTIE PIE","Are you damn sure ?")
    msg.showinfo("CUTIE PIE", f" Maybe you are {cvar.get()}.... But YOU mean the WORLD for ME , my LOVE")


def c_roll():
    msg.showwarning("Rolling WARNING", "NOW YOU ARE TRYING TO ROLL LIKE A CAT")


def c_eyes():
    msg.showwarning("Cute WARNING", " WARNING::: YOU ARE LOOKING AND SMILING IN A CUTE WAY")

mainmenu = Menu(root)
# mainmenu.add_command(label="cute habits", command=cfun)
# mainmenu.add_command(label="cute clothes", command=cfun)
c_habbit_menu = Menu(mainmenu,tearoff=0)
c_habbit_menu.add_command(label="rolling in a cute way ", command=c_roll)
c_habbit_menu.add_command(label="Making big eyes and a cute smile", command=c_eyes)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Cute Habits", menu=c_habbit_menu)



Label(text="CUTE CUTE", bg="blue", font="sanserif 20 bold").pack(fill=X)
Label(text="verify",bg="lightblue", font="sanserif 10 bold").pack(fill=X)
Label().pack()
Label(text="How much cute are YOU? ").pack()

cvar = StringVar()
cvar.set("CUTEST")


    

cute = ["SUPER CUTE", "ULTRA CUTE", "LITTLE BIT CUTE", "CUTEST" ]

for x in cute:
    radio = Radiobutton(root, text=f"{x}", value=f"{x}", variable=cvar, bg="pink", justify=LEFT).pack(fill=X)


Button(root, text="LET'S SEE", command=cfun).pack()
root.mainloop()
