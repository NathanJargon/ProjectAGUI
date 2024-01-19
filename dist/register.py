from tkinter import messagebox, StringVar, Tk, Button, PhotoImage
from customtkinter import *
from database import Database
import tkinter as tk
import result
import warnings
warnings.filterwarnings("ignore")


class Register(result.Result):
    def __init__(self, root):
        self.root = root
        self.db_path = "db/water_bill_database.db"
        #self.db_path = "_internal/db/water_bill_database.db"
        self.db = Database(self.db_path)

        self.service_info_var = StringVar()
        self.billing_summary_var = StringVar()
        self.current_charges_var = StringVar()
        self.current_charges_var2 = StringVar()
        self.title_service = StringVar()
        self.title_billing = StringVar()
        
        self.background_frame = CTkFrame(root, fg_color="gray11", corner_radius=0)
        self.background_frame.place(relx=.18, rely=0, relwidth=.9, relheight=1, anchor='nw')
        self.background_frame.grid_rowconfigure(1, weight=1)
        self.background_frame.grid_columnconfigure(1, weight=1)

        self.service_frame = CTkFrame(self.background_frame, fg_color="gray11")
        self.service_frame.grid(row=0, column=0, sticky='w', padx=(100, 10), pady=(25, 373))

        self.title_frame = CTkFrame(self.background_frame, fg_color="gray12")
        self.title_frame.grid(row=1, column=0, padx=0, pady=5)

        self.label_name1 = CTkLabel(self.service_frame, text="Service Information", font=("Oswald", 24))
        self.label_name1.grid(row=0, column=0, padx=0, pady=(10, 20))

        self.name_frame = CTkFrame(self.service_frame)
        self.name_frame.grid(row=1, column=0, padx=10, pady=5)

        self.label_name = CTkLabel(self.name_frame, text="Customer Name:", font=("Oswald", 18))
        self.label_name.grid(row=0, column=0, padx=(10, 40), pady=5)

        self.entry_name = CTkEntry(self.name_frame, width=200, height=35)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        self.entry_name.insert(0, "Lastname, Firstname")

        self.address_frame = CTkFrame(self.service_frame)
        self.address_frame.grid(row=2, column=0, padx=5, pady=5)

        self.label_address = CTkLabel(self.address_frame, text="Address:", font=("Oswald", 18))
        self.label_address.grid(row=0, column=0, padx=(10, 90), pady=5)
        
        self.entry_address = CTkEntry(self.address_frame, width=200, height=35)
        self.entry_address.grid(row=0, column=1, padx=10, pady=5)
        self.entry_address.insert(0, "Bldg/Rm/Flr")
        
        self.account_frame = CTkFrame(self.service_frame)
        self.account_frame.grid(row=3, column=0, padx=10, pady=5)

        self.label_account = CTkLabel(self.account_frame, text="Account Number:", font=("Oswald", 18))
        self.label_account.grid(row=0, column=0, padx=(10, 36), pady=5)
        
        self.entry_account = CTkEntry(self.account_frame, width=200, height=35)
        self.entry_account.grid(row=0, column=1, padx=10, pady=5)
        self.entry_account.insert(0, "N/A if None")
        
        self.meter_frame = CTkFrame(self.service_frame)
        self.meter_frame.grid(row=4, column=0, padx=10, pady=5)

        self.label_meter = CTkLabel(self.meter_frame, text="Meter Number:", font=("Oswald", 18))
        self.label_meter.grid(row=0, column=0, padx=(10, 48), pady=5)

        self.entry_meter = CTkEntry(self.meter_frame, width=200, height=35)
        self.entry_meter.grid(row=0, column=1, padx=10, pady=5)

        self.reference_frame = CTkFrame(self.service_frame)
        self.reference_frame.grid(row=5, column=0, padx=10, pady=(5, 10))

        self.label_reference = CTkLabel(self.reference_frame, text="Reference Number:", font=("Oswald", 18))
        self.label_reference.grid(row=0, column=0, padx=(10, 25), pady=5)

        self.entry_reference = CTkEntry(self.reference_frame, width=200, height=35)
        self.entry_reference.grid(row=0, column=1, padx=10, pady=5)
        
        # Current Charges
        
        self.current_charges_frame = CTkFrame(self.background_frame, fg_color="gray11")
        self.current_charges_frame.grid(row=0, column=0, sticky='w', padx=(100, 10), pady=(320, 10))

        self.cc_name = CTkLabel(self.current_charges_frame, text="Current Charges", font=("Oswald", 24))
        self.cc_name.grid(row=0, column=0, padx=0, pady=(10, 20))

        self.waterCharges_frame = CTkFrame(self.current_charges_frame)
        self.waterCharges_frame.grid(row=1, column=0, padx=10, pady=(5, 10))

        self.label_waterCharges = CTkLabel(self.waterCharges_frame, text="Water Charge:", font=("Oswald", 18))
        self.label_waterCharges.grid(row=0, column=0, padx=(10, 55), pady=5)

        self.entry_waterCharges = CTkEntry(self.waterCharges_frame, width=200, height=35)
        self.entry_waterCharges.grid(row=0, column=1, padx=10, pady=5)
        self.entry_waterCharges.insert(0, "0")
        
        self.vat_frame = CTkFrame(self.current_charges_frame)
        self.vat_frame.grid(row=2, column=0, padx=10, pady=(5, 10))

        self.label_vat = CTkLabel(self.vat_frame, text="Value-Added Tax:", font=("Oswald", 18))
        self.label_vat.grid(row=0, column=0, padx=(10, 35), pady=5)

        self.entry_vat = CTkEntry(self.vat_frame, width=200, height=35)
        self.entry_vat.grid(row=0, column=1, padx=10, pady=5)
        self.entry_vat.insert(0, "0")
        
        self.dues_frame = CTkFrame(self.current_charges_frame)
        self.dues_frame.grid(row=3, column=0, padx=10, pady=(5, 10))

        self.label_dues = CTkLabel(self.dues_frame, text="Dues:", font=("Oswald", 18))
        self.label_dues.grid(row=0, column=0, padx=(10, 110), pady=5)

        self.entry_dues = CTkEntry(self.dues_frame, width=200, height=35)
        self.entry_dues.grid(row=0, column=1, padx=10, pady=5)
        self.entry_dues.insert(0, "Includes: Arrears")

        self.others_frame = CTkFrame(self.current_charges_frame)
        self.others_frame.grid(row=4, column=0, padx=10, pady=(5, 10))

        self.label_others = CTkLabel(self.others_frame, text="Others:", font=("Oswald", 18))
        self.label_others.grid(row=0, column=0, padx=(10, 100), pady=5)

        self.entry_others = CTkEntry(self.others_frame, width=200, height=35)
        self.entry_others.grid(row=0, column=1, padx=10, pady=5)
        self.entry_others.insert(0, "Includes: Penalty (-11.65)")

        # Billing Summary
        
        self.billing_frame = CTkFrame(self.background_frame, fg_color="gray11")
        self.billing_frame.grid(row=0, column=1, sticky='e', padx=(10, 200), pady=(10, 45))

        self.label_name2 = CTkLabel(self.billing_frame, text="Billing Information", font=("Oswald", 24))
        self.label_name2.grid(row=0, column=0, padx=0, pady=(10, 20))

        self.soa_frame = CTkFrame(self.billing_frame)
        self.soa_frame.grid(row=1, column=0, padx=5, pady=5)

        self.label_soa= CTkLabel(self.soa_frame, text="SOA Number:", font=("Oswald", 18))
        self.label_soa.grid(row=0, column=0, padx=(10, 95), pady=5)

        self.entry_soa = CTkEntry(self.soa_frame, width=200, height=35)
        self.entry_soa.grid(row=0, column=1, padx=10, pady=5)
        
        self.bill_frame = CTkFrame(self.billing_frame)
        self.bill_frame.grid(row=2, column=0, padx=5, pady=5)

        self.label_bill= CTkLabel(self.bill_frame, text="Bill Number:", font=("Oswald", 18))
        self.label_bill.grid(row=0, column=0, padx=(10, 100), pady=5)

        self.entry_bill = CTkEntry(self.bill_frame, width=200, height=35)
        self.entry_bill.grid(row=0, column=1, padx=10, pady=5)
        
        self.billdate_frame = CTkFrame(self.billing_frame)
        self.billdate_frame.grid(row=3, column=0, padx=5, pady=5)

        self.label_billdate = CTkLabel(self.billdate_frame, text="Billing Date:", font=("Oswald", 18))
        self.label_billdate.grid(row=0, column=0, padx=(10, 100), pady=5)

        self.entry_billdate = CTkEntry(self.billdate_frame, width=200, height=35)
        self.entry_billdate.grid(row=0, column=1, padx=10, pady=5)
        self.entry_billdate.insert(0, "YYYY-MM-DD")

        self.billperiod_frame = CTkFrame(self.billing_frame)
        self.billperiod_frame.grid(row=4, column=0, padx=5, pady=5)

        self.label_billperiod= CTkLabel(self.billperiod_frame, text="Billing Period:", font=("Oswald", 18))
        self.label_billperiod.grid(row=0, column=0, padx=(10, 90), pady=5)

        self.entry_billperiod = CTkEntry(self.billperiod_frame, width=200, height=35)
        self.entry_billperiod.grid(row=0, column=1, padx=10, pady=5)
        self.entry_billperiod.insert(0, "YYYY-MM-DD to YYYY-MM-DD")
        
        self.rdg_frame = CTkFrame(self.billing_frame)
        self.rdg_frame.grid(row=5, column=0, padx=5, pady=5)

        self.label_rdg = CTkLabel(self.rdg_frame, text="Rdg Date/Time:", font=("Oswald", 18))
        self.label_rdg.grid(row=0, column=0, padx=(10, 82), pady=5)

        self.entry_rdg = CTkEntry(self.rdg_frame, width=200, height=35)
        self.entry_rdg.grid(row=0, column=1, padx=10, pady=5) 
        self.entry_rdg.insert(0, "YYYY-MM-DD 00:00:00 UTC")
        
        self.due_frame = CTkFrame(self.billing_frame)
        self.due_frame.grid(row=6, column=0, padx=10, pady=5)

        self.label_due = CTkLabel(self.due_frame, text="Due Date:", font=("Oswald", 18))
        self.label_due.grid(row=0, column=0, padx=(10, 120), pady=5)

        self.entry_due = CTkEntry(self.due_frame, width=200, height=35)
        self.entry_due.grid(row=0, column=1, padx=10, pady=5)
        self.entry_due.insert(0, "YYYY-MM-DD")
        
        self.type_frame = CTkFrame(self.billing_frame)
        self.type_frame.grid(row=7, column=0, padx=5, pady=5)

        self.type_label = CTkLabel(self.type_frame, text="Customer Type:", font=("Oswald", 18))
        self.type_label.grid(row=0, column=0, padx=(10, 80), pady=5)

        self.type_entry = CTkEntry(self.type_frame, width=200, height=35)
        self.type_entry.grid(row=0, column=1, padx=10, pady=5)
        self.type_entry.insert(0, "Residential, Semi-Business, Business Group I/II")
        
        self.label_current_reading_frame = CTkFrame(self.billing_frame)
        self.label_current_reading_frame.grid(row=8, column=0, padx=5, pady=5)

        self.label_current_reading = CTkLabel(self.label_current_reading_frame, text="Pres Reading (cms):", font=("Oswald", 18))
        self.label_current_reading.grid(row=0, column=0, padx=(10, 52), pady=5)

        self.entry_current_reading = CTkEntry(self.label_current_reading_frame, width=200, height=35)
        self.entry_current_reading.grid(row=0, column=1, padx=10, pady=5)
        self.entry_current_reading.insert(0, "0 if None")

        self.label_previous_reading_frame = CTkFrame(self.billing_frame)
        self.label_previous_reading_frame.grid(row=9, column=0, padx=5, pady=5)

        self.label_previous_reading = CTkLabel(self.label_previous_reading_frame, text="Prev Reading (cms):", font=("Oswald", 18))
        self.label_previous_reading.grid(row=0, column=0, padx=(10, 52), pady=5)

        self.entry_previous_reading = CTkEntry(self.label_previous_reading_frame, width=200, height=35)
        self.entry_previous_reading.grid(row=0, column=1, padx=10, pady=5)
        self.entry_previous_reading.insert(0, "0")
        
        # BUTTON

        #photo = PhotoImage(file="_internal/img/button1.png")
        photo = PhotoImage(file="img/button1.png")
        photo = photo.subsample(3, 3)

        self.calculate_button = CTkButton(self.billing_frame, image=photo, text="", corner_radius= 50, command=self.calculate_bill, hover_color="gray11", bg_color="gray11", fg_color="gray11")
        self.calculate_button.grid(row=10, column=0, padx=(0, 0), pady=(10, 0))


    def calculate_bill(self):
        try:
            customer_name = self.entry_name.get()[:30] if len(self.entry_name.get()) > 30 else self.entry_name.get()
            address = self.entry_address.get()[:30] if len(self.entry_address.get()) > 30 else self.entry_address.get()
            account = self.entry_account.get()
            meter = self.entry_meter.get()
            reference = self.entry_reference.get()
            due = self.entry_due.get()
            bill_date = self.entry_billdate.get()
            bill_period = self.entry_billperiod.get()
            soa = self.entry_soa.get()
            bill = self.entry_bill.get()
            rdg_date_time = self.entry_rdg.get()
            current_reading = float(self.entry_current_reading.get())
            previous_reading = float(self.entry_previous_reading.get())
            type = self.type_entry.get()
            if ',' in type:
                type = type.split(',')[0]
            water_charges = float(self.entry_waterCharges.get())
            vat = float(self.entry_vat.get())
            dues = float(self.entry_dues.get())
            others = float(self.entry_others.get())
            meter_consumption = current_reading - previous_reading
            message = ""
            
            bill_amount_php = (water_charges + dues + others) + vat

            if meter_consumption < 0:
                meter_consumption = 0
            
            if len(bill_date) != 10 or len(due) != 10:
                raise ValueError("Invalid date")
            
            if len(bill_period) != 24:
                raise ValueError("Invalid bill period")
            
            if meter_consumption < 50:
                message = "Great job on conserving water! Keep it up.\n"
            elif meter_consumption < 100:
                message = "You're using a moderate amount of water. Consider more water-saving habits."
            else:
                message = "Please be mindful of your water usage. Consider implementing water-saving tips."

            #print(customer_name, address, account, meter, reference, rate, consumption, bill_date, bill_period, rdg_date_time, current_reading, previous_reading, meter_consumption, bill_amount_php, message)

            self.db.save_to_database(customer_name, address, account, meter, reference, due, bill_date, 
                bill_period, soa, bill, rdg_date_time, current_reading, previous_reading, 
                type, meter_consumption, bill_amount_php, message, water_charges, vat, dues, others)
            
            self.db.fetch_data()

            title1 = ""
            title1 += f"SERVICE INFORMATION"
            
            service_info = ""
            service_info += f"Customer Name            :   {customer_name}\n"
            service_info += f"Address                          :   {address}\n"
            service_info += f"Account Number           :   {account}\n"
            service_info += f"Meter Number              :   {meter}\n"
            service_info += f"Reference Number       :   {reference}\n"
            service_info += f"Due Date                       :   {due}\n"
            service_info += f"Customer Type             :   {type}"
            
            title2 = ""
            title2 += f"BILLING SUMMARY"
                    
            billing_summary = ""      
            billing_summary += f"Billing Date            :   {bill_date}\n"
            billing_summary += f"Billing Period         :   {bill_period}\n"
            billing_summary += f"SOA Number          :   {soa}\n"
            billing_summary += f"Billing Number       :   {bill}\n"
            billing_summary += f"Rdg Date/Time      :   {rdg_date_time}\n"
            billing_summary += f"Current Reading    :   {current_reading}\n"
            billing_summary += f"Previous Reading   :   {previous_reading}"
            
            current_charges = ""
            current_charges += f"Water Charge           : {water_charges}\n"
            current_charges += f"Value-added Tax       : {vat}\n"
            current_charges += f"Dues                           : {dues}\n"        
            current_charges += f"Others                        : {others}\n"
            current_charges += f"Meter Consumption  : {meter_consumption} gallons"
            
            current_charges2 = "" 
            current_charges2 += f"AMT BEFORE DUE DATE  : ₱{bill_amount_php:.2f}\n"
            current_charges2 += f"Penalty                             : {bill_amount_php*0.1:.2f}\n"
            current_charges2 += f"AMT AFTER DUE DATE     : ₱{bill_amount_php + bill_amount_php*0.1:.2f}\n"
            current_charges2 += f"Message                           : {message}"
            
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

            
        except ValueError as e:
            match str(e): # Switch for more efficient use-case
                case "Invalid bill date":
                    messagebox.showerror("Error", "Please enter a valid bill date!")
                case "Invalid bill period":
                    messagebox.showerror("Error", "Please enter a valid bill period!")
                case _:
                    messagebox.showerror("Error", "Please enter valid numeric values for consumption and meter readings.")
            
            """ If-statement
            if str(e) == "Invalid email address":
                messagebox.showerror("Error", "Please enter a valid email address!")
            elif str(e) == "Invalid meter consumption":
                messagebox.showerror("Error", "Please enter a valid pres and prev reading!")
            else:
                messagebox.showerror("Error", "Please enter valid numeric values for consumption and meter readings.")
            """

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

    register = Register(root)
    root.mainloop()
"""