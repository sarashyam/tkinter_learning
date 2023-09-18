from tkinter import *
root = Tk()

def click(event):
    global scvalue
    t = event.widget.cget("text")
    print(t)
    if t == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"
                print(e)
                scvalue.set(value)
                screen.update()


        scvalue.set(value)
        screen.update()
        
    elif t == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + t)
        screen.update()

# ***************************************

root.geometry("200x450")
root.title("calculator")
root.maxsize(380,700)
root.wm_iconbitmap("calculator_icon.ico")
root.configure(background="grey")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="sanserif 30 bold", relief=SUNKEN, borderwidth="5")
screen.pack(fill=X, ipadx = 25, pady=10, padx=5)


f = Frame(root, border=5, relief=SUNKEN)
b = Button(f, text="9", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

b = Button(f, text="8", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

b = Button(f, text="7", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

f.pack(fill=X, padx=5, pady=5)


# ***********
f = Frame(root, border=5, relief=SUNKEN)
b = Button(f, text="6", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

b = Button(f, text="5", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

b = Button(f, text="4", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

f.pack(fill=X, padx=5, pady=5)

# ********
f = Frame(root, border=5, relief=SUNKEN)
b = Button(f, text="3", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

b = Button(f, text="2", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

b = Button(f, text="1", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

f.pack(fill=X, padx=5, pady=5)

# ***********

f = Frame(root, border=5, relief=SUNKEN)
b = Button(f, text="0", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

b = Button(f, text="+", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

b = Button(f, text="-", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

f.pack(fill=X, padx=5, pady=5)

# ********
f = Frame(root, border=5, relief=SUNKEN)
b = Button(f, text="*", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

b = Button(f, text="/", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

b = Button(f, text="%", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

f.pack(fill=X, padx=5, pady=5)

# ********

f = Frame(root, border=5, relief=SUNKEN)
b = Button(f, text="C", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

b = Button(f, text="=", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

b = Button(f, text=".", font="sanserif 12 bold", width=5)
b.pack(padx= 5 , pady=5, side=LEFT)
b.bind('<Button-1>', click)

f.pack(fill=X, padx=5, pady=5)

# b.bind("<Button-1>", click)
# for i in range(1,4):
#     x = i * 3
#     for j in range(3):
#         b = Button(f, text=f"{x}", font="sanserif 10 bold").pack(padx= 5 , pady=5 , side=LEFT)
#         x-=1
 

root.mainloop()