# Code for getting user feedback and display a message box according to the rating

from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("900x600")
root.title(" RESTAURANT ")

path = "C:/Users/shyam/Desktop/git learn/rest_data.txt"




def rating():
    msg.showinfo("Thank you", f"Thank You soo much for rating us with {rate_slider.get()}, Have a good day")
    name = nameEntry.get()
    with open(path, "a") as file:
        file.write(f" {name} :")
        file.write(f" --{rate_slider.get()}. ")
        file.write("\n")



Label(root, text="HAPPY RESTAURANT ", font="sanserif 25 bold", bg="cyan").pack(fill=X)
Label(root, text="We hope you enjoyed all the moment spent in this restaurant ").pack()
Label(root, text=" We would like to know  how was it, lets us know through rating us").pack()
nameVar = StringVar()
Label(root, text="Enter your name").pack()
nameEntry = Entry(root, textvariable=nameVar)
nameEntry.pack()
rate_slider = Scale(root, from_=0, to=10, sliderrelief=GROOVE, orient=HORIZONTAL, width="20px", tickinterval=3)
rate_slider.set(6)
rate_slider.pack()

Button(root, text="submit", command=rating).pack()

root.mainloop()
