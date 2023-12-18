import tkinter as tk
from tkinter import messagebox, Frame, Canvas, Button, Scrollbar, StringVar
import sqlite3
from PIL import Image, ImageTk
from customtkinter import *
from database import WaterBillDatabase
from sidebar import Sidebar
import history
from register import Register

root = CTk()
root.title("AGUI")
set_appearance_mode("dark")

w = 854
h = 480

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

############################################# Sidebar

sidebar = Sidebar(root, width=200, bg_color="gray12", fg_color="gray12")
sidebar.pack(side=tk.LEFT, fill=tk.Y)

#############################################

root.mainloop()
