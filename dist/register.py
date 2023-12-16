import tkinter as tk
from tkinter import messagebox, Frame, Canvas, Button, Scrollbar, StringVar
import sqlite3
from PIL import Image, ImageTk
from customtkinter import *


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

#############################################

############################################# Register Information

background_frame = CTkFrame(root, fg_color="gray12", corner_radius=0)
background_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1, anchor='nw')

title_frame = CTkFrame(background_frame, fg_color="gray12")
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