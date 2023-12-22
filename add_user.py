import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def add_user():
    username = entry_username.get()
    password = entry_password.get()

    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="asdf",
        database="billing"
    )
    mycursor = mydb.cursor()

    # Insert the new user into the database
    try:
        mycursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mydb.commit()
        messagebox.showinfo("User Added", "User added successfully.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error adding user: {err}")

# Create the main window for adding a user
add_user_window = tk.Tk()
add_user_window.title("Add User")

# Set the initial window size and position
window_width = 300
window_height = 150
screen_width = add_user_window.winfo_screenwidth()
screen_height = add_user_window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
add_user_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a menu bar
menu_bar = tk.Menu(add_user_window)
add_user_window.config(menu=menu_bar)

# Create File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=add_user_window.destroy)

# Create and place the widgets in the frame
frame = ttk.Frame(add_user_window, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(frame, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_username = ttk.Entry(frame)
entry_username.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(frame, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_password = ttk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

ttk.Button(frame, text="Add User", command=add_user).grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

# Start the main event loop for adding a user
add_user_window.mainloop()
