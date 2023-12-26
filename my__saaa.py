from tkinter import *
from tkinter.ttk import *
from time import strftime
room=Tk()
room.title("MUDRIK MOHD IDDI")
def my_saa():
    saa.config(text=strftime(f"""
%A
%H:%M:%S %p
{"MUDRIK MOHD IDDI"}"""))
    saa.after(1000,my_saa)
saa=Label(room,font=("Digital",60),background=("blue"),foreground=("black"))
saa.pack(anchor=("n"))
my_saa()
mainloop()
