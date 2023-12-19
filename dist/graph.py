from customtkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import matplotlib.style as style

class GraphGenerator:
    def __init__(self, root):
        self.root = root
        self.graph_frame = CTkFrame(self.root, fg_color="gray12")
        self.graph_frame.pack(side=tk.LEFT, padx=10, pady=10)

    def create_graph(self):
        set_appearance_mode("dark")

        style.use('dark_background')
        #conn = sqlite3.connect('db/water_bill_database.db')
        conn = sqlite3.connect('_internal/db/water_bill_database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT DISTINCT customer_name FROM water_bills")
        customer_names = [row[0] for row in cursor.fetchall()]

        fig, ax = plt.subplots()
        ax.set_ylim([0, 250])

        for customer_name in customer_names:
            cursor.execute("SELECT * FROM water_bills WHERE customer_name = ?", (customer_name,))
            rows = cursor.fetchall()

            x_data = [row[1] for row in rows]
            y_data = [row[14] for row in rows]

            ax.bar(x_data, y_data, label=f'{customer_name}')

        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)  # Change this line
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1, anchor=tk.CENTER)  # Change this line