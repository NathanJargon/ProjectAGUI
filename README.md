# Water Bill Calculator

This is a straightforward water bill calculator application with a Tkinter GUI and SQLite database integration.

## Images

![Image 1](img/a.png)
![Image 2](img/a1.png)

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
+------------------------------------+
|        CTkFrame                    |
+------------------------------------+
| - root: CTk                        |
| - details_frame: CTkFrame          |
| - bill_details_var: tk.StringVar   |
|------------------------------------|
| + __init__()                       |
| + create_widgets()                 |
| + register_information()           |
| + histories_registered()           |
| + graphical_presentation()         |
| + login_button()                   |
+------------------------------------+
|         Sidebar                    |
+------------------------------------+
|        MainApplication             |
+------------------------------------+
| - create_widgets()                 |
+------------------------------------+
|        CTkFrame                    |
+------------------------------------+
| + __init__()                       |
| + create_graph()                   |
+------------------------------------+
|        GraphGenerator              |
+------------------------------------+
| - background_frame: GraphGenerator |
+------------------------------------+
```

## How to Use

1. Ensure you have Python installed on your machine.
2. Run the water_bill_calculator.py script.
3. Input customer details, meter readings, and consumption.
4. Click "Calculate Bill" to see the calculated water bill.
5. Click "Histories" to view saved water bill data.

## License

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs 4.0 International License.

You are free to:

- Share — copy and redistribute the material in any medium or format
The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:

- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

- NonCommercial — You may not use the material for commercial purposes.

- NoDerivatives — If you remix, transform, or build upon the material, you may not distribute the modified material.

- No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Notices:

- You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.

- No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.

