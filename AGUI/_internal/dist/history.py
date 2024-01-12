from tkinter import messagebox, Frame, Canvas, Button, Scrollbar, StringVar
from customtkinter import *
from database import Database
import tkinter as tk
import result
import warnings
warnings.filterwarnings("ignore")

class History(result.Result):
    def __init__(self, root, details_frame):
        self.root = root
        self.details_frame = details_frame
        self.bill_details_var = StringVar()
        #self.db_path = "db/water_bill_database.db"
        self.db_path = "_internal/db/water_bill_database.db"
        self.db = Database(self.db_path)
        self.background_frame = CTkFrame(self.root, fg_color="gray12", corner_radius=0)
        self.background_frame.place(relx=.18, rely=0, relwidth=0.9, relheight=1, anchor='nw')
        self.title_frame = CTkFrame(self.background_frame, fg_color="gray12")
        self.title_frame.pack(padx=10, pady=5)
        self.label_name = CTkLabel(self.title_frame, text="Histories", font=("Oswald", 25, "underline"))
        self.label_name.grid(row=0, column=0, padx=0, pady=10)
        self.canvas = Canvas(self.background_frame, bg="gray12", highlightthickness=0)
        self.scrollbar = Scrollbar(self.background_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.button_frame = Frame(self.canvas, bg="gray12")
        self.canvas.create_window((0, 0), window=self.button_frame, anchor='nw')
        self.canvas.pack(side='left', fill='both', expand=True)
        self.scrollbar.pack(side='right', fill='y')
        self.service_info_var = StringVar()
        self.billing_summary_var = StringVar()
        self.title_service = StringVar()
        self.title_billing = StringVar()
        self.fetch_data()

    def save_to_database(self, customer_name, address, account, meter, reference, rate, charges, bill_date, 
                bill_period, soa, bill, rdg_date_time, current_reading, previous_reading, 
                consumption, meter_consumption, bill_amount_php, message):
        self.db.save_to_database(customer_name, address, account, meter, reference, rate, charges, bill_date, 
                bill_period, soa, bill, rdg_date_time, current_reading, previous_reading, 
                consumption, meter_consumption, bill_amount_php, message)

    def fetch_data(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        data = self.db.fetch_data()

        for i, row in enumerate(data):
            button_pair_frame = Frame(self.button_frame, bg="gray12")
            button_pair_frame.grid(row=0, column=i, padx=10, pady=5)

            bill_button = CTkButton(button_pair_frame, text=f"Customer: {row[1].lower().title().split()[-1]}", command=lambda row=row: self.show_details(row))
            bill_button.pack(side='left')

            delete_button = CTkButton(button_pair_frame, text="X", command=lambda id=row[0]: self.delete_and_clear(id), width=2)
            delete_button.pack(side='left')
        
    def delete_and_clear(self, id):
        self.db.delete_and_clear(id)
        self.fetch_data()

    def show_details(self, row):
        """
        bill_details = ""
        bill_details += f"SERVICE INFORMATION\n\n"
        bill_details += f"Customer Name: {row[0]}\n"
        bill_details += f"Address: {row[1]}\n"
        bill_details += f"Account Number: {row[2]}\n"
        bill_details += f"Meter Number: {row[3]}\n"
        bill_details += f"Reference Number: {row[4]}\n"
        bill_details += f"Rate per Cubic Meter: {row[5]}\n\n"
        bill_details += f"BILLING SUMMARY:\n\n"
        bill_details += f"Consumption: {row[6]} gallons\n"
        bill_details += f"Billing Date: {row[7]}\n"
        bill_details += f"Billing Period: {row[8]}\n"
        bill_details += f"Reading Date/Time: {row[9]}\n"
        bill_details += f"Current Reading: {row[10]}\n"
        bill_details += f"Previous Reading: {row[11]}\n"
        bill_details += f"Meter Consumption: {row[12]} gallons\n\n"
        bill_details += f"BILLING SUMMARY\n"
        bill_details += f"Total Bill Amount (in PHP): ₱{row[13]:.2f}\n\n"
        bill_details += f"Message: {row[14]}"
        
        for widget in self.background_frame.winfo_children():
            widget.destroy()

        self.bill_details_var.set(bill_details)
        result_screen = result.Result(self.background_frame, self.bill_details_var)

        result_screen.details_frame.pack()
        """
        
        title1 = ""
        title1 += f"SERVICE INFORMATION\n"
        
        service_info = ""
        service_info += f"Customer Name: {row[1]}\n"
        service_info += f"Address: {row[2]}\n"
        service_info += f"Account Number: {row[3]}\n"
        service_info += f"Meter Number: {row[4]}\n"
        service_info += f"Reference Number: {row[5]}\n"
        service_info += f"Rate per Cubic Meter: {row[6]}\n"
        service_info += f"Charges/Dues: {row[7]}"

        title2 = ""
        title2 += f"BILLING SUMMARY\n"
                
        billing_summary = ""      
        billing_summary += f"Billing Date: {row[8]}\n"
        billing_summary += f"Billing Period: {row[9]}\n"
        billing_summary += f"SOA Number: {row[10]}\n"
        billing_summary += f"Billing Number: {row[11]}\n"
        billing_summary += f"Rdg Date/Time: {row[12]}\n"
        billing_summary += f"Current Reading: {row[13]}\n"
        billing_summary += f"Previous Reading: {row[14]}\n"
        billing_summary += f"Consumption: {row[15]}\n"
        billing_summary += f"Meter Consumption: {row[16]} gallons\n\n"
        billing_summary += f"Total Bill Amount (in PHP): ₱{row[17]:.2f}\n"
        billing_summary += f"Message: {row[18]}"

        for widget in self.background_frame.winfo_children():
            widget.destroy()
            
        self.title_service.set(title1)
        self.title_billing.set(title2)

        self.service_info_var.set(service_info)
        self.billing_summary_var.set(billing_summary)

        result_info = result.Result(self.root, self.service_info_var, self.billing_summary_var, self.title_service, self.title_billing)

"""
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

    details_frame = CTkFrame(root, fg_color="gray12", corner_radius=0)
    history = History(root, details_frame)
    root.mainloop()
"""