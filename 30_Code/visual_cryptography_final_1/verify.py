
import tkinter as tk
from PIL import Image, ImageTk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os
import requests
import cv2
import qrcode
from tkinter.filedialog import askopenfilename


window = tk.Tk()
w,h = window.winfo_screenwidth(),window.winfo_screenheight()
window.geometry("%dx%d+0+0"%(w,h))
window.title("verify")
window.configure(background="#6F4E37")

key = tk.IntVar()
photo=tk.StringVar()

w = tk.Label(window, text="VISUAL CRYPTOGRAPHY AUTHENTICATION SYSTEM",width=60,background="#6F4E37",fg="white",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=15)
#####For background Image
image2 =Image.open('v1.jpg')
image2 =image2.resize((1587,735), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=90) #, relwidth=1, relheight=1)



def show():
    global file
    file = askopenfilename(initialdir=r'', title='Select Image',
                                       filetypes=[("all files", "*.*")])
    #print(file)
    #image3 =Image.open(file)
    #image3 =image3.resize((450,280), Image.ANTIALIAS)
    
    
    print(file)
    return file
def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file: # opens a file with the specified filename in write mode with binary data (the 'wb' argument).
        abc=file.write(data) # writes the data to the file.
        #return abc
    
    #print("Stored blob data into: ", filename, "\n")
    return filename  # returns the filename to the calling code.
def insert():
    photo1=file
    #print(photo1)
    key1 = key.get()
    # my_conn = sqlite3.connect('evaluation.db')
    # f1=open("user.txt","r")
    # b1=f1.read()
    # f1.close()
    # r_set=my_conn.execute("select photo from registration where id =" + str(b1) +"");
    # #print(r_set)
    
    # for row in r_set:
    #     #print("photo = ", row[0], )
    #     photo11=row[0]
        
    try:
        fin = open(photo1, 'rb') 
    # It opens a file named "photo1" in binary mode using the open() function, 
    # and reads its contents into a variable called image
        image = fin.read()
        fin.close()
        image = bytearray(image)# converts the image variable into a bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key1
        fin = open(photo1, 'wb')
        #db_image=writeTofile(photo11)
        print(type(image))
        #print(type(db_image))
        # writing decryption data in image
        fin.write(image)
        fin.close()
        
        
        window.destroy()
        from subprocess import call
        call(["python","otp.py"])
    except Exception:
        ms.showinfo("Message", "Please give correct input image or key")
    
# frame = tk.LabelFrame(window, text="", width=500, height=370, bd=5, font=('times', 14, ' bold '),bg="antiquewhite2")
# frame.grid(row=0, column=0, sticky='nw')
# frame.place(x=10, y=250)

# lbl = tk.Label(window, text="Login Form", font=('times', 35,' bold '), height=1, width=60,bg="#000080",fg="red")
# lbl.place(x=0, y=0)





l2 = tk.Label( text="Enter key :", width=14, font=("Times new roman", 15, "bold"), bd=5)
l2.place(x=550, y=250)
t1 = tk.Entry( textvar=key, width=20, font=('', 15),bd=5)
t1.place(x=800, y=250)
# that is for label 2 (full name)


l1 = tk.Button(text="Upload Image", width=12, font=("Times new roman", 15, "bold"), bg="snow",command=show)
l1.place(x=700, y=160)

btn = tk.Button( text="Submit", bg="red",font=("",20),fg="white", width=9, height=1,command=insert)
btn.place(x=700, y=300)

window.mainloop()