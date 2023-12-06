import tkinter as tk
from tkinter import messagebox
import sqlite3

def calculate_bill():
    try:
        # Get user input
        customer_name = entry_name.get()
        address = entry_address.get()
        email = entry_email.get()
        consumption = float(entry_consumption.get())

        if not email.endswith("@gmail"):
            raise ValueError("Invalid email address")
        
        bill_amount_php = consumption * 10

        if consumption < 50:
            message = "Great job on conserving water! Keep it up."
        elif consumption < 100:
            message = "You're using a moderate amount of water. Consider more water-saving habits."
        else:
            message = "Please be mindful of your water usage. Consider implementing water-saving tips."

        # Create a custom dialog to display the water bill and message
        bill_details = f"Customer Name: {customer_name}\n"
        bill_details += f"Address: {address}\n"
        bill_details += f"Email: {email}\n"
        bill_details += f"Consumption: {consumption} gallons\n"
        bill_details += f"Total Bill Amount (in PHP): ₱{bill_amount_php:.2f}\n\n"
        bill_details += f"Message: {message}"

        custom_dialog = tk.Toplevel(root)
        custom_dialog.title("Water Bill Details")
        custom_dialog.geometry("500x250")

        details_label = tk.Label(custom_dialog, text=bill_details, justify=tk.LEFT)
        details_label.pack(padx=10, pady=10)

    except ValueError as e:
        # Handle invalid input (non-numeric consumption or invalid email)
        if str(e) == "Invalid email address":
            messagebox.showerror("Error", "Please enter a valid email address.")
        else:
            messagebox.showerror("Error", "Please enter a valid consumption value.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Water Bill Calculator")

# Create and place widgets in the window
label_name = tk.Label(root, text="Customer Name:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_address = tk.Label(root, text="Address:")
label_address.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entry_address = tk.Entry(root)
entry_address.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email (Must end with @gmail):")
label_email.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_consumption = tk.Label(root, text="Consumption (gallons):")
label_consumption.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

entry_consumption = tk.Entry(root)
entry_consumption.grid(row=3, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate Bill", command=calculate_bill)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
