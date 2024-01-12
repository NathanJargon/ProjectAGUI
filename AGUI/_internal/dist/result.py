from tkinter import messagebox
from customtkinter import *
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

        self.title_frame = CTkFrame(self.details_frame, fg_color="gray12")
        self.title_frame.pack(padx=10, pady=(20, 0))

        #self.label_name = CTkLabel(self.title_frame, text="Information", font=("Oswald", 25))
        #self.label_name.grid(row=0, column=0, padx=0, pady=10)

        self.service_frame = tk.Frame(self.root, width=500, height=300, bg="gray12")
        self.billing_frame = tk.Frame(self.root, width=500, height=300, bg="gray12")

        self.service_frame.place(x=255, y=90, width=400, height=300)
        self.billing_frame.place(x=575, y=90, width=500, height=700)

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

        # Use grid instead of pack for title_service_label and title_billing_label
        self.title_service_label.grid(row=0, column=0, padx=65, pady=0, sticky="w")
        self.title_billing_label.grid(row=0, column=1, padx=(45, 0), pady=0, sticky="e")

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

    bill_details_var = tk.StringVar()
    result = Result(root, bill_details_var)
    root.mainloop()
"""