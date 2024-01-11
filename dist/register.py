from tkinter import messagebox, StringVar
from customtkinter import *
from database import Database
import tkinter as tk
import result
import warnings
warnings.filterwarnings("ignore")


class Register(result.Result):
    def __init__(self, root):
        self.root = root
        #self.db_path = "db/water_bill_database.db"
        self.db_path = "_internal/db/water_bill_database.db"
        self.db = Database(self.db_path)

        self.service_info_var = StringVar()
        self.billing_summary_var = StringVar()
        self.title_service = StringVar()
        self.title_billing = StringVar()
        
        self.background_frame = CTkFrame(root, fg_color="gray12", corner_radius=0)
        self.background_frame.place(relx=.18, rely=0, relwidth=.9, relheight=1, anchor='nw')

        # Service Information
        # Problem #1: Grid and pack will conflict each other.
        # Solution: Use grid instead of pack.
        
        self.service_frame = CTkFrame(self.background_frame, fg_color="gray12")
        self.service_frame.grid(row=0, column=0, sticky='w', padx=(10, 0), pady=25)

        self.title_frame = CTkFrame(self.background_frame, fg_color="gray12")
        self.title_frame.grid(row=1, column=0, padx=0, pady=5)

        self.label_name1 = CTkLabel(self.service_frame, text="Service Information", font=("Oswald", 20))
        self.label_name1.grid(row=0, column=0, padx=0, pady=(0, 10))

        self.name_frame = CTkFrame(self.service_frame)
        self.name_frame.grid(row=1, column=0, padx=10, pady=5)

        self.label_name = CTkLabel(self.name_frame, text="Customer Name:", font=("Oswald", 14))
        self.label_name.grid(row=0, column=0, padx=(10, 40), pady=5)

        self.entry_name = CTkEntry(self.name_frame, width=150)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.address_frame = CTkFrame(self.service_frame)
        self.address_frame.grid(row=2, column=0, padx=5, pady=5)

        self.label_address = CTkLabel(self.address_frame, text="Address:", font=("Oswald", 14))
        self.label_address.grid(row=0, column=0, padx=(10, 85), pady=5)
        
        self.entry_address = CTkEntry(self.address_frame, width=150)
        self.entry_address.grid(row=0, column=1, padx=10, pady=5)
        self.entry_address.insert(0, "Bldg/Rm/Flr")
        
        self.account_frame = CTkFrame(self.service_frame)
        self.account_frame.grid(row=3, column=0, padx=10, pady=5)

        self.label_account = CTkLabel(self.account_frame, text="Account Number:", font=("Oswald", 14))
        self.label_account.grid(row=0, column=0, padx=(10, 38), pady=5)
        
        self.entry_account = CTkEntry(self.account_frame, width=150)
        self.entry_account.grid(row=0, column=1, padx=10, pady=5)
        self.entry_account.insert(0, "N/A if None")
        
        self.meter_frame = CTkFrame(self.service_frame)
        self.meter_frame.grid(row=4, column=0, padx=10, pady=5)

        self.label_meter = CTkLabel(self.meter_frame, text="Meter Number:", font=("Oswald", 14))
        self.label_meter.grid(row=0, column=0, padx=(10, 48), pady=5)

        self.entry_meter = CTkEntry(self.meter_frame, width=150)
        self.entry_meter.grid(row=0, column=1, padx=10, pady=5)

        self.reference_frame = CTkFrame(self.service_frame)
        self.reference_frame.grid(row=5, column=0, padx=10, pady=5)

        self.label_reference = CTkLabel(self.reference_frame, text="Reference Number:", font=("Oswald", 14))
        self.label_reference.grid(row=0, column=0, padx=(10, 25), pady=5)

        self.entry_reference = CTkEntry(self.reference_frame, width=150)
        self.entry_reference.grid(row=0, column=1, padx=10, pady=5)

        self.rate_frame = CTkFrame(self.service_frame)
        self.rate_frame.grid(row=6, column=0, padx=10, pady=5)

        self.label_rate = CTkLabel(self.rate_frame, text="Rate Per Cubic Meter:", font=("Oswald", 14))
        self.label_rate.grid(row=0, column=0, padx=10, pady=5)

        self.entry_rate = CTkEntry(self.rate_frame, width=150)
        self.entry_rate.grid(row=0, column=1, padx=10, pady=5)
        self.entry_rate.insert(0, "0 if None")

        self.charges_frame = CTkFrame(self.service_frame)
        self.charges_frame.grid(row=7, column=0, padx=10, pady=5)

        self.label_charges = CTkLabel(self.charges_frame, text="Charges/Dues:", font=("Oswald", 14))
        self.label_charges.grid(row=0, column=0, padx=(10, 50), pady=5)

        self.entry_charges = CTkEntry(self.charges_frame, width=150)
        self.entry_charges.grid(row=0, column=1, padx=10, pady=5)
        self.entry_charges.insert(0, "0")
        
        # BUTTON
        
        self.buttom_frame = CTkFrame(self.service_frame, fg_color="gray12")
        self.buttom_frame.grid(row=8, column=0, padx=0, pady=15)

        self.calculate_button = CTkButton(self.buttom_frame, text="Calculate Bill", command=self.calculate_bill, font=("Oswald", 15))
        self.calculate_button.grid(row=0, column=0, padx=10, pady=5)


        # Billing Summary
        
        self.billing_frame = CTkFrame(self.background_frame, fg_color="gray12")
        self.billing_frame.grid(row=0, column=1, sticky='w', pady=(10, 47))

        self.label_name2 = CTkLabel(self.billing_frame, text="Billing Summary", font=("Oswald", 20))
        self.label_name2.grid(row=0, column=0, padx=0, pady=(10, 10))
    
        self.billdate_frame = CTkFrame(self.billing_frame)
        self.billdate_frame.grid(row=2, column=0, padx=5, pady=5)

        self.label_billdate = CTkLabel(self.billdate_frame, text="Billing Date:", font=("Oswald", 14))
        self.label_billdate.grid(row=0, column=0, padx=(10, 68), pady=5)

        self.entry_billdate = CTkEntry(self.billdate_frame, width=150)
        self.entry_billdate.grid(row=0, column=1, padx=10, pady=5)
        self.entry_billdate.insert(0, "YYYY-MM-DD")

        self.billperiod_frame = CTkFrame(self.billing_frame)
        self.billperiod_frame.grid(row=3, column=0, padx=5, pady=5)

        self.label_billperiod= CTkLabel(self.billperiod_frame, text="Billing Period:", font=("Oswald", 14))
        self.label_billperiod.grid(row=0, column=0, padx=10, pady=5)

        self.entry_billperiod = CTkEntry(self.billperiod_frame, width=200)
        self.entry_billperiod.grid(row=0, column=1, padx=10, pady=5)
        self.entry_billperiod.insert(0, "YYYY-MM-DD to YYYY-MM-DD")

        self.soa_frame = CTkFrame(self.billing_frame)
        self.soa_frame.grid(row=5, column=0, padx=5, pady=5)

        self.label_soa= CTkLabel(self.soa_frame, text="SOA Number:", font=("Oswald", 14))
        self.label_soa.grid(row=0, column=0, padx=(10, 63), pady=5)

        self.entry_soa = CTkEntry(self.soa_frame, width=150)
        self.entry_soa.grid(row=0, column=1, padx=10, pady=5)

        self.bill_frame = CTkFrame(self.billing_frame)
        self.bill_frame.grid(row=6, column=0, padx=5, pady=5)

        self.label_bill= CTkLabel(self.bill_frame, text="Bill Number:", font=("Oswald", 14))
        self.label_bill.grid(row=0, column=0, padx=(10, 68), pady=5)

        self.entry_bill = CTkEntry(self.bill_frame, width=150)
        self.entry_bill.grid(row=0, column=1, padx=10, pady=5)

        self.rdg_frame = CTkFrame(self.billing_frame)
        self.rdg_frame.grid(row=7, column=0, padx=5, pady=5)

        self.label_rdg = CTkLabel(self.rdg_frame, text="Rdg Date/Time:", font=("Oswald", 14))
        self.label_rdg.grid(row=0, column=0, padx=(10, 20), pady=5)

        self.entry_rdg = CTkEntry(self.rdg_frame, width=180)
        self.entry_rdg.grid(row=0, column=1, padx=10, pady=5) 
        self.entry_rdg.insert(0, "YYYY-MM-DD 00:00:00 UTC")
        
        self.label_current_reading_frame = CTkFrame(self.billing_frame)
        self.label_current_reading_frame.grid(row=8, column=0, padx=5, pady=5)

        self.label_current_reading = CTkLabel(self.label_current_reading_frame, text="Pres Reading (cms):", font=("Oswald", 14))
        self.label_current_reading.grid(row=0, column=0, padx=(10, 76), pady=5)

        self.entry_current_reading = CTkEntry(self.label_current_reading_frame, width=100)
        self.entry_current_reading.grid(row=0, column=1, padx=10, pady=5)
        self.entry_current_reading.insert(0, "0")

        self.label_previous_reading_frame = CTkFrame(self.billing_frame)
        self.label_previous_reading_frame.grid(row=9, column=0, padx=5, pady=5)

        self.label_previous_reading = CTkLabel(self.label_previous_reading_frame, text="Prev Reading (cms):", font=("Oswald", 14))
        self.label_previous_reading.grid(row=0, column=0, padx=(10, 76), pady=5)

        self.entry_previous_reading = CTkEntry(self.label_previous_reading_frame, width=100)
        self.entry_previous_reading.grid(row=0, column=1, padx=10, pady=5)
        self.entry_previous_reading.insert(0, "0")

        self.consumption_frame = CTkFrame(self.billing_frame)
        self.consumption_frame.grid(row=10, column=0, padx=5, pady=5)

        self.label_consumption = CTkLabel(self.consumption_frame, text="Consumption:", font=("Oswald", 14))
        self.label_consumption.grid(row=0, column=0, padx=(10, 110), pady=5)

        self.entry_consumption = CTkEntry(self.consumption_frame, width=100)
        self.entry_consumption.grid(row=0, column=1, padx=10, pady=5)
        self.entry_consumption.insert(0, "0")
        
    def calculate_bill(self):
        try:
            customer_name = self.entry_name.get()[:11] if ' ' not in self.entry_name.get() else self.entry_name.get().split(' ')[0]
            address = self.entry_address.get()[:30] if len(self.entry_address) > 30 else self.entry_address.get()
            account = self.entry_account.get()
            meter = self.entry_meter.get()
            reference = self.entry_reference.get()
            rate = float(self.entry_rate.get())
            charges = float(self.entry_charges.get())
            bill_date = self.entry_billdate.get()
            bill_period = self.entry_billperiod.get()
            soa = self.entry_soa.get()
            bill = self.entry_bill.get()
            rdg_date_time = self.entry_rdg.get()
            current_reading = float(self.entry_current_reading.get())
            previous_reading = float(self.entry_previous_reading.get())
            consumption = float(self.entry_consumption.get())
            meter_consumption = current_reading - previous_reading
            message = ""
            
            bill_amount_php = (charges + consumption) + (meter_consumption * 2.5)

            if meter_consumption < 0:
                raise ValueError("Invalid meter consumption")
            
            if len(bill_date) != 10:
                raise ValueError("Invalid bill date")
            
            if len(bill_period) != 24:
                raise ValueError("Invalid bill period")
            
            if meter_consumption < 50:
                message = "Great job on conserving water! Keep it up.\n"
            elif meter_consumption < 100:
                message = "You're using a moderate amount of water. Consider more water-saving habits."
            else:
                message = "Please be mindful of your water usage. Consider implementing water-saving tips."

            #print(customer_name, address, account, meter, reference, rate, consumption, bill_date, bill_period, rdg_date_time, current_reading, previous_reading, meter_consumption, bill_amount_php, message)

            self.db.save_to_database(customer_name, address, account, meter, reference, rate, charges, bill_date, 
                bill_period, soa, bill, rdg_date_time, current_reading, previous_reading, 
                consumption, meter_consumption, bill_amount_php, message)
            
            self.db.fetch_data()

            title1 = ""
            title1 += f"SERVICE INFORMATION\n"
           
            service_info = ""
            service_info += f"Customer Name: {customer_name}\n"
            service_info += f"Address: {address}\n"
            service_info += f"Account Number: {account}\n"
            service_info += f"Meter Number: {meter}\n"
            service_info += f"Reference Number: {reference}\n"
            service_info += f"Rate per Cubic Meter: {rate}\n"
            service_info += f"Charges/Dues: {charges}"

            title2 = ""
            title2 += f"BILLING SUMMARY\n"
        
            billing_summary = ""
            billing_summary += f"Billing Date: {bill_date}\n"
            billing_summary += f"Billing Period: {bill_period}\n"
            billing_summary += f"SOA Number: {soa}\n"
            billing_summary += f"Billing Number: {bill}\n"
            billing_summary += f"Rdg Date/Time: {rdg_date_time}\n"
            billing_summary += f"Current Reading: {current_reading}\n"
            billing_summary += f"Previous Reading: {previous_reading}\n"
            billing_summary += f"Consumption: {consumption}\n"
            billing_summary += f"Meter Consumption: {meter_consumption} gallons\n\n"
            billing_summary += f"Total Bill Amount (in PHP): ₱{bill_amount_php:.2f}\n"
            billing_summary += f"Message: {message}"
            
            for widget in self.background_frame.winfo_children():
                widget.destroy()

            self.title_service.set(title1)
            self.title_billing.set(title2)

            self.service_info_var.set(service_info)
            self.billing_summary_var.set(billing_summary)

            result_info = result.Result(self.root, self.service_info_var, self.billing_summary_var, self.title_service, self.title_billing)

            
        except ValueError as e:
            match str(e): # Switch for more efficient use-case
                case "Invalid meter consumption":
                    messagebox.showerror("Error", "Please enter a valid pres and prev reading!")
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

    w = 854
    h = 480

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

    register = Register(root)
    root.mainloop()
"""