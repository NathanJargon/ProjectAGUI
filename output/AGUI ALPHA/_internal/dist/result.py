import tkinter as tk
from customtkinter import *
import ast

class Result:
    def __init__(self, root, service_info_var, billing_summary_var):
        self.root = root
        self.service_info_var = service_info_var
        self.billing_summary_var = billing_summary_var

        #ToDo: customize each label of the informations
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
        self.title_frame.pack(padx=10, pady=5)

        self.label_name = CTkLabel(self.title_frame, text="Information", font=("Oswald", 25))
        self.label_name.grid(row=0, column=0, padx=0, pady=10)

        # Create two frames for service and billing information
        self.service_frame = CTkFrame(self.details_frame, fg_color="gray12")
        self.billing_frame = CTkFrame(self.details_frame, fg_color="gray12")

        # Place the frames side by side
        self.service_frame.pack(side=tk.LEFT, padx=100, pady=(10, 196))
        self.billing_frame.pack(side=tk.LEFT, padx=50, pady=10)

        # Create labels for service and billing information
        self.service_info_label = CTkLabel(self.service_frame, textvariable=self.service_info_var, justify=tk.LEFT, font=("Oswald", 12), 
                                           bg_color="gray12", 
                                           fg_color="gray12")
        self.billing_info_label = CTkLabel(self.billing_frame, textvariable=self.billing_summary_var, justify=tk.LEFT, font=("Oswald", 12), 
                                           bg_color="gray12", 
                                           fg_color="gray12", wraplength=250)

        # Pack the labels into their respective frames
        self.service_info_label.pack(padx=10, pady=10)
        self.billing_info_label.pack(padx=10, pady=10)
        
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