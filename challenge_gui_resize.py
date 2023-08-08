# Changes the size of the gui window according to user input

from tkinter import *

root = Tk()
root.geometry("900x600")


def change_window():
    width = new_width_entry.get()
    height = new_height_entry.get()
    root.geometry(f"{width}x{height}")


Label(root, text="New width").grid(row=0, column=0)
Label(root, text="New height").grid(row=2, column=0)

new_width = StringVar()
new_height = StringVar()

new_width_entry = Entry(root, textvariable=new_width)
new_height_entry = Entry(root, textvariable=new_height)

new_width_entry.grid(row=1, column=0)
new_height_entry.grid(row=3, column=0)

Button(root, text="change GUI size", command=change_window).grid(row=5, column=0)

root.mainloop()
