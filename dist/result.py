import tkinter as tk
from tkinter import messagebox, Frame, Canvas, Button, Scrollbar, StringVar
import sqlite3
from PIL import Image, ImageTk
from customtkinter import *


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
    