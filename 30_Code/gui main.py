from tkinter import *
import tkinter as tk
from PIL import Image ,ImageTk
from tkinter.ttk import *
from PIL import Image 
from pkg_resources import parse_version
if parse_version(Image.__version__)>=parse_version('10.0.0'):
    Image.ANTIALIAS=Image.LANCZOS


root=tk.Tk()

root.title("VISUAL CRYPTOGRAPHY AUTHENTICATION SYSTEM")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

image2 =Image.open('vv.webp')
image2 =image2.resize((1300,687), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=93)
#, relwidth=1, relheight=1)

w = tk.Label(root, text="VISUAL CRYPTOGRAPHY AUTHENTICATION SYSTEM",width=60,background="skyblue",height=2,font=("SF Pro Display",19,"bold"))
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
    call(["python","register.py"])


wlcm=tk.Label(root,text="  WELCOME TO VISUAL CRYPTOGRAPHY AUTHENTICATION SYSTEM ",width=50,height=1,background="skyblue",foreground="black",font=("Plus Jakarta Sans",25,"bold"))
wlcm.place(x=0,y=730)

d2=tk.Button(root,text="Login",command=Login,width=7,height=1,bd=0,background="skyblue",foreground="black",font=("SF Pro Display",20,"bold"))
d2.place(x=1000,y=18)

d3=tk.Button(root,text="Register",command=Register,width=10,height=1,bd=0,background="skyblue",foreground="black",font=("SF Pro Display",20,"bold"))
d3.place(x=1100,y=18)

root.mainloop()