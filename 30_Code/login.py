import io
import subprocess
import os
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2
from sendEmail import send_email
from temo.renegerate_image import generate_image
from temo.split import encrypt_split_image
from temo.regenerate import reconstruct_image
# from visual_cryptography_final_1.GUI_master import runme

# Function to handle user login
def login(username, entered_text, window):
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



# Function to retrieve share1 and text from the database
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


# GUI class for login window
class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.state('zoomed')
        self.master.configure(bg="#BFEFFF")

        # Create username label and entry widget
        self.username_label = tk.Label(self.master, text="Username:", bg="#BFEFFF", font=("Arial", 20))
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.master, font=("Arial", 20))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create username enter button to select image file
        self.browse_button = tk.Button(self.master, text="Enter", command=self.enter_function, bg="blue", fg="white", font=("Arial", 20))
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)


        # Create image file path label and entry widget
        self.image_label = tk.Label(self.master, text="Image File Path:", bg="#BFEFFF", font=("Arial", 20))
        self.image_label.grid(row=1, column=0, padx=10, pady=10)
        self.image_entry = tk.Entry(self.master, font=("Arial", 20))
        self.image_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create browse button to select image file
        self.browse_button = tk.Button(self.master, text="Browse", command=self.browse_image, bg="blue", fg="white", font=("Arial", 20))
        self.browse_button.grid(row=1, column=2, padx=10, pady=10)
        
        # Create text label and entry widget
        self.text_label = tk.Label(self.master, text="Text from Image:", bg="#BFEFFF", font=("Arial", 20))
        self.text_label.grid(row=3, column=0, padx=10, pady=10)
        self.text_entry = tk.Entry(self.master, font=("Arial", 20))
        self.text_entry.grid(row=3, column=1, padx=10, pady=10)


        # Create reconstruct button
        self.reconstruct_button = tk.Button(self.master, text="Reconstruct Image", command=self.reconstruct_image_from_user, bg="orange", fg="white", font=("Arial", 20))
        self.reconstruct_button.grid(row=2, columnspan=3, pady=10)

        # Create login button
        self.login_button = tk.Button(self.master, text="Login", command=self.login, bg="green", fg="white", font=("Arial", 20))
        self.login_button.grid(row=4, columnspan=3, pady=10)

    def browse_image(self):
        # Open file dialog to select image file
        self.file_path = filedialog.askopenfilename()
        # Set the selected file path to the image entry field
        self.image_entry.delete(0, tk.END)
        self.image_entry.insert(0, self.file_path)

        # generate_text_image(self.username_entry.get())

    def enter_function(self):
        self.username = self.username_entry.get()

        # clear local images before generation
        try:
            os.remove(f"{self.username}_output.png")
        except FileNotFoundError:
            pass

        try:
            os.remove(f"{self.username}_part1.png")
        except FileNotFoundError:
            pass

        try:
            os.remove(f"{self.username}_part2.png")
        except FileNotFoundError:
            pass

        try:
            os.remove(f"{self.username}.png")
        except FileNotFoundError:
            pass


        text = generate_image(self.username)
        store_secret_text_database(text, self.username)
        encrypt_split_image(f"{self.username}.png", f"{self.username}_part1.png", f"{self.username}_part2.png")
        send_email("vasteadi45@gmail.com", "Sample Title", "How are you brother !", f"{self.username}_part2.png")


    def reconstruct_image_from_user(self):
        
        reconstruct_status = reconstruct_image(f"{self.username}_part1.png", self.file_path, f"{self.username}_output.png")
        if(reconstruct_status == 0):
            print("Wrong image, upload the current one !")


        try:
            image = Image.open(f"{self.username}_output.png")

            # Convert the Image object into a Tkinter PhotoImage object
            image = image.resize((250, 150)) 
            photo = ImageTk.PhotoImage(image)

            # Create a label to display the image
            image_label = tk.Label(self.master, image=photo)
            image_label.image = photo  # Retain reference to the image to avoid garbage collection
            
            # Place the label on the window
            image_label.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

        except:
            print("Wrong image, upload the current one !")
        
        
    # Function to handle login button click
    def login(self):
        # Get username and text from entry widgets
        username = self.username_entry.get()
        text = self.text_entry.get()

        # Call login function
        login(username, text, self.master)

# Main function to run the GUI
def main():
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()