import sys
import os
import importlib
from tkinter import messagebox
import ast
import csv
import sqlite3
import tkinter as tk
import customtkinter as ctk
from tkinter import PhotoImage
import history
import register
import subprocess
import graph
import warnings
warnings.filterwarnings("ignore")


class Sidebar(ctk.CTkFrame):
    def export_to_csv(self):
        conn = sqlite3.connect('_internal/db/water_bill_database.db')
        #conn = sqlite3.connect('db/water_bill_database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM water_bills")
        rows = cursor.fetchall()

        if rows:
            #filename = f"csv/CSV.csv"
            filename = f"_internal/csv/CSV.csv"
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)

                # Write column headers
                column_names = [description[0] for description in cursor.description]
                writer.writerow(column_names)

                # Write rows
                for row in rows:
                    writer.writerow(row)

            messagebox.showinfo("Success", f"Successfully exported to CSV file")
        conn.close()
        
    def __init__(self, root, master=None, **kwargs):
        super().__init__(master, **kwargs) # Takes all attributes from CTkFrame
        self.root = root
        self.create_widgets()
        self.details_frame = ctk.CTkFrame(root, fg_color="gray12", corner_radius=0)
        self.bill_details_var = tk.StringVar()
        register_window = register.Register(self.root)
        
    def create_widgets(self):
        title_frame = ctk.CTkFrame(self, bg_color="gray12", fg_color="gray12", height=50)
        title_frame.pack(fill=tk.X)

        image = PhotoImage(file="_internal/img/logo.png")
        #image = PhotoImage(file="img/logo.png")
        image = image.subsample(3, 3)
        title_label = ctk.CTkButton(title_frame, image=image, text="", bg_color="gray12", 
                                    fg_color="gray12", hover_color="gray12")
        title_label.image = image
        title_label.pack(pady=(0,0))

        button_frame = ctk.CTkFrame(self, bg_color="gray12", fg_color="gray12")
        button_frame.pack(fill=tk.BOTH, expand=True)
                
        button1 = ctk.CTkButton(button_frame, text="Register\nInformation", command=self.register_information, bg_color="gray12", fg_color="gray10", corner_radius=22, hover_color="black")
        button1.pack(pady=(15,5), padx=10)

        button2 = ctk.CTkButton(button_frame, text="Histories\nRegistered", command=self.histories_registered, bg_color="gray12", fg_color="gray10", corner_radius=22, hover_color="black")
        button2.pack(pady=(15,5), padx=10)

        button3 = ctk.CTkButton(button_frame, text="Graphical\nPresentation", command=self.graphical_presentation, bg_color="gray12", fg_color="gray10", corner_radius=22, hover_color="black")
        button3.pack(pady=(15,5), padx=10)
    
        button4 = ctk.CTkButton(button_frame, text="Export Result \nto CSV", command=self.export_to_csv, bg_color="gray12", fg_color="gray10", corner_radius=22, hover_color="black")
        button4.pack(pady=(15,5), padx=10)

        button5 = ctk.CTkButton(button_frame, text="Log out", command=self.login_button, bg_color="gray12", fg_color="gray10", corner_radius=22, hover_color="black")
        button5.pack(pady=(60,5), padx=10)
        
    def register_information(self):
        register_window = register.Register(self.root)

    def histories_registered(self):
        history_window = history.History(self.root, self.details_frame)

    def graphical_presentation(self):
        # Now create a new graph frame
        self.background_frame = graph.GraphGenerator(self.root)
        self.background_frame.create_graph()

    def login_button(self):
        self.root.destroy()
        login_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'login.py')
        #login_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'login.py')
        subprocess.run(['python', login_path])

class MainApplication(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        main_label = ctk.CTkLabel(self, text="You have accessed\nthe application!", font=("Arial", 40), bg_color="gray12", fg_color="gray12")
        main_label.pack(pady=150)

"""
if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Sidebar")
    ctk.set_appearance_mode("dark")
    
    w = 854
    h = 480

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

    sidebar = Sidebar(root, width=200, bg_color="gray12", fg_color="gray12")
    sidebar.pack(side=tk.LEFT, fill=tk.Y)

    root.mainloop()
"""