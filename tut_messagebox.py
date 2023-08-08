# Random questions asked via a help menu and message box

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("900x600")


def file_func():
    print(" I'm in file menu")


def rate_us():
    print("I'm gonna help u")
    tmsg.showinfo("titlie-help", "hum karenge aapko help")
    result = tmsg.askquestion("title-rating", "was your experience good or not")
    print(f" ask question {result}")
    result = tmsg.askokcancel("ask ok cancel", "karoge ki nahi")
    print(f" ask ok cancel {result}")
    result = tmsg.askyesnocancel(" ask yes no cancel ", " plan work hoga ki nahi")
    print(f" ask yes no  cancel {result}")
    result = tmsg.askyesno("ask yes no ", "karoge ki naahii")
    print(f" ask yes no {result}")


def asking():
    result = tmsg.askretrycancel("u want to retry", "or you want ot cancel")
    if result:
        print("baat ban gayi")
    else:
        print("baat nahi bani")


main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="new", command=file_func)
file_menu.add_separator()
file_menu.add_command(label="open", command=file_func)
file_menu.add_command(label="save", command=file_func)
root.config(menu=main_menu)
main_menu.add_cascade(label="file", menu=file_menu)

edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label="copy", command=file_func)
edit_menu.add_separator()
edit_menu.add_command(label="paste", command=file_func)
root.config(menu=main_menu)
main_menu.add_cascade(label="edit", menu=edit_menu)

help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label="Help", command=rate_us)
help_menu.add_command(label="ask", command=asking)
main_menu.add_cascade(label="Help", menu=help_menu)
root.config(menu=main_menu)

root.mainloop()
