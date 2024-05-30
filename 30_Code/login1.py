import os 
import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from pkg_resources import parse_version
from sendEmail import send_email
from temo.renegerate_image import generate_image
from temo.split import encrypt_split_image
from temo.regenerate import reconstruct_image


if parse_version(Image.__version__) >= parse_version('10.0.0'):
    Image.ANTIALIAS = Image.LANCZOS

root = tk.Tk()
root.configure(background="#BFEFFF")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login Form")

# Background Image
image2 = Image.open('log1.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

username = tk.StringVar()
password = tk.StringVar()


def show(some):
    global file
    file = askopenfilename(initialdir=r'', title='Select Image',
                           filetypes=[("all files", "*.*")])

    image3 = Image.open(file)
    image3 = image3.resize((450, 280), Image.ANTIALIAS)
    print(file)
    return file


def registration():
    root.destroy()
    from subprocess import call
    call(["python","register.py"])


def login():
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()
        db = sqlite3.connect('evaluation.db')
        cursor = db.cursor()
        db.commit()
        find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
        c.execute(find_entry, [(username.get()), (password.get())])
        result = c.fetchall()
        print((username.get()))

        if result:
            msg = ""
            for element in result:
                id1 = element[0]
            print(id1)
            with open("user.txt", "w") as f:
                f.write(str(id1))
            root.destroy()
        else:
            messagebox.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

def reconstruct_image_from_user(self):

    username = txtuser.get()
    file_path = txtbrowse.get()
    
    reconstruct_status = reconstruct_image(f"{username}_part1.png", file_path, f"{username}_output.png")
    if(reconstruct_status == 0):
        print("Wrong image, upload the current one !")


    try:
        image = Image.open(f"{username}_output.png")

        # Convert the Image object into a Tkinter PhotoImage object
        image = image.resize((250, 150)) 
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        image_label = tk.Label(Login_frame, image=photo)
        image_label.image = photo  # Retain reference to the image to avoid garbage collection
        
        # Place the label on the window
        image_label.grid(row=2, column=3, columnspan=2, padx=10, pady=10)

    except:
        print("Wrong image, upload the current one !")


# Store the text in database
def store_secret_text_database(secret_text, username):
    
    # Connect to the database
    conn = sqlite3.connect('evaluation.db')
    cursor = conn.cursor()

    # Insert share1 and text into the database
    cursor.execute("UPDATE registration SET text = ? WHERE username = ?", (secret_text, username))
    print("stored into database")

    # Commit changes and close connection
    conn.commit()
    conn.close()

def enter_function(self):
        username = txtuser.get()

        # Get the user from the database
        conn = sqlite3.connect('evaluation.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM registration WHERE username = ?", (username,))

        userObj = cursor.fetchone()
        if (userObj is None):
            messagebox.showerror('Oops!', 'Username not Found/Match.')
            return

        # clear local images before generation
        try:
            os.remove(f"{username}_output.png")
        except FileNotFoundError:
            pass

        try:
            os.remove(f"{username}_part1.png")
        except FileNotFoundError:
            pass

        try:
            os.remove(f"{username}_part2.png")
        except FileNotFoundError:
            pass

        try:
            os.remove(f"{username}.png")
        except FileNotFoundError:
            pass


        text = generate_image(username)
        store_secret_text_database(text, username)
        encrypt_split_image(f"{username}.png", f"{username}_part1.png", f"{username}_part2.png")
        send_email("vasteadi45@gmail.com", "Sample Title", "How are you brother !", f"{username}_part2.png")
        messagebox.showinfo("Message", "Image sent to email successfully !")

def browse_image():
    # Open file dialog to select image file
    file_path = filedialog.askopenfilename()

    # Set the selected file path to the image entry field
    txtbrowse.delete(0, tk.END)
    txtbrowse.insert(0, file_path)

    # generate_text_image(self.username_entry.get())

def retrieve_share_and_text_from_database(username):
    # Connect to the database
    conn = sqlite3.connect('evaluation.db')
    cursor = conn.cursor()

    # Retrieve share1 and text from the database based on the username
    cursor.execute("SELECT text FROM registration WHERE username = ?", (username,))
    print(username)
    original_text = cursor.fetchone()

    # Close connection
    conn.close()

    return original_text


def login():
    # Get username and text from entry widgets
    username = txtuser.get()
    text = txtpass.get()

    # Call login function
    loginMain(username, text, Login_frame)

def loginMain(username, entered_text, window):
    # Retrieve share1 and text from the database based on the username
    original_text = retrieve_share_and_text_from_database(username)
    print(original_text, entered_text)

    # Compare entered_text with the original text
    if entered_text == original_text[0]:
        # Provide login access
        messagebox.showinfo("Login Successful", "You have been logged in successfully.")
        # Place your code to proceed after successful login here
        os.chdir('./visual_cryptography_final_1')
        os.system("python ./GUI_master.py")

        # window.destroy()
    else:
        # Deny access
        messagebox.showerror("Login Failed", "Invalid username or text entered. Please try again.")


bg_icon = ImageTk.PhotoImage(file=r"L.jpg")
user_icon = ImageTk.PhotoImage(file=r"l1.png")
pass_icon = ImageTk.PhotoImage(file=r"p1.jpg")

title = tk.Label(root, text="Login Here", font=("Plus Jakarta Sans", 30, "bold"), bd=5, padx=10)
title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

Login_frame = tk.Frame(root, bg="black", bd=10, relief=tk.GROOVE)
Login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

logolbl = tk.Label(Login_frame, image=bg_icon, bd=0)
logolbl.grid(row=0, columnspan=2, pady=20)

lbluser = tk.Label(Login_frame, text="Username  ", image=user_icon, compound=tk.LEFT, font=("Plus Jakarta Sans", 20, "bold"),
                   bg="white")
lbluser.grid(row=1, column=0, padx=20, pady=10)
txtuser = tk.Entry(Login_frame, bd=5, textvariable=username, font=("", 15))
txtuser.grid(row=1, column=1, padx=20)
txtuser.bind("<Return>", enter_function)


lblbrowse = tk.Button(Login_frame, text="Browse     ", image=pass_icon, compound=tk.LEFT, command=browse_image, height=40,
                   font=("Plus Jakarta Sans", 20, "bold"), bg="white")
lblbrowse.grid(row=2, column=0, padx=50, pady=0)
txtbrowse = tk.Entry(Login_frame, bd=5,  font=("", 15))
txtbrowse.grid(row=2, column=1, padx=20)
txtbrowse.bind("<Return>", reconstruct_image_from_user)



lblpass = tk.Label(Login_frame, text="Enter text ", image=pass_icon, compound=tk.LEFT,
                   font=("Plus Jakarta Sans", 20, "bold"), bg="white")
lblpass.grid(row=3, column=0, padx=50, pady=10)
txtpass = tk.Entry(Login_frame, bd=5, font=("", 15))
txtpass.grid(row=3, column=1, padx=20)


btn_log = tk.Button(Login_frame, text="Submit", command=login, width=15, font=("Plus Jakarta Sans", 14, "bold"),
                    bg="Green", fg="black")
btn_log.grid(row=4, column=1, pady=10)

btn_reg = tk.Button(Login_frame, text="Create Account", command=registration, width=15,
                    font=("Plus Jakarta Sans", 14, "bold"), bg="red", fg="black")
btn_reg.grid(row=4, column=0, pady=10)


root.mainloop()
