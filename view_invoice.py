import tkinter as tk
from tkinter import ttk
import mysql.connector

def view_invoice():
    invoice_id = entry_invoice_id.get()
    
    # Retrieve invoice details from the database (you need to adjust the connection parameters)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="asdf",
        database="billing"
    )
    mycursor = mydb.cursor()

    try:
        mycursor.execute(f"SELECT * FROM invoice_{invoice_id}")
        invoice_items = mycursor.fetchall()
        display_invoice_items(invoice_items)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error retrieving invoice details: {err}")

def display_invoice_items(items):
    # Clear previous items in the treeview
    tree.delete(*tree.get_children())

    # Display new items in the treeview
    for item in items:
        tree.insert("", tk.END, values=item)

# Create the main window for viewing invoices
view_invoice_window = tk.Tk()
view_invoice_window.title("View Invoice")

# Set the initial window size and position
window_width = 1100
window_height = 400
screen_width = view_invoice_window.winfo_screenwidth()
screen_height = view_invoice_window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
view_invoice_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a frame to hold the widgets
frame = ttk.Frame(view_invoice_window, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

# Create and place the widgets in the frame
ttk.Label(frame, text="Enter Invoice ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_invoice_id = ttk.Entry(frame)
entry_invoice_id.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

ttk.Button(frame, text="View Invoice", command=view_invoice).grid(row=0, column=2, padx=5, pady=5, sticky="ew")

columns = ("SNo", "Description", "Quantity", "Unit Price", "Price")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
tree.column("#0", stretch=False)
for col in range(5):
    tree.column(col, stretch=True)
    tree.heading(columns[col], text=columns[col])

# Add a vertical scrollbar to the treeview
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scrollbar.grid(row=1, column=3, sticky="ns")
tree.configure(yscrollcommand=scrollbar.set)

# Start the main event loop for viewing invoices
view_invoice_window.mainloop()
