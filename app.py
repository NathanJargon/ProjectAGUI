import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
from customtkinter import *

def calculate_bill():
    try:
        customer_name = entry_name.get()
        address = entry_address.get()
        email = entry_email.get()
        consumption = float(entry_consumption.get())

        current_reading = float(entry_current_reading.get())
        previous_reading = float(entry_previous_reading.get())
        meter_consumption = current_reading - previous_reading

        if not email.endswith("@gmail"):
            raise ValueError("Invalid email address")
        
        bill_amount_php = meter_consumption * 2.5

        if consumption < 50:
            message = "Great job on conserving water! Keep it up."
        elif consumption < 100:
            message = "You're using a moderate amount of water. Consider more water-saving habits."
        else:
            message = "Please be mindful of your water usage. Consider implementing water-saving tips."

        save_to_database(customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php)

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

        custom_dialog = CTkToplevel(root)
        custom_dialog.title("Water Bill - Details")
        set_appearance_mode("dark")

        w = 800 
        h = 300

        ws = custom_dialog.winfo_screenwidth()
        hs = custom_dialog.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        custom_dialog.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

        details_label = CTkLabel(custom_dialog, text=bill_details, justify=tk.LEFT, font=("Helvetica", 12), padx=10, pady=10)
        details_label.pack()

    except ValueError as e:
        if str(e) == "Invalid email address":
            messagebox.showerror("Error", "Please enter a valid email address.")
        else:
            messagebox.showerror("Error", "Please enter valid numeric values for consumption and meter readings.")

def save_to_database(customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php):
    conn = sqlite3.connect("water_bill_database.db")
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
            bill_amount_php REAL
        )
    ''')

    cursor.execute('''
        INSERT INTO water_bills (
            customer_name,
            address,
            email,
            consumption,
            current_reading,
            previous_reading,
            meter_consumption,
            bill_amount_php
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php))

    conn.commit()
    conn.close()

def display_saved_data():
    conn = sqlite3.connect("water_bill_database.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM water_bills')
    data = cursor.fetchall()

    conn.close()

    if data:
        display_window = CTkToplevel(root)
        display_window.title("Water Bill - Histories")
        set_appearance_mode("dark")
    
        for row in data:
            button_text = f"Customer: {row[1]}"
            button = CTkButton(display_window, text=button_text, command=lambda r=row: show_details(r))
            button.pack(padx=10, pady=5)

        w = 200 
        h = 350 

        # Get the screen width and height
        ws = display_window.winfo_screenwidth()
        hs = display_window.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        display_window.geometry(f"{w}x{h}+{int(x)+390}+{int(y)-160}")
    else:
        messagebox.showinfo("No Data", "No water bill data found in the database.")


def show_details(row):
    details_window = CTkToplevel(root)
    details_window.title("Water Bill - Details")
    set_appearance_mode("dark")
    bill_details = f"Customer Name: {row[1]}\n"
    bill_details += f"Address: {row[2]}\n"
    bill_details += f"Email: {row[3]}\n"
    bill_details += f"Consumption: {row[4]} gallons\n\n"
    bill_details += f"Metering Information:\n"
    bill_details += f"Current Reading: {row[5]}\n"
    bill_details += f"Previous Reading: {row[6]}\n"
    bill_details += f"Meter Consumption: {row[7]} gallons\n\n"
    bill_details += f"Billing Summary:\n"
    bill_details += f"Total Bill Amount (in PHP): ₱{row[8]:.2f}"

    details_label = CTkLabel(details_window, text=bill_details, justify=tk.LEFT, font=("Helvetica", 15), padx=10, pady=10)
    details_label.pack()

    w = 360
    h = 300 

    ws = details_window.winfo_screenwidth()
    hs = details_window.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    details_window.geometry(f"{w}x{h}+{int(x)}+{int(y)+200}")


root = CTk()
root.title("Water Bill - Main")
set_appearance_mode("dark")

w = 360
h = 270

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry(f"{w}x{h}+{int(x)}+{int(y)-200}")

label_name = CTkLabel(root, text="Customer Name:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

entry_name = CTkEntry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_address = CTkLabel(root, text="Address:")
label_address.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entry_address = CTkEntry(root)
entry_address.grid(row=1, column=1, padx=10, pady=5)

label_email = CTkLabel(root, text="Email (Must end with @gmail):")
label_email.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

entry_email = CTkEntry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_current_reading = CTkLabel(root, text="Current Meter Reading (cms):")
label_current_reading.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

entry_current_reading = CTkEntry(root)
entry_current_reading.grid(row=3, column=1, padx=10, pady=5)

label_previous_reading = CTkLabel(root, text="Previous Meter Reading (cms):")
label_previous_reading.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

entry_previous_reading = CTkEntry(root)
entry_previous_reading.grid(row=4, column=1, padx=10, pady=5)

label_consumption = CTkLabel(root, text="Consumption (gal):")
label_consumption.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

entry_consumption = CTkEntry(root)
entry_consumption.grid(row=5, column=1, padx=10, pady=5)

calculate_button = CTkButton(root, text="Calculate Bill", command=calculate_bill)
calculate_button.grid(row=6, column=0, columnspan=2, pady=10, sticky=tk.E)

histories_button = CTkButton(root, text="Histories", command=display_saved_data)
histories_button.grid(row=6, column=0, columnspan=1, pady=10, padx=5, sticky=tk.W)

root.mainloop()
