import tkinter as tk
from tkinter import messagebox, Frame, Canvas, Button, Scrollbar, StringVar
import sqlite3
from PIL import Image, ImageTk
from customtkinter import *
from database import WaterBillDatabase
from register import Register
import result

class History(result.Result):
    def __init__(self, root, details_frame):
        self.root = root
        self.details_frame = details_frame
        self.bill_details_var = StringVar()
        self.db = WaterBillDatabase()
        self.background_frame = CTkFrame(self.root, fg_color="gray12", corner_radius=0)
        self.background_frame.place(relx=.18, rely=0, relwidth=0.9, relheight=1, anchor='nw')
        self.title_frame = CTkFrame(self.background_frame, fg_color="gray12")
        self.title_frame.pack(padx=10, pady=5)
        self.label_name = CTkLabel(self.title_frame, text="Histories", font=("Oswald", 25))
        self.label_name.grid(row=0, column=0, padx=0, pady=10)
        self.canvas = Canvas(self.background_frame, bg="gray12", highlightthickness=0)
        self.scrollbar = Scrollbar(self.background_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.button_frame = Frame(self.canvas, bg="gray12")
        self.canvas.create_window((0, 0), window=self.button_frame, anchor='nw')
        self.canvas.pack(side='left', fill='both', expand=True)
        self.scrollbar.pack(side='right', fill='y')
        self.fetch_data()

    def save_to_database(self, customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php, messages):
        self.db.save_to_database(customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php, messages)

    def fetch_data(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        data = self.db.fetch_data()

        for i, row in enumerate(data):
            bill_button = CTkButton(self.button_frame, text=f"Customer: {row[1]}", command=lambda row=row: self.show_details(row))
            bill_button.grid(row=0, column=i, padx=10, pady=5)
        
    def delete_and_clear(self, id):
        self.db.delete_and_clear(id)
        self.fetch_data()

    def show_details(self, row):
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
        
        for widget in self.background_frame.winfo_children():
            widget.destroy()

        self.bill_details_var.set(bill_details)
        result_screen = result.Result(self.background_frame, self.bill_details_var)

        result_screen.details_frame.pack()
            

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

    details_frame = CTkFrame(root, fg_color="gray12", corner_radius=0)
    history = History(root, details_frame)
    root.mainloop()