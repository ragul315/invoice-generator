import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import subprocess

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Connect to the database (you need to adjust the connection parameters)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="asdf",
        database="billing"
    )
    mycursor = mydb.cursor()

    
    try:
        mycursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = mycursor.fetchone()

        if user:
            open_home_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to the database: {err}")

def open_home_page():
    login_window.destroy()  
    subprocess.run(["python", "home_page.py"])


login_window = tk.Tk()
login_window.title("Login Page")


window_width = 300
window_height = 200
screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
login_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = ttk.Frame(login_window, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(frame, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_username = ttk.Entry(frame)
entry_username.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(frame, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_password = ttk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

ttk.Button(frame, text="Login", command=login).grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky="ew")


login_window.mainloop()
