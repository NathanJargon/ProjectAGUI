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
        self.label_name = CTkLabel(self.title_frame, text="Histories", font=("Oswald", 35))
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
        self.current_charges_var = StringVar()
        self.current_charges_var2 = StringVar()
        self.title_service = StringVar()
        self.title_billing = StringVar()
        self.fetch_data()

    def save_to_database(self, customer_name, address, account, meter, reference, due, bill_date, 
                bill_period, soa, bill, rdg_date_time, current_reading, previous_reading, 
                consumption, meter_consumption, bill_amount_php, message, water_charges, vat, dues, others):
        self.db.save_to_database(customer_name, address, account, meter, reference, due, bill_date, 
                bill_period, soa, bill, rdg_date_time, current_reading, previous_reading, 
                consumption, meter_consumption, bill_amount_php, message, water_charges, vat, dues, others)

    def fetch_data(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        data = self.db.fetch_data()

        total_width = 0
        frame_width = 300
        row = 0
        column = 0

        for i, row_data in enumerate(data):
            button_width = 70

            if total_width + button_width > frame_width:
                row += 1
                column = 0
                total_width = 0

            button_pair_frame = Frame(self.button_frame, bg="gray12")
            button_pair_frame.grid(row=row, column=column, padx=(50, 10), pady=5)

            bill_button = CTkButton(button_pair_frame, text=f"Customer: {row_data[1].lower().title().split(', ')[-1]}", command=lambda row=row_data: self.show_details(row), font=("Oswald", 18), height=40, width=70)
            bill_button.pack(side='left', padx=(0, 5))

            delete_button = CTkButton(button_pair_frame, text="X", command=lambda id=row_data[0]: self.delete_and_clear(id), font=("Oswald", 17), width=10, height=20)
            delete_button.pack(side='left')

            total_width += button_width
            column += 1
        
    def delete_and_clear(self, id):
        self.db.delete_and_clear(id)
        self.fetch_data()

    def show_details(self, row):
        title1 = ""
        title1 += f"SERVICE INFORMATION"
    
        """
        
            self.db.save_to_database(customer_name, address, account, meter, reference, rate, bill_date, 
        bill_period, soa, bill, rdg_date_time, current_reading, previous_reading, 
        consumption, meter_consumption, bill_amount_php, message, water_charges, vat, dues, others)
        
        """
        
        service_info = ""
        service_info += f"Customer Name            :   {row[1]}\n"
        service_info += f"Address                          :   {row[2]}\n"
        service_info += f"Account Number           :   {row[3]}\n"
        service_info += f"Meter Number              :   {row[4]}\n"
        service_info += f"Reference Number       :   {row[5]}\n"
        service_info += f"Due Date                       :   {row[6]}"

        title2 = ""
        title2 += f"BILLING SUMMARY"
                
        billing_summary = ""      
        billing_summary += f"Billing Date            :   {row[7]}\n"
        billing_summary += f"Billing Period         :   {row[8]}\n"
        billing_summary += f"SOA Number          :   {row[9]}\n"
        billing_summary += f"Billing Number       :   {row[10]}\n"
        billing_summary += f"Rdg Date/Time      :   {row[11]}\n"
        billing_summary += f"Current Reading    :   {row[12]}\n"
        billing_summary += f"Previous Reading   :   {row[13]}\n"
        
        current_charges = ""
        current_charges += f"Water Charge            : {row[18]}\n"
        current_charges += f"Value-added Tax       : {row[19]}\n"
        current_charges += f"Dues                           : {row[20]}\n"        
        current_charges += f"Others                        : {row[21]}\n"
        current_charges += f"Consumption             : {row[14]}\n"
        current_charges += f"Meter Consumption  : {row[15]} gallons\n"
        
        current_charges2 = "" 
        current_charges2 += f"AMT BEFORE DUE DATE  : ₱{row[16]:.2f}\n"
        current_charges2 += f"AMT AFTER DUE DATE     : ₱{row[16] + row[16]*0.1:.2f}\n"
        current_charges2 += f"Message                           : {row[17]}"

        for widget in self.background_frame.winfo_children():
            widget.destroy()
            
        self.title_service.set(title1)
        self.title_billing.set(title2)

        self.service_info_var.set(service_info)
        self.billing_summary_var.set(billing_summary)
        self.current_charges_var.set(current_charges)
        self.current_charges_var2.set(current_charges2)

        result_info = result.Result(self.root, self.service_info_var, self.billing_summary_var, 
                                    self.current_charges_var, self.current_charges_var2, self.title_service, self.title_billing)


"""
if __name__ == "__main__":
    root = CTk()
    set_appearance_mode("dark")

    w = 1280
    h = 720
    
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

    details_frame = CTkFrame(root, fg_color="gray11", corner_radius=0)
    history = History(root, details_frame)
    root.mainloop()
"""