from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
from pymsgbox import *

from tkinter import messagebox as ms
from PIL import Image 
from pkg_resources import parse_version
if parse_version(Image.__version__)>=parse_version('10.0.0'):
    Image.ANTIALIAS=Image.LANCZOS

root=tk.Tk()

root.title("VISUAL CRYPTOGRAPHY AUTHENTICATION SYSTEM")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

image2 =Image.open('o.jpg')
image2 =image2.resize((1587,900), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=93)


w = tk.Label(root, text="VISUAL CRYPTOGRAPHY AUTHENTICATION SYSTEM",width=60,background="skyblue",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=15)

w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="skyblue")
import random
import requests
otp = tk.IntVar()

import math
# print('Decryption Done...')
digits="0123456789"
OTP=""
for i in range(6):
      OTP+=digits[math.floor(random.random()*10)]
f = open("otp.txt", "w")
f.write(str(OTP))
f.close()
url="https://www.fast2sms.com/dev/bulk"
params={

    "authorization":"LoBtzPDeJciQwV9yMvnX6H3kUWgYqlrbu85TAEN7ZhdCFs42I1b86vnPIjEtokup7V21OM9yBxd3XcKZ",
    "sender_id":"SMSINI",
    "message":OTP,
    "language":"english",
    "route":"p",
    "numbers":"9673924688"
    }
rs=requests.get(url,params=params)
# def sms_send():
#     url="https://www.fast2sms.com/dev/bulk"
#     params={

#         "authorization":"LoBtzPDeJciQwV9yMvnX6H3kUWgYqlrbu85TAEN7ZhdCFs42I1b86vnPIjEtokup7V21OM9yBxd3XcKZ",
#         "sender_id":"SMSINI",
#         "message":OTP,
#         "language":"english",
#         "route":"p",
#         "numbers":"8956060594"
#         }
#     rs=requests.get(url,params=params)
print(OTP)
def check():
    
    f1=open("otp.txt","r")
    b1=f1.read()
    print(type(b1))
    f1.close()
    new_otp=otp.get()
    print(type(new_otp))
    print(new_otp)
    print(b1)
    if(str(new_otp)==str(b1)):
        ms.showinfo("Message", "Login Successful")
        
        root.destroy()
        from subprocess import call
        call(["python","master.py"])
        
    else:
        ms.showinfo("Message", "Login Fail")
        
    
# btn = tk.Button(root, text="Send OTP",bg="black",font=("",20),fg="white", width=15, height=1,command=sms_send)
# btn.place(x=600, y=250)    
l2 = tk.Label(root, text="Enter Your OTP :", width=40, font=("Times new roman", 15, "bold"), bg="skyblue",bd=5)
l2.place(x=600, y=300)
t1 = tk.Entry(root, textvar=otp, width=20, font=('', 15),bd=5)
t1.place(x=600, y=350)
btn = tk.Button(root, text="Submit",bg="red",font=("",20),fg="white", width=15, height=1,command=check)
btn.place(x=600, y=400)

root.mainloop()