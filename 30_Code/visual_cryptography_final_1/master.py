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

background_label.place(x=0, y=0)
#, relwidth=1, relheight=1)

# w = tk.Label(root, text="VISUAL CRYPTOGRAPHY AUTHENTICATION SYSTEM",width=60,background="skyblue",height=2,font=("Times new roman",19,"bold"))
# w.place(x=0,y=15)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="skyblue")




wlcm=tk.Label(root,text="......WELCOME TO VISUAL CRYPTOGRAPHY AUTHENTICATION SYSTEM ......",width=95,height=1,background="skyblue",foreground="black",font=("Times new roman",22,"bold"))
wlcm.place(x=0,y=630)





root.mainloop()