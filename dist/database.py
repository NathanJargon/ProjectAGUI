import sqlite3
import warnings
warnings.filterwarnings("ignore")

class Database:
    def __init__(self, db_path="db/water_bill_database.db"): #add _internal/ if build
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS water_bills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT,
                address TEXT,
                account TEXT,
                meter TEXT,
                reference TEXT,
                due TEXT,
                bill_date TEXT,
                bill_period TEXT,
                soa TEXT,
                bill TEXT,
                rdg_date_time TEXT,
                current_reading REAL,
                previous_reading REAL,
                type TEXT,
                meter_consumption REAL,
                bill_amount_php REAL,
                message TEXT,
                water_charges REAL,
                vat REAL,
                dues REAL,
                others REAL
            )
        ''')

        self.cursor.execute("PRAGMA table_info(water_bills)")
        columns = [column[1] for column in self.cursor.fetchall()]
        if 'messages' not in columns:
            self.cursor.execute("ALTER TABLE water_bills ADD COLUMN messages TEXT")

        self.conn.commit()

    def save_to_database(self, customer_name, address, account, meter, reference, due, bill_date, 
                bill_period, soa, bill, rdg_date_time, current_reading, previous_reading, 
                type, meter_consumption, bill_amount_php, message, water_charges, vat, dues, others):
        self.cursor.execute('''
            INSERT INTO water_bills (
                customer_name,
                address,
                account,
                meter,
                reference,
                due,
                bill_date,
                bill_period,
                soa,
                bill,
                rdg_date_time,
                current_reading,
                previous_reading,
                type,
                meter_consumption,
                bill_amount_php,
                message,
                water_charges,
                vat,
                dues,
                others
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (customer_name, address, account, meter, reference, due, bill_date, 
                bill_period, soa, bill, rdg_date_time, current_reading, previous_reading, 
                type, meter_consumption, bill_amount_php, message, water_charges, vat, dues, others))

        self.conn.commit()

    def fetch_data(self):
        self.cursor.execute('SELECT * FROM water_bills')
        data = self.cursor.fetchall()
        return data

    def delete_and_clear(self, id):
        self.cursor.execute("DELETE FROM water_bills WHERE id = ?", (id,))
        self.conn.commit()

    def update_user_details(self, user_id, updated_user_details):
        self.cursor.execute('''
            UPDATE water_bills
            SET 
                customer_name = ?,
                address = ?,
                account = ?,
                meter = ?,
                reference = ?,
                due = ?,
                bill_date = ?,
                bill_period = ?,
                soa = ?,
                bill = ?,
                rdg_date_time = ?,
                current_reading = ?,
                previous_reading = ?,
                type = ?,
                meter_consumption = ?,
                bill_amount_php = ?,
                message = ?,
                water_charges = ?,
                vat = ?,
                dues = ?,
                others = ?
            WHERE id = ?
        ''', (
            updated_user_details['Customer Name'],
            updated_user_details['Address'],
            updated_user_details['Account Number'],
            updated_user_details['Meter Number'],
            updated_user_details['Reference Number'],
            updated_user_details['Due Date'],
            updated_user_details['Bill Date'],
            updated_user_details['Bill Period'],
            updated_user_details['SOA Number'],
            updated_user_details['Bill Number'],
            updated_user_details['Rdg Date/Time'],
            updated_user_details['Current Reading'],
            updated_user_details['Previous Reading'],
            updated_user_details['Customer Type'],
            updated_user_details['Meter Consumption'],
            updated_user_details['Bill Amount PHP'],
            updated_user_details['Message'],
            updated_user_details['Water Charges'],
            updated_user_details['Value-added Tax'],
            updated_user_details['Dues'],
            updated_user_details['Others'],
            user_id
        ))

        self.conn.commit()