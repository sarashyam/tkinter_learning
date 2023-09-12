from tkinter import *
root = Tk()
root.geometry("400x200")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

svar = StringVar()
svar.set("Your use of this software is subject to the terms and conditions of the license agreement by which you acquired this software.  If you are a volume license customer, use of this software is subject to your volume license agreement.  You may not use this software if you have not validly acquired a license for the software from Microsoft or its licensed distributors.")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill=BOTH)
scrollbar.config(command=txt.yview)


root.mainloop()