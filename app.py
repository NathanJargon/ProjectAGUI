import tkinter as tk
from tkinter import messagebox

def calculate_bill():
    try:
        # Get user input
        customer_name = entry_name.get()
        consumption = float(entry_consumption.get())

        # Calculate bill amount (you can customize this calculation)
        bill_amount = consumption * 0.05  # Replace with your own calculation

        # Determine a message based on consumption
        if consumption < 50:
            message = "Great job on conserving water! Keep it up."
        elif consumption < 100:
            message = "You're using a moderate amount of water. Consider more water-saving habits."
        else:
            message = "Please be mindful of your water usage. Consider implementing water-saving tips."

        # Create a custom dialog to display the water bill and message
        bill_details = f"Customer Name: {customer_name}\n"
        bill_details += f"Consumption: {consumption} gallons\n"
        bill_details += f"Total Bill Amount: ${bill_amount:.2f}\n\n"
        bill_details += f"Message: {message}"

        custom_dialog = tk.Toplevel(root)
        custom_dialog.title("Water Bill Details")
        custom_dialog.geometry("500x200")

        details_label = tk.Label(custom_dialog, text=bill_details, justify=tk.LEFT)
        details_label.pack(padx=10, pady=10)

    except ValueError:
        # Handle invalid input (non-numeric consumption)
        messagebox.showerror("Error", "Please enter a valid consumption value.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Water Bill Calculator")

# Create and place widgets in the window
label_name = tk.Label(root, text="Customer Name:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_consumption = tk.Label(root, text="Consumption (gallons):")
label_consumption.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entry_consumption = tk.Entry(root)
entry_consumption.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate Bill", command=calculate_bill)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
