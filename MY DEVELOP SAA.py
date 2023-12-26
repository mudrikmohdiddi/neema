
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Fasil's Digital Clock")

def time():

    st = strftime(f'''
%A
%H:%M:%S %p
{"MUDRIK MOHD IDDI"}''')
    
    k.config(text = st)
    k.after(1000, time)
    
k = Label(root, font = ("open_24_display_st", 50), background = "pink", foreground = "cyan")
k.pack(anchor = 'center')
time()
mainloop()


