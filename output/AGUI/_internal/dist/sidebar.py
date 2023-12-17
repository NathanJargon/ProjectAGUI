import sys
import os
import importlib
import tkinter as tk
import customtkinter as ctk
from tkinter import PhotoImage
from database import WaterBillDatabase
import history
import register
import subprocess

class Sidebar(ctk.CTkFrame):
    def __init__(self, root, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()
        self.root = root
        self.details_frame = ctk.CTkFrame(root, fg_color="gray12", corner_radius=0)
        self.bill_details_var = tk.StringVar()
        
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

        button1 = ctk.CTkButton(button_frame, text="Input Data", command=self.on_button1_click, bg_color="gray12", fg_color="gray12")
        button1.pack(pady=(20,5), padx=10)

        button2 = ctk.CTkButton(button_frame, text="Histories", command=self.on_button2_click, bg_color="gray12", fg_color="gray12")
        button2.pack(pady=(20,5), padx=10)

        button3 = ctk.CTkButton(button_frame, text="Graphical Presentation", command=self.on_button3_click, bg_color="gray12", fg_color="gray12")
        button3.pack(pady=(20,5), padx=10)

        button4 = ctk.CTkButton(button_frame, text="Log out", command=self.on_button4_click, bg_color="gray12", fg_color="gray12")
        button4.pack(pady=(95,5), padx=10)
        
    def on_button1_click(self):
        register_window = register.Register(self.root)

    def on_button2_click(self):
        history_window = history.History(self.root, self.details_frame)

    def on_button3_click(self):
        pass

    def on_button4_click(self):
        self.root.destroy()
        login_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'login.py')
        #subprocess.run(['python', login_path])
        subprocess.run(['python', login_path])

class MainApplication(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        main_label = ctk.CTkLabel(self, text="Main Content", font=("Arial", 16), bg_color="gray12", fg_color="white")
        main_label.pack(pady=20)

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

    main_app = MainApplication(root, bg_color="gray12")
    main_app.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    root.mainloop()