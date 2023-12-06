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

        # New: Get metering information
        current_reading = float(entry_current_reading.get())
        previous_reading = float(entry_previous_reading.get())
        meter_consumption = current_reading - previous_reading

        if not email.endswith("@gmail"):
            raise ValueError("Invalid email address")
        
        # New: Calculate bill amount based on meter consumption
        bill_amount_php = meter_consumption * 2.5

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
        bill_details += f"Consumption: {consumption} gallons\n\n"
        bill_details += f"Metering Information:\n"
        bill_details += f"Current Reading: {current_reading}\n"
        bill_details += f"Previous Reading: {previous_reading}\n"
        bill_details += f"Meter Consumption: {meter_consumption} gallons\n\n"
        bill_details += f"Billing Summary:\n"
        bill_details += f"Total Bill Amount (in PHP): ₱{bill_amount_php:.2f}\n\n"
        bill_details += f"Message: {message}"
        
                # Save data to the SQLite database
        save_to_database(customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php)

        # Create a custom dialog to display the water bill and message
        custom_dialog = tk.Toplevel(root)
        custom_dialog.title("Water Bill Details")

        # New: Center the custom dialog
        w = 800  # Width for the custom dialog
        h = 300  # Height for the custom dialog

        # Get the screen width and height
        ws = custom_dialog.winfo_screenwidth()
        hs = custom_dialog.winfo_screenheight()

        # Calculate x and y coordinates for the custom dialog window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        custom_dialog.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

        # New: Change the font and style for the details label
        details_label = tk.Label(custom_dialog, text=bill_details, justify=tk.LEFT, font=("Helvetica", 12), padx=10, pady=10)
        details_label.pack()

    except ValueError as e:
        # Handle invalid input (non-numeric consumption or invalid email)
        if str(e) == "Invalid email address":
            messagebox.showerror("Error", "Please enter a valid email address.")
        else:
            messagebox.showerror("Error", "Please enter valid numeric values for consumption and meter readings.")

# Function to save data to the SQLite database
def save_to_database(customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php):
    # Connect to the SQLite database (create one if it doesn't exist)
    conn = sqlite3.connect("water_bill_database.db")
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS water_bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            address TEXT,
            email TEXT,
            consumption REAL,
            current_reading REAL,
            previous_reading REAL,
            meter_consumption REAL,
            bill_amount_php REAL
        )
    ''')

    # Insert data into the table
    cursor.execute('''
        INSERT INTO water_bills (
            customer_name,
            address,
            email,
            consumption,
            current_reading,
            previous_reading,
            meter_consumption,
            bill_amount_php
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Function to display saved data from the SQLite database
def display_saved_data():
    # Connect to the SQLite database
    conn = sqlite3.connect("water_bill_database.db")
    cursor = conn.cursor()

    # Retrieve data from the table
    cursor.execute('SELECT * FROM water_bills')
    data = cursor.fetchall()

    # Close the connection
    conn.close()

    # Display the data in a new window
    if data:
        display_window = tk.Toplevel(root)
        display_window.title("Saved Water Bill Data")

        for row in data:
            row_text = ', '.join(str(value) for value in row)
            label = tk.Label(display_window, text=row_text, justify=tk.LEFT)
            label.pack(padx=10, pady=5)
    else:
        messagebox.showinfo("No Data", "No water bill data found in the database.")


# Create the main Tkinter window
root = tk.Tk()
root.title("Water Bill Calculator")

# New: Center the main window
w = 350  # Width for the main window
h = 240  # Height for the main window

# Get the screen width and height
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# Calculate x and y coordinates for the main window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

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

label_current_reading = tk.Label(root, text="Current Meter Reading:")
label_current_reading.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

entry_current_reading = tk.Entry(root)
entry_current_reading.grid(row=3, column=1, padx=10, pady=5)

label_previous_reading = tk.Label(root, text="Previous Meter Reading:")
label_previous_reading.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

entry_previous_reading = tk.Entry(root)
entry_previous_reading.grid(row=4, column=1, padx=10, pady=5)

label_consumption = tk.Label(root, text="Consumption (gallons):")
label_consumption.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

entry_consumption = tk.Entry(root)
entry_consumption.grid(row=5, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate Bill", command=calculate_bill)
calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
