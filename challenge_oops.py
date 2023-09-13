# This is the first time that we are learing oops in tkinter 

# so this a challenge to display a description of a custom class created by us

from tkinter import * 

class BTS(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")

    def des(self):
        self.var = StringVar()
        self.var.set("this is a a simple class which will be about bts")
        Label(self, textvariable=self.var, bg= "purple").pack(side=RIGHT)



if  __name__ == '__main__':
    w = BTS()
    w.des()
    w.mainloop()