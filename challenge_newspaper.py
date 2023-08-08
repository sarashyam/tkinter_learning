# This is a demo newspaper lot of modifications to be done 
# but this is just a dummy newspaper style

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title(" NewsPaper Challenge")
root.geometry("900x600")

# creating a function to break in each 100 characters
def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i%100==0 and i!=0:
            final_text +="\n"
    return final_text


texts = []  # to store the text data
photos = []  # to store the photos

# for looping through text and photo files
for i in range(0, 2):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")
    image = image.resize((100, 100))



    photos.append(ImageTk.PhotoImage(image))


f0 = Frame(root, width=800, height=100)
f1 = Frame(root, width=800, height=100)
f2 = Frame(root, width=800, height=100)
f0.pack()

f2.pack()


# for main heading
Label(f0, padx=30, pady=30, text="This is the main Headline", font="sanserif 30 bold").pack()
Label(f0, text="this is the date ").pack()

# for inner news
Label(f1, text=texts[0], padx=30, pady=30).pack(side=LEFT)
# for image
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(fill=X, padx=30, pady=30)

Label(f2, text=texts[1], padx=30, pady=30).pack(side=LEFT)
# for image
Label(f2, image=photos[1], anchor="e").pack()
f2.pack(fill=X, padx=30, pady=30)




root.mainloop()
