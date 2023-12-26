from tkinter import *
from tkinter.ttk import *
from time import strftime
st=strftime("%A__%H:%M:%S %p")
import calendar
root=Tk()
root.title("MUDRIK MOHD IDDI")
def mysaa():
    d=strftime("%A")
    if(d==calendar.day_name[0]):
        z=f"BUSINESS MATHEMATICS   + DEVELOPMENT STUDY "
    elif(d==calendar.day_name[1]):
        z=f"INFORMATION TACHNOLOGY + ACCOUNTING"
    elif(d==calendar.day_name[2]):
        z=f"COMPUTER AMBLICATION   + COMMUNICATION SKILLS"
    elif(d==calendar.day_name[3]):
        z=f"ECONOMICS              + ACCOUNTING"
    elif(d==calendar.day_name[4]):
        z=f"BUSINESS MATHEMATICS   + COMMUNICATION SKILLS "
    elif(d==calendar.day_name[5]):
        z=f"DEVELOPMENT STUDY      + ECONOMICS"
    elif(d==calendar.day_name[6]):
        z=f"COMPUTER AMBLICATION   + INFORMATION TACHNOLOGY"
    g=0
    if(int(strftime("%S"))%2==0):
        u="""
     *       I LOVE MY FATHER
    *** 
   *****
  *******
"""
    elif(int(strftime("%S"))%2==1):
        u="""
*******     I LOVE MY MOTHER 
******* 
*******     
*******       
"""
    f=strftime("%S")
    if(int(f)%2==0):
        r="BITA/7/23/013/TZ"
    elif(int(f)%2==1):
        r="MUDRIK MOHD IDDI"
    
    saa.config(text=strftime(f"""
%A {r}
%H:%M:%S %p
{z}
{"MUDRIK MOHD IDDI"}
{u}
"""))
    saa.after(1000,mysaa)
saa=Label(root,font=("digital",45),background="blue",foreground="yellow")
saa.pack(anchor="nw")
mysaa()
mainloop()
    
            
