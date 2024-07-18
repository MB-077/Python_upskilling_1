from tkinter import *

def display():
    print("Button clicked")
    
root = Tk()
root.geometry("300x300")
hello = Label(root, text="Hello, world!", fg="red", bg="white", font=("Arial", 36))
hello.pack()
button = Button(root, text="Click here", command=display)
button.pack()
root.mainloop()