from tkinter import messagebox
from PIL import Image, ImageTk
from customtkinter import *
import customtkinter as ctk
import tkinter as tk
import warnings
warnings.filterwarnings("ignore")


class Result:
    def __init__(self, root, service_info_var, billing_summary_var, title_service, title_billing):
        self.root = root
        self.service_info_var = service_info_var
        self.billing_summary_var = billing_summary_var
        self.title_service = title_service
        self.title_billing = title_billing

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
        
        self.title_frame = CTkFrame(self.details_frame, fg_color="gray12")
        self.title_frame.grid(padx=10, pady=(20, 0))

        image = Image.open("_internal/img/logo.png")
        #image = Image.open("img/logo.png")
        image = image.resize((200, 200), Image.BICUBIC)
        photo = ImageTk.PhotoImage(image)
        title_label = ctk.CTkButton(self.title_frame, image=photo, text="AGUI WATER DISTRICT CO.\n  Grand Garden Office, Harlson Street\nCagayan de Oro, Philippines 9000\n      VAT Reg. TIN: 002-152-512-412-000", 
                                    bg_color="gray12", fg_color="gray12", hover_color="gray12", font=("Oswald", 15))
        title_label.image = image
        title_label.grid(padx=(175, 0), pady=(0,0), sticky='nsew')
        
        #self.label_name = CTkLabel(self.title_frame, text="Information", font=("Oswald", 25))
        #self.label_name.grid(row=0, column=0, padx=0, pady=10)

        self.service_frame = tk.Frame(self.root, width=500, height=300, bg="gray10")
        self.billing_frame = tk.Frame(self.root, width=500, height=300, bg="gray11")

        self.service_frame.place(x=355, y=300, width=400, height=300)
        self.billing_frame.place(x=575, y=300, width=500, height=300)

        self.service_info_label = CTkLabel(self.service_frame, textvariable=self.service_info_var, justify=tk.LEFT, font=("Oswald", 15), 
                                           bg_color="gray12", 
                                           fg_color="gray12", wraplength=250)
        self.billing_info_label = CTkLabel(self.billing_frame, textvariable=self.billing_summary_var, justify=tk.LEFT, font=("Oswald", 15), 
                                           bg_color="gray12", 
                                           fg_color="gray12", wraplength=250)
        self.title_service_label = CTkLabel(self.title_frame, textvariable=self.title_service, justify=tk.LEFT, font=("Oswald", 25, "underline"), 
                                           bg_color="gray12", 
                                           fg_color="gray12")
        self.title_billing_label = CTkLabel(self.title_frame, textvariable=self.title_billing, justify=tk.LEFT, font=("Oswald", 25, "underline"), 
                                           bg_color="gray12", 
                                           fg_color="gray12")

        self.service_info_label.pack(padx=(10, 70), pady=10)
        self.billing_info_label.pack(padx=(35, 10), pady=10)

        # Use grid instead of pack for title_service_label and title_billing_label
        # Pack the title_frame with fill and expand parameters
        self.title_frame.pack(fill=tk.BOTH, expand=True)

        self.title_service_label.grid(row=0, column=0, padx=65, pady=0, sticky="w")
        self.title_billing_label.grid(row=0, column=1, padx=(45, 0), pady=0, sticky="e")

        title_label = CTkLabel(self.title_frame,
            text="REMINDERS\n* Please disregard statement if payment has been made.\n* This serves as your notice of disconnection if current account remains unpaid ten (days) after due date.\n* A penalty charge of 10% will be added to your previous balance.\n* The above computation is only an estimate of your water bill.\n* In case there is a discrepancy between the estimated rate and your water bill, your water bill will take precedence.",
            bg_color="gray12", fg_color="gray12", font=("Oswald", 13), justify=tk.LEFT)
        title_label.grid(padx=(295, 0), pady=(400,0), sticky='nsew')
        
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
    result = Result(root, bill_details_var, billing_summary_var, title_service, title_billing)
    root.mainloop()