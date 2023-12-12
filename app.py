import tkinter as tk
from tkinter import messagebox, Frame, Canvas, Button, Scrollbar, StringVar
import sqlite3
from PIL import Image, ImageTk
from customtkinter import *

def save_to_database(customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php, messages):
    conn = sqlite3.connect("_internal/db/water_bill_database.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS water_bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            address TEXT,
            email TEXT,
            consumption REAL,
            current_reading REAL,
            previous_reading REAL,
            meter_consumption REAL,
            bill_amount_php REAL,
            messages TEXT
        )
    ''')

    cursor.execute("PRAGMA table_info(water_bills)")
    columns = [column[1] for column in cursor.fetchall()]
    if 'messages' not in columns:
        cursor.execute("ALTER TABLE water_bills ADD COLUMN messages TEXT")


    cursor.execute('''
        INSERT INTO water_bills (
            customer_name,
            address,
            email,
            consumption,
            current_reading,
            previous_reading,
            meter_consumption,
            bill_amount_php,
            messages
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php, messages))

    conn.commit()
    conn.close()

def delete_and_clear(id):
    delete_data(id)
    bill_details_var.set("")
    
def fetch_data():
    for widget in button_frame.winfo_children():
        widget.destroy()

    conn = sqlite3.connect("_internal/db/water_bill_database.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM water_bills')
    data = cursor.fetchall()
    conn.close()
    
    for row in data:
        bill_button = CTkButton(button_frame, text=f"Customer: {row[1]}", command=lambda row=row: show_details(row))
        bill_button.pack(padx=10, pady=5)
        
def delete_data(id):
    conn = sqlite3.connect("_internal/db/water_bill_database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM water_bills WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    fetch_data()
    
root = CTk()
root.title("Water Bill - Main")
set_appearance_mode("dark")

w = 854
h = 480

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

############################################# Show Details

bill_details_var = StringVar()

details_frame = CTkFrame(root, fg_color="gray10", corner_radius=0)
details_frame.place(relx=.7, rely=0, relwidth=0.3, relheight=1, anchor='nw')

title_frame = CTkFrame(details_frame, fg_color="gray10")
title_frame.pack(padx=10, pady=5)

label_name = CTkLabel(title_frame, text="Results", font=("Oswald", 25))
label_name.grid(row=0, column=0, padx=0, pady=10)

bill_details_label = CTkLabel(details_frame, textvariable=bill_details_var, justify=tk.LEFT, font=("Helvetica", 15), 
                              bg_color="gray10", 
                              fg_color="gray10",
                              wraplength=220)
bill_details_label.pack(padx=10, pady=10)

def calculate_bill():
    try:
        customer_name = entry_name.get()[:11] if ' ' not in entry_name.get() else entry_name.get().split(' ')[0]
        address = entry_address.get()
        email = entry_email.get()
        consumption = float(entry_consumption.get())

        current_reading = float(entry_current_reading.get())
        previous_reading = float(entry_previous_reading.get())
        meter_consumption = current_reading - previous_reading
        message = ""
        
        if not email.endswith("@gmail"):
            raise ValueError("Invalid email address")
        
        bill_amount_php = meter_consumption * 2.5

        if consumption < 50:
            message = "Great job on conserving water! Keep it up."
        elif consumption < 100:
            message = "You're using a moderate amount of water. Consider more water-saving habits."
        else:
            message = "Please be mindful of your water usage. Consider implementing water-saving tips."

        save_to_database(customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php, message)
        
        fetch_data()
        
        bill_details = f"Customer Name: {customer_name}\n"
        bill_details += f"Address: {address}\n"
        bill_details += f"Email: {email}\n"
        bill_details += f"Consumption: {consumption} gallons\n\n"
        bill_details += f"Metering Information:\n"
        bill_details += f"Current Reading: {current_reading}\n"
        bill_details += f"Previous Reading: {previous_reading}\n"
        bill_details += f"Meter Consumption: {meter_consumption} gallons\n\n"
        bill_details += f"Billing Summary:\n"
        bill_details += f"Total Bill Amount (in PHP): ₱{bill_amount_php:.2f}\n\n"
        bill_details += f"Message: {message}"
        
        bill_details_var.set(bill_details)
        
    except ValueError as e:
        if str(e) == "Invalid email address":
            messagebox.showerror("Error", "Please enter a valid email address.")
        else:
            messagebox.showerror("Error", "Please enter valid numeric values for consumption and meter readings.")


def show_details(row):
    bill_details = f"Customer Name: {row[1]}\n"
    bill_details += f"Address: {row[2]}\n"
    bill_details += f"Email: {row[3]}\n"
    bill_details += f"Consumption: {row[4]} gallons\n\n"
    bill_details += f"Metering Information:\n"
    bill_details += f"Current Reading: {row[5]}\n"
    bill_details += f"Previous Reading: {row[6]}\n"
    bill_details += f"Meter Consumption: {row[7]} gallons\n\n"
    bill_details += f"Billing Summary:\n"
    bill_details += f"Total Bill Amount (in PHP): ₱{row[8]:.2f}\n\n"
    bill_details += f"Message: {row[9]}"
    
    bill_details_var.set(bill_details)
    for widget in details_frame.winfo_children():
        if isinstance(widget, CTkButton):
            widget.destroy()

    delete_button = CTkButton(details_frame, text="Delete", command=lambda id=row[0]: delete_and_clear(id))
    delete_button.pack(padx=10, pady=5)
    
#############################################

############################################# CSV Histories

conn = sqlite3.connect("_internal/db/water_bill_database.db")
cursor = conn.cursor()

cursor.execute('SELECT * FROM water_bills')
data = cursor.fetchall()

conn.close()

background_frame = CTkFrame(root, fg_color="gray11", corner_radius=0)
background_frame.place(relx=.5, rely=0, relwidth=0.2, relheight=1, anchor='nw')

title_frame = CTkFrame(background_frame, fg_color="gray11")
title_frame.pack(padx=10, pady=5)

label_name = CTkLabel(title_frame, text="Histories", font=("Oswald", 25))
label_name.grid(row=0, column=0, padx=0, pady=10)

canvas = Canvas(background_frame, bg="gray11", highlightthickness=0)
scrollbar = Scrollbar(background_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

button_frame = Frame(canvas, bg="gray11")

if data:
    for row in data:
        button_text = f"Customer: {row[1]}"
        button = CTkButton(button_frame, text=button_text, command=lambda r=row: show_details(r), font=("Oswald", 15))
        button.pack(padx=(15,10), pady=5)
else:
    messagebox.showinfo("No Data", "No water bill data found in the database.")

canvas.create_window((0, 0), window=button_frame, anchor='nw')


button_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox('all'))

canvas.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

#############################################

############################################# Register Information

background_frame = CTkFrame(root, fg_color="gray12", corner_radius=0)
background_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1, anchor='nw')

title_frame = CTkFrame(background_frame, fg_color="gray13")
title_frame.pack(padx=10, pady=5)

label_name = CTkLabel(title_frame, text="Register Information", font=("Oswald", 25))
label_name.grid(row=0, column=0, padx=0, pady=10)

name_frame = CTkFrame(background_frame)
name_frame.pack(padx=10, pady=5)

label_name = CTkLabel(name_frame, text="Customer Name:", font=("Oswald", 15))
label_name.grid(row=0, column=0, padx=53, pady=5)

entry_name = CTkEntry(name_frame, width=150)
entry_name.grid(row=0, column=1, padx=10, pady=5)

address_frame = CTkFrame(background_frame)
address_frame.pack(padx=10, pady=5)

label_address = CTkLabel(address_frame, text="Address:", font=("Oswald", 15))
label_address.grid(row=0, column=0, padx=75, pady=5)

entry_address = CTkEntry(address_frame, width=150)
entry_address.grid(row=0, column=1, padx=10, pady=5)

email_frame = CTkFrame(background_frame)
email_frame.pack(padx=10, pady=5)

label_email = CTkLabel(email_frame, text="Email:", font=("Oswald", 15))
label_email.grid(row=0, column=0, padx=82, pady=5)

entry_email = CTkEntry(email_frame, width=150)
entry_email.grid(row=0, column=1, padx=10, pady=5)
entry_email.insert(0, "must end with @gmail")

label_current_reading_frame = CTkFrame(background_frame)
label_current_reading_frame.pack(padx=10, pady=5)

label_current_reading = CTkLabel(label_current_reading_frame, text="Current Meter Reading (cms):", font=("Oswald", 15))
label_current_reading.grid(row=0, column=0, padx=18.5, pady=5)

entry_current_reading = CTkEntry(label_current_reading_frame, width=150)
entry_current_reading.grid(row=0, column=1, padx=10, pady=5)

label_previous_reading_frame = CTkFrame(background_frame)
label_previous_reading_frame.pack(padx=10, pady=5)

label_previous_reading = CTkLabel(label_previous_reading_frame, text="Previous Meter Reading (cms):", font=("Oswald", 15))
label_previous_reading.grid(row=0, column=0, padx=17, pady=5)

entry_previous_reading = CTkEntry(label_previous_reading_frame, width=150)
entry_previous_reading.grid(row=0, column=1, padx=10, pady=5)

label_consumption_frame = CTkFrame(background_frame)
label_consumption_frame.pack(padx=10, pady=5)

label_consumption = CTkLabel(label_consumption_frame, text="Consumption (gal):", font=("Oswald", 15))
label_consumption.grid(row=0, column=0, padx=49, pady=5)

entry_consumption = CTkEntry(label_consumption_frame, width=150)
entry_consumption.grid(row=0, column=1, padx=10, pady=5)

buttom_frame = CTkFrame(background_frame, fg_color="gray13")
buttom_frame.pack(padx=10, pady=5)

calculate_button = CTkButton(buttom_frame, text="Calculate Bill", command=calculate_bill, font=("Oswald", 15))
calculate_button.grid(row=0, column=0, padx=10, pady=5)

#############################################

root.mainloop()
