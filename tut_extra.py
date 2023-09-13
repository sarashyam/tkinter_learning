#  This contains some extra methods/functions that we didn't learn before 

from tkinter import *

root = Tk()
root.geometry("600x300")

# Used to set a title to the window
root.title("Watermelon.............")

# Used to set a icon to the window
root.wm_iconbitmap("watermelon.ico")

# Used to know the screens height and width 
h = root.winfo_screenheight()
w = root.winfo_screenmmwidth()
print(f"width {w} x height {h}")

# Used to configure the whole window
root.configure(background="red")

# Used to destroy the root window
Button(text="Destroyer", command=root.destroy, bg="green", font="sanserif 15 bold").pack(side=BOTTOM)


root.mainloop()