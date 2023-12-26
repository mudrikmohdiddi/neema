# The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit.
from tkinter import *
# The tkinter.ttk module provides access to the Tk themed widget set
from tkinter.ttk import *
# This module provides various time-related functions
from time import strftime

# Tk class is used to create a root window. Frame is a container for other widgets.
root = Tk()
# Tittle of the frame for the window
root.title("MUDRIK MOHD IDDI")


def time():

    string = strftime('%A__%H:%M:%S %p')   # time format type
    label.config(text=string)     # text will be in string
    label.after(1000, time)     # request tkinter to refresh after 1s (the delay is given in ms)


label = Label(root, font=("Digital-7", 60), background="red", foreground="cyan")     # font name- ds-digital, font size- 80, background color is black and text color is cyan.
label.pack(anchor='sw')   # Anchors are used to define where text is positioned relative to a reference point.
time()
mainloop()
