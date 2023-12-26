from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title("MUDRIK MOHD IDDI")
def mysaa():
    saa.config(text=strftime(f"""
%H:%M:%S %p
%A
{"MUDRIK MOHD IDDI"}
"""))
    saa.after(1000,mysaa)
saa=Label(root,font=("digital",60),background="black",foreground="yellow")
saa.pack(anchor="ne")
mysaa()
mainloop()
               
