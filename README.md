# Water Bill Calculator

This is a straightforward water bill calculator application with a Tkinter GUI and SQLite database integration.

## Overview

### WaterBill Class

The `WaterBill` class encapsulates the core application logic for calculating water bills and managing interactions with the SQLite database.

#### Attributes

- `customer_name: str`
- `address: str`
- `email: str`
- `consumption: float`
- `current_reading: float`
- `previous_reading: float`
- `meter_consumption: float`
- `bill_amount_php: float`

#### Methods

- `calculate_bill()`: Computes the water bill based on user input.
- `save_to_database()`: Persists data to the SQLite database.
- `display_saved_data()`: Retrieves and displays saved data from the database.
- `show_details(row: Tuple)`: Presents details of a specific entry.

### Tkinter Class

The `Tkinter` class manages the graphical user interface using the Tkinter library.

#### Components

- `root`: The primary Tkinter window.
- Labels, Entries, and Buttons: Various Tkinter widgets for user input and interaction.

#### Associations

- The `WaterBill` class interacts with Tkinter widgets for user input.
- The `WaterBill` class triggers the creation of new Tkinter windows (`Toplevel`) for displaying details.

## UML Diagram

```
+------------------+          +-----------------+
|   WaterBill      |          |     Tkinter     |
+------------------+          +-----------------+
| - customer_name  |          |                 |
| - address        |          |                 |
| - email          |          |                 |
| - consumption    |          | +--------+      |
| - current_reading|          | |  root  |      |
| - previous_readin|          | +--------+      |
| - meter_consumpti|          | | Labels |      |
| - bill_amount_php|          | | Entries|      |
+------------------+          | | Buttons|      |
| + calculate_bill | -------->| +--------+      |
| + save_to_databa | -------->| |   ...  |      |
| + display_saved_ | -------->| +--------+      |
| + show_details(r)|          |                 |
+------------------+          +-----------------+

## How to Use

1. Ensure you have Python installed on your machine.
2. Run the water_bill_calculator.py script.
3. Input customer details, meter readings, and consumption.
4. Click "Calculate Bill" to see the calculated water bill.
5. Click "Histories" to view saved water bill data.
