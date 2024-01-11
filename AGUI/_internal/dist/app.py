from customtkinter import *
from sidebar import Sidebar
import tkinter as tk
import warnings
warnings.filterwarnings("ignore")

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
root.resizable(False, False)

############################################# Sidebar

sidebar = Sidebar(root, width=200, bg_color="gray12", fg_color="gray12")
sidebar.pack(side=tk.LEFT, fill=tk.Y)

#############################################

root.mainloop()
