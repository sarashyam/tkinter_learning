#  This is a program that takes a name from user and stores it in a file

from tkinter import *

root = Tk()
root.geometry("600x300")

path = "C:/Users/shyam/PycharmProjects/learn_tkinter/hai"


def names():
    name = name_variable_entry.get()
    print(name)
    with open(path, "a") as file:
        file.write(name)
        file.write("\n")


# file = os.open(path, "w")
# os.write(file, name)


nameLabel = Label(root, text="enter the name", fg="blue")
nameLabel.grid(row=0, column=0)

name_variable = StringVar()
name_variable_entry = Entry(root, textvariable=name_variable)
name_variable_entry.grid(row=0, column=1)

Button(root, text="enter", bg="green", command=names).grid(row=1, column=1)

root.mainloop()
