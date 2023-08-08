from tkinter import *
root = Tk()
root.geometry("900x600")

def file_func():
    print("hi this is file function")


def edit_func():
    print("this is edit function")


# ******************** for non drop down menu ********************************
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=file_func)
# mymenu.add_command(label="exit", command=quit)
# root.config(menu=mymenu)
# *****************************************************************************

# *********************** To create a tray ************************
# tearoff=0 is used to disable the menu tearing option
# add_separator is used to create separation between the menu items
main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=0)
# file_menu.add_command(label="New project", command=file_func)

# to add inner menu to file
project_menu = Menu(file_menu)
project_menu.add_command(label="new project", command=file_func())
file_menu.add_cascade(label="project ", menu=project_menu)

file_menu.add_separator()
file_menu.add_command(label="save", command=file_func)
file_menu.add_separator()
file_menu.add_command(label="print", command=file_func)

root.config(menu=main_menu)
main_menu.add_cascade(label="file", menu=file_menu)


# edit menu
edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label="copy", command=edit_func())
edit_menu.add_command(label="paste", command=edit_func())
edit_menu.add_command(label="cut", command=edit_func())
root.config(menu=main_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)

exit_menu = Menu(root)
exit_menu.add_command(label="exit", command=quit)
root.config(menu=main_menu)
main_menu.add_cascade(label="exit", menu=exit_menu)


root.mainloop()