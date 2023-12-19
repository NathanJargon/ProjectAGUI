import tkinter as tk
from tkinter import messagebox, Frame, Canvas, Button, Scrollbar, StringVar
import sqlite3
from PIL import Image, ImageTk
from customtkinter import *
from database import WaterBillDatabase
import ast

class Result:
    def __init__(self, root, service_info_var, billing_summary_var):
        self.root = root
        self.service_info_var = service_info_var
        self.billing_summary_var = billing_summary_var
        self.service_info_string = self.service_info_var.get()
        self.billing_info_string = self.billing_summary_var.get()
        #self.service_info_list = self.service_info_string.split()
        #self.billing_info_list = self.billing_info_list.split()
        #print(self.service_info_list)
        #print(self.billing_info_list)
        
        self.details_frame = CTkFrame(self.root, fg_color="gray12", corner_radius=0)
        self.details_frame.place(relx=.18, rely=0, relwidth=0.9, relheight=1, anchor='nw')

        self.title_frame = CTkFrame(self.details_frame, fg_color="gray12")
        self.title_frame.pack(padx=10, pady=5)

        self.label_name = CTkLabel(self.title_frame, text="Information", font=("Oswald", 25))
        self.label_name.grid(row=0, column=0, padx=0, pady=10)

        # Create two frames for service and billing information
        self.service_frame = CTkFrame(self.details_frame, fg_color="gray12")
        self.billing_frame = CTkFrame(self.details_frame, fg_color="gray12")

        # Place the frames side by side
        self.service_frame.pack(side=tk.LEFT, padx=100, pady=10)
        self.billing_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Create labels for service and billing information
        self.service_info_label = CTkLabel(self.service_frame, textvariable=self.service_info_var, justify=tk.LEFT, font=("Oswald", 15), 
                                           bg_color="gray12", 
                                           fg_color="gray12")
        self.billing_info_label = CTkLabel(self.billing_frame, textvariable=self.billing_summary_var, justify=tk.LEFT, font=("Oswald", 12), 
                                           bg_color="gray12", 
                                           fg_color="gray12", wraplength=250)

        # Pack the labels into their respective frames
        self.service_info_label.pack(padx=10, pady=10)
        self.billing_info_label.pack(padx=10, pady=10)
        
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

    bill_details_var = tk.StringVar()
    result = Result(root, bill_details_var)
    root.mainloop()