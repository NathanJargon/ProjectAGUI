from customtkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import matplotlib.style as style
import sidebar

class GraphGenerator:
    def __init__(self, root):
        self.root = root
        self.background_frame = CTkFrame(self.root, fg_color="black", corner_radius=0)
        self.background_frame.place(relx=.18, rely=0, relwidth=0.9, relheight=1, anchor='nw')
        self.title_frame = CTkFrame(self.background_frame, fg_color="black")
        self.title_frame.pack(padx=10, pady=5)
        self.label_name = CTkLabel(self.title_frame, text="Graphical Representation", font=("Oswald", 25))
        self.label_name.grid(row=0, column=0, padx=0, pady=10)

    def create_graph(self):
        if hasattr(self, 'background_frame') and self.background_frame.winfo_exists():
            for widget in self.background_frame.winfo_children():
                widget.destroy()
            self.background_frame.destroy()

        if hasattr(self, 'root') and self.root.winfo_exists():
            for widget in self.root.winfo_children():
                widget.destroy()

        # Recreate the sidebar widget and background frame after destroying it.
        self.sidebar = sidebar.Sidebar(self.root)
        self.sidebar.pack(side='left', fill='y') 

        
        self.background_frame = CTkFrame(self.root, fg_color="black", corner_radius=0)
        self.background_frame.place(relx=.18, rely=0, relwidth=0.9, relheight=1, anchor='nw')
        self.title_frame = CTkFrame(self.background_frame, fg_color="black")
        self.title_frame.pack(padx=10, pady=5)
        self.label_name = CTkLabel(self.title_frame, text="Graphical Representation", font=("Oswald", 25))
        self.label_name.grid(row=0, column=0, padx=0, pady=10)

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
            y_data = [row[17] for row in rows]

            ax.bar(x_data, y_data, label=f'{customer_name}')

        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.background_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)  # Change this line
        
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

    history = GraphGenerator(root)
    history.create_graph()
    root.mainloop()