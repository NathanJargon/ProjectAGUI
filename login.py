from tkinter import messagebox, PhotoImage
import tkinter as tk
from PIL import Image, ImageTk
from customtkinter import *
import time

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "admin":
        root.destroy()
        import app
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def turn_gray(widget):
    widget.config(fg="white")

def on_space(event):
    event.widget.config(fg="red")
    root.after(500, turn_gray, event.widget)  # 500 milliseconds = 0.5 seconds
    return "break"
    
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

title = CTkButton(root, text="LOG IN", font=("Montserrat", 45), corner_radius=32, fg_color="gray14", hover_color="gray14")
title.place(relx=0.795, rely=0.2, anchor='center')


label_username = CTkLabel(root, text="Username")
label_username.place(relx=0.8, rely=0.35, anchor='e')

entry_username = CTkEntry(root, width=150, height=35, fg_color="black")
entry_username.place(relx=0.885, rely=0.4, anchor='e')
entry_username.bind('<space>', on_space)

label_password = CTkLabel(root, text="Password")
label_password.place(relx=0.8, rely=0.55, anchor='e')

entry_password = CTkEntry(root, show="*", width=150, height=35, fg_color="black") 
entry_password.place(relx=0.885, rely=0.6, anchor='e')
entry_password.bind('<space>', on_space)

############################################# Main Image and Label

image = Image.open("img/img1.png")

# Resize the image
new_size = (550, 550)
image = image.resize(new_size, Image.LANCZOS)

photo = ImageTk.PhotoImage(image)

# Create a Label to display the image
image_label = CTkLabel(root, image=photo, text="")
image_label.place(relx=0.4, rely=0.5, anchor='center')

image_label.image = photo

label = CTkLabel(root, text="Synochrina © 2023", font=("Montserrat", 15))
label.place(relx=0.10, rely=.96, anchor='center')

#############################################


histories_button = CTkButton(root, text="START!", command=login, corner_radius=32, fg_color="#008000",
                             hover_color="#4158D0",)
histories_button.place(relx=0.88, rely=0.75, anchor="e")


root.mainloop()
