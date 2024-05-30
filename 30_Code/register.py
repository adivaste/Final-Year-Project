import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
import re
import random

# Function to check password strength
def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True
    
    if len(passwd) < 6:
        ms.showinfo('Password Strength', 'Password should be at least 6 characters long.')
        val = False
        
    if len(passwd) > 20:
        ms.showinfo('Password Strength', 'Password should not be greater than 20 characters long.')
        val = False
        
    if not any(char.isdigit() for char in passwd):
        ms.showinfo('Password Strength', 'Password should contain at least one digit.')
        val = False
        
    if not any(char.isupper() for char in passwd):
        ms.showinfo('Password Strength', 'Password should contain at least one uppercase letter.')
        val = False
        
    if not any(char.islower() for char in passwd):
        ms.showinfo('Password Strength', 'Password should contain at least one lowercase letter.')
        val = False
        
    if not any(char in SpecialSym for char in passwd):
        ms.showinfo('Password Strength', 'Password should contain at least one of the symbols $@#.')
        val = False
    
    return val

# Function to insert data into the database
def insert():
    # Extracting values from entry fields
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    pwd = password.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()

    # Password strength check
    if not password_check(pwd):
        return
    
    # Inserting data into the database
    try:
        sqliteConnection = sqlite3.connect('evaluation.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        
        # Modify the CREATE TABLE statement to include the new columns 'Share1' and 'Text'
        cursor.execute('CREATE TABLE IF NOT EXISTS registration (Fullname TEXT, address TEXT, username TEXT, password TEXT, Email TEXT, Phoneno TEXT, Gender TEXT, age TEXT, Share1 BLOB, Text TEXT)')
        
        # Executing the insertion query
        cursor.execute('INSERT INTO registration (Fullname, address, username, password, Email, Phoneno, Gender, age) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (fname, addr, un, pwd, email, mobile, gender, time))
        sqliteConnection.commit()
        print("Data inserted successfully into the table")
        
        # Close cursor and connection
        cursor.close()
        sqliteConnection.close()
        print("SQLite connection closed")
        
        # Destroy the window after successful registration
        window.destroy()
        
        # Call the main GUI script
        from subprocess import call
        call(["python", "gui_main.py"])
        
    except sqlite3.Error as error:
        print("Failed to insert data into SQLite table:", error)
        ms.showerror('Error!', 'Failed to insert data into SQLite table')
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

# Main Tkinter window
window = tk.Tk()
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
window.title("REGISTRATION FORM")
window.configure(background="skyblue")

# Variables for entry fields
Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()

# Frame for the registration form
frame = tk.LabelFrame(window, text="", width=550, height=650, bd=5, font=('Plus Jakarta Sans', 14, ' bold '))
frame.place(relx=0.5, rely=0.55, anchor="center")

# Registration Form title
lbl = tk.Label(window, text="Registration Form", font=("Plus Jakarta Sans", 28, "bold"), fg="red")
lbl.place(relx=0.5, rely=0.067, anchor="center")

# Labels and Entry Widgets
labels = ["Full Name:", "Address:", "E-mail:", "Phone number:", "Gender:", "Age:", "User Name:", "Password:"]
entry_vars = [Fullname, address, Email, Phoneno, None, age, username, password]

for i, label_text in enumerate(labels):
    if label_text == "Gender:":
        tk.Label(frame, text=label_text, width=12, font=("Plus Jakarta Sans", 15, "bold"), bg="antiquewhite2").grid(row=i, column=0, pady=5, padx=5)
        tk.Radiobutton(frame, text="Male", padx=5, width=5, bg="antiquewhite2", font=("bold", 15), variable=var, value=1).grid(row=i, column=1)
        tk.Radiobutton(frame, text="Female", padx=20, width=4, bg="antiquewhite2", font=("bold", 15), variable=var, value=2).grid(row=i, column=2)
    else:
        tk.Label(frame, text=label_text, width=12, font=("Plus Jakarta Sans", 15, "bold"), bg="antiquewhite2").grid(row=i, column=0, pady=10, padx=30)
        tk.Entry(frame, textvar=entry_vars[i], width=20, font=('', 15), bd=5).grid(row=i, column=1, columnspan=2, padx=30)

# Register button
btn = tk.Button(frame, text="Register", bg="red", font=("SF Pro Display", 18), fg="white", width=10, height=1, command=insert)
btn.grid(row=len(labels) + 1, column=0, columnspan=3, pady=2)

window.mainloop()
