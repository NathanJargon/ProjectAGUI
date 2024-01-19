from tkinter import messagebox, PhotoImage, Toplevel, Label, Entry, Button, Frame
from PIL import Image, ImageTk
from customtkinter import *
from database import Database
import customtkinter as ctk
import tkinter as tk
import warnings
import sqlite3
warnings.filterwarnings("ignore")


class Result:
    def __init__(self, root, service_info_var, billing_summary_var, current_charges_var, current_charges_var2, title_service, title_billing, id=None):
        self.root = root
        self.service_info_var = service_info_var
        self.entry_fields = {}
        self.billing_summary_var = billing_summary_var
        self.title_service = title_service
        self.title_billing = title_billing
        self.current_charges_var = current_charges_var
        self.current_charges_var2 = current_charges_var2
        #self.db_path = "_internal/db/water_bill_database.db"
        self.db_path = "db/water_bill_database.db"
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.currentId = 0 if None else id

        """
        service_info_converted = self.service_info_var.encode("utf-8")
        billing_summary_converted = self.billing_summary_var.encode("utf-8")
        service_info_split = self.service_info_converted.split()
        for row in self.service_info_split:
            service_info_split = row.split("\n")
            
        service_info_split = service_info_split.replace('', '\n')
        
        print(service_info_split)
        print(self.service_info_var)
        print(self.billing_summary_var)
        """
        
        self.details_frame = CTkFrame(self.root, fg_color="gray12", corner_radius=0)
        self.details_frame.place(relx=.18, rely=0, relwidth=0.9, relheight=1, anchor='nw')
        
        self.details_frame.columnconfigure(0, weight=1)
        self.details_frame.rowconfigure(0, weight=1)
        
        #self.label_name = CTkLabel(self.title_frame, text="Information", font=("Oswald", 25))
        #self.label_name.grid(row=0, column=0, padx=0, pady=10)

        self.service_frame = tk.Frame(self.root, width=500, height=300, bg="gray12")
        self.billing_frame = tk.Frame(self.root, width=500, height=300, bg="gray12")
        self.current_charges_frame = tk.Frame(self.root, width=500, height=300, bg="gray12")
        
        self.service_frame.place(x=355, y=200, width=500, height=250)
        self.billing_frame.place(x=1050, y=200, width=500, height=350)
        self.current_charges_frame.place(x=355, y=450, width=1200, height=260)

        self.title_frame = CTkFrame(self.details_frame, fg_color="gray12")
        self.title_frame.grid(padx=10, pady=(20, 0))

        #image = Image.open("_internal/img/logo.png")
        image = Image.open("img/logo.png")
        image = image.resize((150, 150), Image.BICUBIC)
        photo = ImageTk.PhotoImage(image)
        title_label = ctk.CTkButton(self.title_frame, image=photo, text="AGUI WATER DISTRICT CO.\n  Grand Garden Office, Harlson Street\nCagayan de Oro, Philippines 9000\n      VAT Reg. TIN: 002-152-512-412-000", 
                                    bg_color="gray12", fg_color="gray12", hover_color="gray12", font=("Oswald", 15))
        title_label.image = image
        title_label.grid(padx=(175, 0), pady=(0,0), sticky='nsew')
        
        if self.currentId:
            #edit_image = Image.open("_internal/img/button2.png") 
            edit_image = Image.open("img/button2.png")
            edit_image = edit_image.resize((50, 50), Image.BICUBIC)
            edit_photo = ImageTk.PhotoImage(edit_image)
            
            edit_button = CTkButton(self.root, image=edit_photo, text="Edit", font=("Oswald", 15, "bold"), text_color="white", fg_color="gray12", bg_color="gray12", hover_color="gray12", command=lambda: self.edit_user_details(self.currentId))
            edit_button.image = edit_photo
            edit_button.place(x=1150, y=0)


        self.service_info_label = CTkLabel(self.service_frame, textvariable=self.service_info_var, justify=tk.LEFT, font=("Oswald", 15), 
                                           bg_color="gray12", 
                                           fg_color="gray12")
        self.billing_info_label = CTkLabel(self.billing_frame, textvariable=self.billing_summary_var, justify=tk.LEFT, font=("Oswald", 15), 
                                           bg_color="gray12", 
                                           fg_color="gray12")
        self.current_charges_label = CTkLabel(self.current_charges_frame, textvariable=self.current_charges_var, justify=tk.LEFT, font=("Oswald", 15), 
                                           bg_color="gray12", 
                                           fg_color="gray12")
        self.current_charges_label2 = CTkLabel(self.current_charges_frame, textvariable=self.current_charges_var2, justify=tk.LEFT, font=("Oswald", 15), 
                                           bg_color="gray12", 
                                           fg_color="gray12")
        self.title_service_label = CTkLabel(self.root, textvariable=self.title_service, justify=tk.LEFT, font=("Oswald", 20, "bold"), 
                                           bg_color="gray12", 
                                           fg_color="gray12")
        self.title_billing_label = CTkLabel(self.root, textvariable=self.title_billing, justify=tk.LEFT, font=("Oswald", 20, "bold"), 
                                           bg_color="gray12", 
                                           fg_color="gray12")

        self.service_line_frame = tk.Frame(self.root, bg="gray12")
        self.service_line = CTkLabel(self.service_line_frame, text="__________________________________________________________________________________________________________________________________________________", bg_color="gray12", fg_color="gray12", font=("Oswald", 20, "bold"))
        self.service_line.pack()
        self.service_line_frame.place(x=289, y=140)
        
        self.service_info_label.pack(padx=(10, 50), pady=0)
        self.billing_info_label.pack(padx=(35, 10), pady=0)
        self.current_charges_label.place(x=250, y=40)
        self.current_charges_label2.place(x=500, y=40)
        self.title_service_label.place(x=670, y=140)
        self.title_billing_label.place(x=680, y=360)
        
        self.line_frame = tk.Frame(self.root, bg="gray12")
        self.line_label = CTkLabel(self.line_frame, text="__________________________________________________________________________________________________________________________________________________", bg_color="gray12", fg_color="gray12", font=("Oswald", 20, "bold"))
        self.line_label.pack()
        self.line_frame.place(x=289, y=420)
                
        self.reminder_frame = tk.Frame(self.root, bg="gray12")
        self.reminder_label = CTkLabel(self.reminder_frame, text="REMINDER", font=("Oswald", 24, "bold"))
        self.reminder_label.pack()
        self.reminder_frame.place(x=400, y=730)

        self.reminder_line_frame = tk.Frame(self.root, bg="gray12")
        self.reminder_line_label = CTkLabel(self.reminder_line_frame, text="__________________________________________________________________________________________________________________________________________________", bg_color="gray12", fg_color="gray12", font=("Oswald", 20, "bold"))
        self.reminder_line_label.pack()
        self.reminder_line_frame.place(x=289, y=700)
        
        # Always use a single way to display widgets
        
        self.title_frame.pack(fill=tk.BOTH, expand=True)

        title_label = CTkLabel(self.title_frame,
            text="* Please disregard statement if payment has been made.\n* This serves as your notice of disconnection if current account remains unpaid ten (days) after due date.\n* A penalty charge of 10% will be added to your previous balance.\n* The above computation is only an estimate of your water bill.\n* In case there is a discrepancy between the estimated rate and your water bill, your water bill will take precedence.",
            bg_color="gray12", fg_color="gray12", font=("Oswald", 13, "bold"), justify=tk.LEFT)
        title_label.grid(padx=(295, 0), pady=(470,0), sticky='nsew')


    # For editing user data
    
    def edit_user_details(self, user_id):
        user_details = self.fetch_user_details_from_database(user_id)

        edit_window = Toplevel(self.root)
        edit_window.configure(background='gray12')
        edit_window.resizable(False, False)
        edit_window.geometry('+150+100')
        edit_window.title('Edit User Details')

        user_details_items = list(user_details.items())
        self.entry_fields = {}
        for i in range(0, len(user_details_items), 2):
            for j in range(2):
                if i + j < len(user_details_items):
                    key, value = user_details_items[i + j]
                    Label(edit_window, text=key, background='gray12', foreground='white', font=('Oswald', 15)).grid(row=i//2, column=j*2, padx=10, pady=10)
                    entry = ctk.CTkEntry(edit_window, bg_color='gray12', fg_color='gray12', text_color="white", font=('Oswald', 15))
                    entry.insert(0, ' ' + str(value))
                    entry.grid(row=i//2, column=j*2+1, padx=10, pady=10)
                    self.entry_fields[key] = entry

        save_button = Button(edit_window, text="Save", command=lambda: self.save_user_details(user_id, edit_window), 
                            background='gray12', foreground='white', font=('Oswald', 15), relief=tk.RAISED)
        save_button.grid(row=i//2+1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')


    def fetch_user_details_from_database(self, user_id):
        self.cursor.execute("SELECT * FROM water_bills WHERE id=?", (user_id,))
        user_details = self.cursor.fetchone()

        user_details_dict = {
            "Customer Name": user_details[1],
            "Address": user_details[2],
            "Account Number": user_details[3],
            "Meter Number": user_details[4],
            "Reference Number": user_details[5],
            "Due Date": user_details[6],
            "Bill Date": user_details[7],
            "Bill Period": user_details[8],
            "SOA Number": user_details[9],
            "Bill Number": user_details[10],
            "Rdg Date/Time": user_details[11],
            "Current Reading": user_details[12],
            "Previous Reading": user_details[13],
            "Customer Type": user_details[14],
            "Meter Consumption": user_details[15],
            "Bill Amount PHP": user_details[16],
            "Message": user_details[17],
            "Water Charges": user_details[18],
            "Value-added Tax": user_details[19],
            "Dues": user_details[20],
            "Others": user_details[21]
        }

        return user_details_dict

    def save_user_details(self, user_id, edit_window):
        updated_user_details = {key: entry.get().strip() for key, entry in self.entry_fields.items()}

        db = Database()
        db.update_user_details(user_id, updated_user_details)

        edit_window.destroy()
            
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

    bill_details_var = tk.StringVar()
    billing_summary_var = tk.StringVar()
    title_service = tk.StringVar()
    title_billing = tk.StringVar()
    current_charges_var = tk.StringVar()
    current_charges_var2 = tk.StringVar()
    result = Result(root, bill_details_var, billing_summary_var, current_charges_var, current_charges_var2, title_service, title_billing)
    root.mainloop()
"""