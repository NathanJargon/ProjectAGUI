import tkinter as tk
from tkinter import messagebox, Frame, Canvas, Button, Scrollbar, StringVar
import sqlite3
from PIL import Image, ImageTk
from customtkinter import *
from database import WaterBillDatabase

db = WaterBillDatabase()

def save_to_database(customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php, messages):
    db.save_to_database(customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php, messages)

def fetch_data():
    for widget in button_frame.winfo_children():
        widget.destroy()

    data = db.fetch_data()
    
    for row in data:
        bill_button = CTkButton(button_frame, text=f"Customer: {row[1]}", command=lambda row=row: show_details(row))
        bill_button.pack(padx=10, pady=5)

def delete_data(id):
    db.delete_data(id)
    fetch_data()
    
def fetch_data():
    for widget in button_frame.winfo_children():
        widget.destroy()

    #conn = sqlite3.connect("_internal/db/water_bill_database.db")
    conn = sqlite3.connect("db/water_bill_database.db")
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM water_bills')
    data = cursor.fetchall()
    conn.close()
    
    for row in data:
        bill_button = CTkButton(button_frame, text=f"Customer: {row[1]}", command=lambda row=row: show_details(row))
        bill_button.pack(padx=10, pady=5)
        
def delete_and_clear(id):
    #conn = sqlite3.connect("_internal/db/water_bill_database.db")
    conn = sqlite3.connect("db/water_bill_database.db")
    
    cursor = conn.cursor()
    db.delete_and_clear(id)
    conn.close()
    fetch_data()
    
############################################# CSV Histories

#conn = sqlite3.connect("_internal/db/water_bill_database.db")
conn = sqlite3.connect("db/water_bill_database.db")

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