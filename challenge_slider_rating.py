# Code for getting user feedback and display a message box according to the rating

from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("900x600")
root.title(" RESTAURANT ")


def rating():
    msg.showinfo("Thank you", f"Thank You soo much for rating us with {rate_slider.get()}, Have a good day")


Label(root, text="HAPPY RESTAURANT ", font="sanserif 25 bold", bg="cyan").pack(fill=X)
Label(root, text="We hope you enjoyed all the moment spent in this restaurant ").pack()
Label(root, text=" We would like to know  how was it, lets us know through rating us").pack()
rate_slider = Scale(root, from_=0, to=10, sliderrelief=GROOVE)
rate_slider.set(5)
rate_slider.pack()

Button(root, text="submit", command=rating).pack()

root.mainloop()
