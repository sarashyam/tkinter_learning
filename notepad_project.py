from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file  # The file var we created in main to make it accesseble
    root.title("untitle - notepad")
    file = None  # to set nothing is there
    textArea.delete(1.0, END)  # 1.0 means first line and zeroth character, from 1.0 remove till end


def openFile():
    global file
    # to make default extension as 'txt' ,
    # filetypes show what kind of files can be opened, all files and types can be opened *.*
    # text documents which are .txt format can be opened

    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == " ":  # if there is nothing in file
        file = None
    else:  # if something is in file and can be opened 
        root.title(
            os.path.basename(file) + " - Notepad")  # Getting the path and the filename and concat text - Notepad
        textArea.delete(1.0, END)  # deleting whatever was written on the file
        f = open(file, "r")  # opening the file in read and write mode
        textArea.insert(1.0, f.read())  # inserting the file items from 1st line and 0th character
        f.close()  # closing the file once it is done

# to save a file ***********************

def saveFile():
    global file
    if file == None:  # when it's a new file
        file = asksaveasfilename(initialfile='Untitled',
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":  # if no file is being selected
            file = None
        else:  # save as a new file
            f = open(file, "w")  # open in write mode
            f.write(textArea.get(1.0, END))  # writing in 1st line 0th char
            f.close()

            root.title(os.path.basename(file) + "- Notepad") # to change the title to new file name that is saved
            print("file saved")
    else:  # if file already exists then it is replaced with the new one
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()


def copyFile():
    textArea.event_generate(("<<Copy>>"))  # automatically handled by tkinter itself


def cutFile():
    textArea.event_generate(("<<Cut>>"))  # automatically handled by tkinter itself


def pasteFile():
    textArea.event_generate(("<<Paste>>"))  # automatically handled by tkinter itself


def about():
    showinfo("Notepad by Saradha", "This is a notepad by Saradha")


if __name__ == "__main__":
    root = Tk()
    # scrollbar = Scrollbar(root)
    # scrollbar.pack(side=RIGHT, fill=Y)
    root.geometry("600x300")
    root.title("Untitled -- file")
    root.configure(background="pink")
    root.wm_iconbitmap("watermelon.ico")  # icon of the notepad

    # To create a text area
    textArea = Text(root, font="sanserif 15", background="pink", fg="green")
    file = None  # To show no files are open
    textArea.pack(expand=True, fill=BOTH)  # to expand till how the window is

    # scrollbar.config(command=textArea.yview)

    # To create the menu
    mainMenu = Menu(root, tearoff=0)

    # To create file menu
    fileMenu = Menu(mainMenu, tearoff=0)

    # To add it's elements
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quit)
    mainMenu.add_cascade(label="File", menu=fileMenu)
    # root.config(menu=mainMenu)
    # ************

    # edit menu*******
    editMenu = Menu(mainMenu, tearoff=0)
    editMenu.add_command(label="Cut", command=cutFile)
    editMenu.add_command(label="Copy", command=copyFile)
    editMenu.add_command(label="Paste", command=pasteFile)
    mainMenu.add_cascade(label="Edit", menu=editMenu)
    # root.config(menu=mainMenu)
    # ************
    # help menu ***********
    helpMenu = Menu(mainMenu, tearoff=0)
    helpMenu.add_command(label="About", command=about)
    mainMenu.add_cascade(label="Help", menu=helpMenu)
    root.config(menu=mainMenu)

    Scroll = Scrollbar(textArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
