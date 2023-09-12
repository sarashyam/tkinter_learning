from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w" )
        self.statusbar.pack(fill=X,side=BOTTOM)

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.mainloop()

