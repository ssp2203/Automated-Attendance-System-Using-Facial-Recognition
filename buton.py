from tkinter import *
from PIL import ImageTk, Image

app = Tk()

def do(event):
    print("Button Clicked!")
    #...

img = ImageTk.PhotoImage(Image.open("button1.png"))
button = Label(app, image = img)
button.pack()

button.bind('<Button-1>', do)
