from tkinter import messagebox, PhotoImage, Button
from PIL import Image, ImageTk
from customtkinter import *
import tkinter as tk
import time
import sys
import os
import subprocess
import warnings

warnings.filterwarnings("ignore")

class Login:
    def __init__(self):
        self.root = CTk()
        self.root.title("AGUI")
        set_appearance_mode("dark")

        w = 1280
        h = 720

        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
        self.root.resizable(False, False)
        self.create_widgets()

        self.root.attributes('-alpha', 0.0)

        for i in range(1, 101):
            self.root.after(i * 50, lambda i=i: self.root.attributes('-alpha', i / 100.0))

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "admin":
            self.root.destroy()
            app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.py')
            subprocess.run(['python', app_path])
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def turn_gray(self, widget):
        widget.config(fg="white")

    def on_space(self, event):
        event.widget.config(fg="red")
        self.root.after(500, self.turn_gray, event.widget)  # 500 milliseconds = 0.5 seconds
        return "break"
        
    def create_widgets(self):
        background_frame = CTkFrame(self.root, fg_color="gray12")
        background_frame.place(relx=0.56, rely=0, relwidth=0.5, relheight=1, anchor='nw')
    

        title = Button(self.root, text="Welcome!", font=("Oswald", 65), 
                       fg="white", bg="gray12", bd=0, activebackground="gray12", activeforeground="white",)
        title.place(relx=0.80, rely=0.2, anchor='center')
        
        label_username = CTkLabel(self.root, text="Username", fg_color="gray12", font=("Oswald", 24))
        label_username.place(relx=0.76, rely=0.32, anchor='e')
        label_password = CTkLabel(self.root, text="Password", fg_color="gray12", font=("Oswald", 24))
        label_password.place(relx=0.76, rely=0.52, anchor='e')

        self.entry_username = CTkEntry(self.root, width=200, height=50, fg_color="gray12", font=("Oswald", 15))
        self.entry_username.place(relx=0.885, rely=0.4, anchor='e')
        self.entry_username.insert(0, "admin")
        self.entry_username.bind('<space>', self.on_space)

        self.entry_password = CTkEntry(self.root, show="*", width=200, height=50, fg_color="gray12", font=("Oswald", 15))
        self.entry_password.place(relx=0.885, rely=0.6, anchor='e')
        self.entry_password.insert(0, "admin")
        self.entry_password.bind('<space>', self.on_space)

        image = Image.open("img/png/logo-no-background.png")
        #image = Image.open("_internal/img/png/logo-no-background.png")
        new_size = (850, 350)
        image = image.resize(new_size, Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        image_label = CTkLabel(self.root, image=photo, text="")
        image_label.place(relx=0.285, rely=0.5, anchor='center')

        image_label.image = photo

        label = CTkLabel(self.root, text="Synochrina © 2023", font=("Nanum Pen", 16))
        label.place(relx=0.06, rely=.96, anchor='center')

        histories_button = CTkButton(self.root, text="Access", font=("Oswald", 25), command=self.login, corner_radius=32, fg_color="#008000",
                                    hover_color="#4158D0",)
        histories_button.place(relx=0.865, rely=0.75, anchor="e")

        if getattr(sys, 'frozen', False):
            pyi_splash.close()
        self.root.mainloop()


if __name__ == '__main__':
    login_app = Login()