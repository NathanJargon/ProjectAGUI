import tkinter as tk
from tkinter import messagebox, Frame, Canvas, Button, Scrollbar, StringVar
import sqlite3
from PIL import Image, ImageTk
from customtkinter import *
from database import WaterBillDatabase

class Register:
    def __init__(self, root):
        self.root = root
        self.db = WaterBillDatabase()
        self.bill_details_var = StringVar()

        self.background_frame = CTkFrame(root, fg_color="gray12", corner_radius=0)
        self.background_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1, anchor='nw')

        self.title_frame = CTkFrame(self.background_frame, fg_color="gray12")
        self.title_frame.pack(padx=10, pady=5)

        self.label_name = CTkLabel(self.title_frame, text="Register Information", font=("Oswald", 25))
        self.label_name.grid(row=0, column=0, padx=0, pady=10)

        self.name_frame = CTkFrame(self.background_frame)
        self.name_frame.pack(padx=10, pady=5)

        self.label_name = CTkLabel(self.name_frame, text="Customer Name:", font=("Oswald", 15))
        self.label_name.grid(row=0, column=0, padx=53, pady=5)

        self.entry_name = CTkEntry(self.name_frame, width=150)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.address_frame = CTkFrame(self.background_frame)
        self.address_frame.pack(padx=10, pady=5)

        self.label_address = CTkLabel(self.address_frame, text="Address:", font=("Oswald", 15))
        self.label_address.grid(row=0, column=0, padx=75, pady=5)

        self.entry_address = CTkEntry(self.address_frame, width=150)
        self.entry_address.grid(row=0, column=1, padx=10, pady=5)

        self.email_frame = CTkFrame(self.background_frame)
        self.email_frame.pack(padx=10, pady=5)

        self.label_email = CTkLabel(self.email_frame, text="Email:", font=("Oswald", 15))
        self.label_email.grid(row=0, column=0, padx=82, pady=5)

        self.entry_email = CTkEntry(self.email_frame, width=150)
        self.entry_email.grid(row=0, column=1, padx=10, pady=5)
        self.entry_email.insert(0, "must end with @gmail")

        self.label_current_reading_frame = CTkFrame(self.background_frame)
        self.label_current_reading_frame.pack(padx=10, pady=5)

        self.label_current_reading = CTkLabel(self.label_current_reading_frame, text="Current Meter Reading (cms):", font=("Oswald", 15))
        self.label_current_reading.grid(row=0, column=0, padx=18.5, pady=5)

        self.entry_current_reading = CTkEntry(self.label_current_reading_frame, width=150)
        self.entry_current_reading.grid(row=0, column=1, padx=10, pady=5)

        self.label_previous_reading_frame = CTkFrame(self.background_frame)
        self.label_previous_reading_frame.pack(padx=10, pady=5)

        self.label_previous_reading = CTkLabel(self.label_previous_reading_frame, text="Previous Meter Reading (cms):", font=("Oswald", 15))
        self.label_previous_reading.grid(row=0, column=0, padx=17, pady=5)

        self.entry_previous_reading = CTkEntry(self.label_previous_reading_frame, width=150)
        self.entry_previous_reading.grid(row=0, column=1, padx=10, pady=5)

        self.label_consumption_frame = CTkFrame(self.background_frame)
        self.label_consumption_frame.pack(padx=10, pady=5)

        self.label_consumption = CTkLabel(self.label_consumption_frame, text="Consumption (gal):", font=("Oswald", 15))
        self.label_consumption.grid(row=0, column=0, padx=49, pady=5)

        self.entry_consumption = CTkEntry(self.label_consumption_frame, width=150)
        self.entry_consumption.grid(row=0, column=1, padx=10, pady=5)

        self.buttom_frame = CTkFrame(self.background_frame, fg_color="gray13")
        self.buttom_frame.pack(padx=10, pady=5)

        self.calculate_button = CTkButton(self.buttom_frame, text="Calculate Bill", command=self.calculate_bill, font=("Oswald", 15))
        self.calculate_button.grid(row=0, column=0, padx=10, pady=5)


    def calculate_bill(self):
        try:
            customer_name = self.entry_name.get()[:11] if ' ' not in self.entry_name.get() else self.entry_name.get().split(' ')[0]
            address = self.entry_address.get()
            email = self.entry_email.get()
            consumption = float(self.entry_consumption.get())

            current_reading = float(self.entry_current_reading.get())
            previous_reading = float(self.entry_previous_reading.get())
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

            self.db.save_to_database(customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php, message)
            
            self.db.fetch_data()
            
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
            
            self.bill_details_var.set(bill_details)
            
        except ValueError as e:
            if str(e) == "Invalid email address":
                messagebox.showerror("Error", "Please enter a valid email address.")
            else:
                messagebox.showerror("Error", "Please enter valid numeric values for consumption and meter readings.")

if __name__ == "__main__":
    root = CTk()
    set_appearance_mode("dark")

    w = 854
    h = 480

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

    register = Register(root)
    root.mainloop()