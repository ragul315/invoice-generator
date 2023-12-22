import tkinter as tk
from tkinter import ttk
import subprocess

def open_invoice_generator():
    subprocess.run(["python", "invoice_generator.py"])

def open_view_invoice():
    subprocess.run(["python", "view_invoice.py"])

def open_add_user():
    subprocess.run(["python", "add_user.py"])

def exit_application():
    home_window.destroy()

# Create the main window
home_window = tk.Tk()
home_window.title("Invoice Generator")

# Set the initial window size and position
window_width = 500
window_height = 350
screen_width = home_window.winfo_screenwidth()
screen_height = home_window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
home_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a frame to hold the widgets
frame = ttk.Frame(home_window, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

# Create and place the widgets in the frame
ttk.Label(frame, text="Welcome to the Invoice Generator", font=("Helvetica", 18, "bold")).grid(row=0, column=0, padx=10, pady=10)

# Set a consistent width for all buttons
button_width = 20

# Create buttons for main operations
generate_button = ttk.Button(frame, text="Generate Invoice", command=open_invoice_generator, width=button_width)
generate_button.grid(row=1, column=0, pady=10)

view_button = ttk.Button(frame, text="View Invoice", command=open_view_invoice, width=button_width)
view_button.grid(row=2, column=0, pady=10)

add_user_button = ttk.Button(frame, text="Add User", command=open_add_user, width=button_width)
add_user_button.grid(row=3, column=0, pady=10)

exit_button = ttk.Button(frame, text="Exit", command=exit_application, width=button_width)
exit_button.grid(row=4, column=0, pady=10)

# Configure grid weights to make the frame expandable
home_window.grid_rowconfigure(0, weight=1)
home_window.grid_columnconfigure(0, weight=1)

# Start the main event loop for the home page
home_window.mainloop()
