import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
from docxtpl import DocxTemplate
from docx2pdf import convert
import os
import mysql.connector
import win32api

# Create a connection to the MySQL database (you need to provide your own credentials)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="asdf",
    database="billing"
)
mycursor = mydb.cursor()

# Create lists to store invoice items
invoicelist = []
invoicelistdb = []


def add_item():
    description = entry_description.get()
    quantity = int(entry_quantity.get())
    unit_price = float(entry_unit_price.get())
    line_total = quantity * unit_price
    invoice_item = [description, quantity, unit_price, line_total]
    tree.insert("", tk.END, values=invoice_item)
    clear_items()
    invoicelist.append(invoice_item)
    invoicelistdb.append(tuple(invoice_item))


def delete_item():
    selected_item = tree.selection()
    if selected_item:
        index = tree.index(selected_item[0])
        invoicelist.pop(index)
        invoicelistdb.pop(index)
        tree.delete(selected_item)


def clear_items():
    entry_description.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_unit_price.delete(0, tk.END)


def generate_invoice():
    if not invoicelist:
        messagebox.showerror("Error", "No items added to the invoice.")
        return

    doc = DocxTemplate("invoicetemplate.docx")
    customer_name = entry_first_name.get() + " " + entry_last_name.get()
    phone = entry_phone.get()
    subtotal = sum(item[3] for item in invoicelist)
    salestax = 0.18
    total = subtotal * (1 + salestax)

    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    doc.render({
        "date": date,
        "invoiceid": date,
        "name": customer_name,
        "phone": phone,
        "invoicelist": invoicelist,
        "subtotal": subtotal,
        "salestax": f"{salestax * 100:.2f}%",
        "total": total
    })

    docname = date + ".docx"
    doc.save(docname)

    pdfname = date + ".pdf"
    convert(docname, pdfname)

    os.remove(docname)

    mycursor.execute(
        f"CREATE TABLE invoice_{date} (sno INT AUTO_INCREMENT PRIMARY KEY, description VARCHAR(255), qty FLOAT, unitprice FLOAT, price FLOAT)")
    mycursor.executemany(
        f"INSERT INTO invoice_{date} (description, qty, unitprice, price) VALUES (%s, %s, %s, %s)", invoicelistdb)
    mydb.commit()

    try:
        win32api.ShellExecute(0, "print", pdfname, None, ".", 0)
        print_success = True
    except Exception as e:
        print_success = False
        messagebox.showerror(
            "Printing Error", "An error occurred while attempting to print the invoice.")

    if print_success:
        messagebox.showinfo("Invoice generated",
                            "Invoice generated and sent to the printer.")
    else:
        messagebox.showinfo("Invoice generated",
                            "Invoice generated as PDF. Printing is optional.")

    new_invoice()


def new_invoice():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    clear_items()
    tree.delete(*tree.get_children())
    invoicelist.clear()


# Create the main window
window = tk.Tk()
window.title("Invoice Generator")

# Set the initial window size and position
window_width = 1000
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a ttk style and set the font size for the entire application
app_style = ttk.Style(window)
app_font_size = 12
app_style.configure("TLabel", font=("TkDefaultFont", app_font_size))
app_style.configure("TEntry", font=("TkDefaultFont", app_font_size))
app_style.configure("TButton", font=("TkDefaultFont", app_font_size))

# Create a frame to hold the widgets
frame = ttk.Frame(window, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

# Configure column weights for resizing
frame.columnconfigure(1, weight=1)
frame.columnconfigure(3, weight=1)
frame.columnconfigure(4, weight=1)

# Create and place the widgets in the frame
ttk.Label(frame, text="First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_first_name = ttk.Entry(frame)
entry_first_name.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(frame, text="Last Name:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
entry_last_name = ttk.Entry(frame)
entry_last_name.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

ttk.Label(frame, text="Phone Number:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
entry_phone = ttk.Entry(frame)
entry_phone.grid(row=0, column=5, padx=5, pady=5, sticky="ew")

ttk.Label(frame, text="Description:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_description = ttk.Entry(frame)
entry_description.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(frame, text="Quantity:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
entry_quantity = ttk.Spinbox(frame, from_=1, to=100)
entry_quantity.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

ttk.Label(frame, text="Unit Price:").grid(row=1, column=4, padx=5, pady=5, sticky="e")
entry_unit_price = ttk.Spinbox(frame, from_=0.0, to=100000, increment=0.5)
entry_unit_price.grid(row=1, column=5, padx=5, pady=5, sticky="ew")

ttk.Button(frame, text="Add Item", command=add_item).grid(row=1, column=6, padx=5, pady=5, sticky="ew")

columns = ("Description", "Quantity", "Unit Price", "Total")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")
tree.column("#0", stretch=False)
for col in range(4):
    tree.column(col, stretch=True)
    tree.heading(columns[col], text=columns[col])

# Add a vertical scrollbar to the treeview
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scrollbar.grid(row=2, column=7, sticky="ns")
tree.configure(yscrollcommand=scrollbar.set)

ttk.Button(frame, text="Delete Item", command=delete_item).grid(row=3, column=0, padx=5, pady=5, sticky="ew")
ttk.Button(frame, text="Generate Invoice", command=generate_invoice).grid(row=3, column=6, padx=5, pady=5, sticky="ew")

# Start the main event loop
window.mainloop()
