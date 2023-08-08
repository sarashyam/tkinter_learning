from tkinter import *

root = Tk()
root.geometry("900x600")
root.minsize(300, 100)
root.maxsize(1080, 750)


def korean():
    print("Aniyo")


def nepali():
    print("Namaste")


def chinese():
    print("NiHao")


def japanese():
    print("Konichiva")


frame1 = Frame(root, bg="yellow", borderwidth=6)
frame1.pack(side=BOTTOM, fill=X)

lablel1 = Label(frame1, text="hello in different languages", fg="green")
lablel1.pack()

b1 = Button(frame1, text="Korean", command=korean)
b1.pack(side=LEFT, anchor="nw", padx="20px", pady="20px")

b2 = Button(frame1, text="Japanese", command=japanese)
b2.pack(side=LEFT, anchor="nw", padx="20px", pady="20px")

b3 = Button(frame1, text="Chinese", command=chinese)
b3.pack(side=LEFT, anchor="nw", padx="20px", pady="20px")

b4 = Button(frame1, text="Nepali", command=nepali)
b4.pack(side=LEFT, anchor="nw", padx="20px", pady="20px")

root.mainloop()
