'''Pygame Window
Outline:
Create your first GUI window using Tkinter! Students will learn the basics of creating a graphical window,
setting its title, and defining its size. This is the foundation for building interactive desktop applications.

from tkinter import *
window= Tk()

window.title("Demo Window")
window.geometry("400x300")

window.mainloop()'''


'''Getting started with widgets Outline: 
Create an interactive GUI application using Tkinter that greets users by name and displays today's date! 
Students will learn to build windows, add widgets, handle button clicks, and display dynamic messages in a 
text box'''

from tkinter import *
from datetime import date

root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

lbl = Label(text = "Hey There!",fg = "white",bg = "#072F5F", height = 1, width = 30)
name_lbl = Label(text = "Full Name", bg = "#3895D3")
name_entry = Entry()
def display():
    name = name_entry.get()
    global message
    message = "Welcome to the application!\nToday's date is : "
    greet = "Hello"+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())



text_box = Text(height=-3)
btn = Button(text = "Begin",command = display, height = 1, bg = "#1261A0", fg = "White")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()


