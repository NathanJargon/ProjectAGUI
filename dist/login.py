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

if getattr(sys, 'frozen', False):
    import pyi_splash
        
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "admin":
        root.destroy()
        #import app
        #app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist', 'app.py')
        app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.py')
        subprocess.run(['python', app_path])
        #subprocess.run(['python', app_path])
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def turn_gray(widget):
    widget.config(fg="white")

def on_space(event):
    event.widget.config(fg="red")
    root.after(500, turn_gray, event.widget)  # 500 milliseconds = 0.5 seconds
    return "break"

if __name__ == '__main__':
    ############################################# Origin Screen

    root = CTk()
    root.title("Water Bill - Login")
    set_appearance_mode("dark")

    w = 854
    h = 480

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry(f"{w}x{h}+{int(x)}+{int(y)}")


    ############################################# LOGIN

    background_frame = CTkFrame(root, fg_color="gray12")
    background_frame.place(relx=0.56, rely=0, relwidth=0.5, relheight=1, anchor='nw')

    title = Button(root, text="Welcome!", font=("Oswald", 45), fg="white", bg="gray12", bd=0)
    title.place(relx=0.79, rely=0.2, anchor='center')

    label_username = CTkLabel(root, text="Username", fg_color="gray12", font=("Oswald", 15))
    label_username.place(relx=0.76, rely=0.32, anchor='e')
    label_password = CTkLabel(root, text="Password", fg_color="gray12", font=("Oswald", 15))
    label_password.place(relx=0.76, rely=0.52, anchor='e')

    entry_username = CTkEntry(root, width=150, height=35, fg_color="gray12", font=("Oswald", 12))
    entry_username.place(relx=0.885, rely=0.4, anchor='e')
    entry_username.insert(0, "admin")
    entry_username.bind('<space>', on_space)

    entry_password = CTkEntry(root, show="*", width=150, height=35, fg_color="gray12", font=("Oswald", 12))
    entry_password.place(relx=0.885, rely=0.6, anchor='e')
    entry_password.insert(0, "admin")
    entry_password.bind('<space>', on_space)

    ############################################# Main Image and Label

    image = Image.open("_internal/img/img1.png")
    #image = Image.open("img/img1.png")

    new_size = (550, 550)
    image = image.resize(new_size, Image.LANCZOS)

    photo = ImageTk.PhotoImage(image)

    image_label = CTkLabel(root, image=photo, text="")
    image_label.place(relx=0.30, rely=0.5, anchor='center')

    image_label.image = photo

    label = CTkLabel(root, text="Synochrina © 2023", font=("Nanum Pen", 15))
    label.place(relx=0.09, rely=.96, anchor='center')

    #############################################


    def login_with_error_handling():
        try:
            login()
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to exit...")

    histories_button = CTkButton(root, text="Access", font=("Oswald", 15), command=login_with_error_handling, corner_radius=32, fg_color="#008000",
                                hover_color="#4158D0",)
    histories_button.place(relx=0.88, rely=0.75, anchor="e")

    if getattr(sys, 'frozen', False):
        pyi_splash.close()
    root.mainloop()
