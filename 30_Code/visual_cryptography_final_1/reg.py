import smtplib
from email.message import EmailMessage
import imghdr

import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os
import cv2
from tkinter.filedialog import askopenfilename

window = tk.Tk()
w,h = window.winfo_screenwidth(),window.winfo_screenheight()
window.geometry("%dx%d+0+0"%(w,h))
window.title("REGISTRATION FORM")
window.configure(background="skyblue")

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
photo=tk.StringVar()
sec_key=tk.IntVar()

value = random.randint(1, 1000)
print(value)

def show():
    global file
    file = askopenfilename(initialdir=r'', title='Select Image',
                                       filetypes=[("all files", "*.*")])
    
    image3 =Image.open(file)
    image3 =image3.resize((450,280), Image.ANTIALIAS)
    print(file)
    return file

# database code
db = sqlite3.connect('evaluation.db')
# cursor = db.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS reg"
#                "(Fullname TEXT, address TEXT, username TEXT,password TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT ,photo TEXT, sec_key TEXT)")
# db.commit()


def convertToBinaryData(filename):             #We have to add image to database thats why use this function to convert image into binary format
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    pwd = password.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    photo1 = file
    sec_key1=sec_key.get()
    print(photo1)
    fin = open(photo1, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ sec_key1
    fin = open(photo1, 'wb')
    fin.write(image)
    fin.close()
    print('Encryption Done...')


    # Sender_Email = "sendmailsctcode@gmail.com"
    # Reciever_Email = "sheetal09.srccode@gmail.com"

    # Password ='ymqzpdecuqxdfosl'
    # newMessage = EmailMessage()    #creating an object of EmailMessage class
    # newMessage['Subject'] = "Encrypted Image" #Defining email subject
    # newMessage['From'] = Sender_Email  #Defining sender email
    # newMessage['To'] = Reciever_Email  #Defining reciever email

    # newMessage.set_content('Please refer the attached Encrypted image ') #Defining email body
    # with open(photo1, 'rb') as f:
    #     image_data = f.read()
    #     image_type = imghdr.what(f.name)
    #     image_name = f.name
    # newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
    #     smtp.login(Sender_Email, Password)              
    #     smtp.send_message(newMessage)
    

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif(sec_key1 == ""):
        ms.showinfo("Message", "Please Enter your 1 digit secret key")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
        
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
        
    elif((len(str(sec_key1)))<1 or len(str((sec_key1)))>1):
        ms.showinfo("Message", "Please Enter 1 digit secret code")
    
    else:
        try:
            sqliteConnection = sqlite3.connect('evaluation.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sqlite_insert_blob_query = """ INSERT INTO registration
                                      (Fullname, address, username,password, Email, Phoneno, Gender, age , photo, sec_key) 
                                      VALUES (?,?,?,?,?,?,?,?,?,?)"""

            empPhoto = convertToBinaryData(photo1)
            #resume = convertToBinaryData(resumeFile)
            # Convert data into tuple format
            data_tuple = (fname, addr,un,pwd,email,mobile,gender,time,empPhoto,sec_key1)
            cursor.execute(sqlite_insert_blob_query, data_tuple)
            sqliteConnection.commit()
            print("Image and file inserted successfully as a BLOB into a table")
            cursor.close()
            window.destroy()
            from subprocess import call
            call(["python","gui main.py"])

        except sqlite3.Error as error:
            print("Failed to insert blob data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("the sqlite connection is closed")
            

#####################################################################################################################################################

#from subprocess import call
#call(["python", "lecture_login.py"])


# assign and define variable
# def login():

#####For background Image
image2 =Image.open('v11.webp')
image2 =image2.resize((1600,850), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

frame = tk.LabelFrame(window, text="", width=550, height=650, bd=5, font=('times', 14, ' bold '),bg="#b8b8cc")
frame.grid(row=0, column=0, sticky='nw')
frame.place(x=490, y=120)

lbl = tk.Label(window, text="Registration Form", font=("Algerian", 30, "bold","italic"), bg="#b8b8cc",fg="red")
lbl.place(x=570,y=20,width=420)



#l1 = tk.Label(window, text="Registration Form", font=("Times new roman", 30, "bold"), bg="blue4", fg="red")
#l1.place(x=490, y=40)

# that is for label1 registration

l2 = tk.Label(frame, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2",bd=5)
l2.place(x=30, y=30)
t1 = tk.Entry(frame, textvar=Fullname, width=20, font=('', 15),bd=5)
t1.place(x=230, y=30)
# that is for label 2 (full name)






l3 = tk.Label(frame, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2",bd=5)
l3.place(x=30, y=80)
t2 = tk.Entry(frame, textvar=address, width=20, font=('', 15),bd=5)
t2.place(x=230, y=80)
# that is for label 3(address)


# that is for label 4(blood group)

l5 = tk.Label(frame, text="E-mail :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2")
l5.place(x=30, y=130)
t4 = tk.Entry(frame, textvar=Email, width=20, font=('', 15),bd=5)
t4.place(x=230, y=130)
# that is for email address

l6 = tk.Label(frame, text="Phone number :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2")
l6.place(x=30, y=180)
t5 = tk.Entry(frame, textvar=Phoneno, width=20, font=('', 15),bd=5)
t5.place(x=230, y=180)
# phone number
l7 = tk.Label(frame, text="Gender :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2")
l7.place(x=30, y=230)
# gender
tk.Radiobutton(frame, text="Male", padx=5, width=5, bg="antiquewhite2", font=("bold", 15), variable=var, value=1).place(x=230,
                                                                                                                y=230)
tk.Radiobutton(frame, text="Female", padx=20, width=4, bg="antiquewhite2", font=("bold", 15), variable=var, value=2).place(
    x=340, y=230)

l8 = tk.Label(frame, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2")
l8.place(x=30, y=280)
t6 = tk.Entry(frame, textvar=age, width=20, font=('', 15),bd=5)
t6.place(x=230, y=280)

l4 = tk.Label(frame, text="User Name :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2")
l4.place(x=30, y=330)
t3 = tk.Entry(frame, textvar=username, width=20, font=('', 15),bd=5)
t3.place(x=230, y=330)


l9 = tk.Label(frame, text="Secret Key :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2")
l9.place(x=30, y=425)
t8 = tk.Entry(frame, textvar=sec_key, width=20, font=('', 15), show="*",bd=5)
t8.place(x=230, y=425)

l10 = tk.Label(frame, text="Password :", width=12, font=("Times new roman", 15, "bold"),bd=5, fg="black",bg="antiquewhite2")
l10.place(x=30, y=380)
t9 = tk.Entry(frame, textvar=password, width=20, font=('', 15), show="*",bd=5)
t9.place(x=230, y=380)

l1 = tk.Button(window, text="Upload Image :", width=12, font=("Times new roman", 15, "bold"), bg="snow",command=show)
l1.place(x=700, y=600)

btn = tk.Button(frame, text="Register", bg="red",font=("",20),fg="white", width=10, height=1, command=insert)
btn.place(x=200, y=550)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
window.mainloop()