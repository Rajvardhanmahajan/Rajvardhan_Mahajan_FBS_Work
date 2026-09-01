# Import Tkinter library
import tkinter as tk

# Import messagebox for displaying popup messages
from tkinter import messagebox


# Function to check username and password
def login():

    # Get username entered by the user
    username = username_entry.get()

    # Get password entered by the user
    password = password_entry.get()

    # Check username and password
    if username == "admin" and password == "1234":

        # Display success message
        messagebox.showinfo("Login", "Login Successful!")

    else:

        # Display error message
        messagebox.showerror("Login", "Invalid Username or Password!")


# Create the main window
window = tk.Tk()

# Set window title
window.title("Login System")

# Set window size
window.geometry("300x200")


# Create Username label
tk.Label(window, text="Username").pack(pady=5)

# Create entry box for username
username_entry = tk.Entry(window)
username_entry.pack()


# Create Password label
tk.Label(window, text="Password").pack(pady=5)

# Create entry box for password
# show="*" hides the entered password
password_entry = tk.Entry(window, show="*")
password_entry.pack()


# Create Login button
# command=login calls login() function when button is clicked
tk.Button(window, text="Login", command=login).pack(pady=15)


# Keep the GUI window running
window.mainloop()