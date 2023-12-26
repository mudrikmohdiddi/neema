from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title("MUDRIK MOHD IDDI")
def nn():
    a="""***   *                                 START                                             












"""
    b=""" ***  *                                                                                   












"""
    c="""   ****                                                                                   










"""
    d="""     ****                                                                                  

*            *                                *










                                                                      
"""
    e="""                                                                                                                
                      **
*                      *
           *           *
                       *









                                                                        
"""
    f="""                                                                                                           
*
           *
                *****









           
"""
    g="""                                                                                            
*           *
            *****










"""
    h="""                                                                                           
*     ****
         **         










"""
    j="""                                                                                          
*******             FINISH










"""
    k=f"""                                                                                         
{("*"+"     ")*8}
{("*"+"     ")*8}
{("*"+"     ")*8}
{("*"+"     ")*8}
{("*"+"     ")*8}
{("*"+"     ")*8}
{("*"+"     ")*8}
{("*"+"     ")*8}
{("*"+"     ")*8}

"""
    t=strftime("%S")
    p=int(t)
    if(p==1 or p==11 or p==21 or p==31 or p==41 or p==51):
        u=a
    elif(p==2 or p==12 or p==22 or p==32 or p==42 or p==52):
        u=b
    elif(p==3 or p==13 or p==23 or p==33 or p==43 or p==53):
        u=c
    elif(p==4 or p==14 or p==24 or p==34 or p==44 or p==54):
        u=d
    elif(p==5 or p==15 or p==25 or p==35 or p==45 or p==55):
        u=e
    elif(p==6 or p==16 or p==26 or p==36 or p==46 or p==56):
        u=f
    elif(p==7 or p==17 or p==27 or p==37 or p==47 or p==57):
        u=g
    elif(p==8 or p==18 or p==28 or p==38 or p==48 or p==58):
        u=h
    elif(p==9 or p==19 or p==29 or p==39 or p==49 or p==59):
        u=j
    elif(p==10 or p==20 or p==30 or p==40 or p==50 or p==0):
        u=k

    jina.config(text=strftime(f"""%S
{u}"""))
    jina.after(1000,nn)
jina=Label(root,font=("digital",45),background="blue",foreground="yellow")
jina.pack(anchor="nw")
nn()
mainloop()
