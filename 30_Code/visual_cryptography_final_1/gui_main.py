

from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
from pymsgbox import *


root=tk.Tk()

root.title("VISUAL CRYPTOGRAPHY AUTHENTICATION SYSTEM")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

image2 =Image.open('vv.webp')
image2 =image2.resize((1587,900), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=93)
#, relwidth=1, relheight=1)

w = tk.Label(root, text="VISUAL CRYPTOGRAPHY AUTHENTICATION SYSTEM",width=60,background="skyblue",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=15)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="skyblue")


from tkinter import messagebox as ms


def Login():
    root.destroy()
    from subprocess import call
    call(["python","login.py"])
def Register():
    root.destroy()
    from subprocess import call
    call(["python","reg.py"])
    
def reg():
    root.destroy()
    from subprocess import call
    call(["python","GUI_Master.py"])

def re():
    root.destroy()
       


wlcm=tk.Label(root,text="......WELCOME TO VISUAL CRYPTOGRAPHY AUTHENTICATION SYSTEM ......",width=95,height=1,background="skyblue",foreground="black",font=("Times new roman",22,"bold"))
wlcm.place(x=0,y=730)




d2=tk.Button(root,text="Login",command=Login,width=15,height=1,bd=3,background="skyblue",foreground="black",font=("times new roman",20,"bold"))
d2.place(x=30,y=270)


d3=tk.Button(root,text="Register",command=Register,width=15,height=1,bd=3,background="skyblue",foreground="black",font=("times new roman",20,"bold"))
d3.place(x=30,y=200)

d4=tk.Button(root,text="Face Authentication",command=reg,width=15,height=1,bd=3,background="skyblue",foreground="black",font=("times new roman",20,"bold"))
d4.place(x=30,y=130)

d4=tk.Button(root,text="Exit",command=re,width=15,height=1,bd=3,background="red",foreground="black",font=("times new roman",20,"bold"))
d4.place(x=30,y=330)

root.mainloop()