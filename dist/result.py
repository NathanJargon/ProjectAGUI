import tkinter as tk
from tkinter import messagebox, Frame, Canvas, Button, Scrollbar, StringVar
import sqlite3
from PIL import Image, ImageTk
from customtkinter import *
from database import WaterBillDatabase
from history import History
from register import Register

class Result:
    def __init__(self):
        self.details_frame = CTkFrame(self.root, fg_color="gray10", corner_radius=0)
        self.details_frame.place(relx=.7, rely=0, relwidth=0.3, relheight=1, anchor='nw')

        self.title_frame = CTkFrame(self.details_frame, fg_color="gray10")
        self.title_frame.pack(padx=10, pady=5)

        self.label_name = CTkLabel(self.title_frame, text="Results", font=("Oswald", 25))
        self.label_name.grid(row=0, column=0, padx=0, pady=10)

        self.bill_details_label = CTkLabel(self.details_frame, textvariable=self.bill_details_var, justify=tk.LEFT, font=("Helvetica", 15), 
                                    bg_color="gray10", 
                                    fg_color="gray10",
                                    wraplength=220)
        self.bill_details_label.pack(padx=10, pady=10)