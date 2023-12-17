import tkinter as tk
from tkinter import messagebox, Frame, Canvas, Button, Scrollbar, StringVar
import sqlite3
from PIL import Image, ImageTk
from customtkinter import *
from database import WaterBillDatabase

class Result:
    def __init__(self, root, bill_details_var):
        self.root = root
        self.bill_details_var = bill_details_var

        self.details_frame = CTkFrame(self.root, fg_color="gray12", corner_radius=0)
        self.details_frame.place(relx=.18, rely=0, relwidth=0.9, relheight=1, anchor='nw')

        self.title_frame = CTkFrame(self.details_frame, fg_color="gray12")
        self.title_frame.pack(padx=10, pady=5)

        self.label_name = CTkLabel(self.title_frame, text="Results", font=("Oswald", 25))
        self.label_name.grid(row=0, column=0, padx=0, pady=10)

        self.bill_details_label = CTkLabel(self.details_frame, textvariable=self.bill_details_var, justify=tk.LEFT, font=("Helvetica", 15), 
                                    bg_color="gray12", 
                                    fg_color="gray12",
                                    wraplength=220)
        self.bill_details_label.pack(padx=10, pady=10)
        
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