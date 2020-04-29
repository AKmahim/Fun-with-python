from tkinter import *

def data():
    global d;
    

window = Tk()
window.geometry('350x200')

window.title("Wecome to Bangladesh")

lb1 = Label(window,text="Hello",font=("Arial Bold",50))
lb1.grid(column=0,row=0)

def clicked():
    lb1.configure(text="Button was clicked!")


button = Button(window,text="Click Me",command=clicked)
button.grid(column=0,row=1)

window.mainloop()
