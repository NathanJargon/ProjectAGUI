import sqlite3

class WaterBillDatabase:
    def __init__(self, db_path="_internal/db/water_bill_database.db"):
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
                email TEXT,
                consumption REAL,
                current_reading REAL,
                previous_reading REAL,
                meter_consumption REAL,
                bill_amount_php REAL,
                messages TEXT
            )
        ''')

        self.cursor.execute("PRAGMA table_info(water_bills)")
        columns = [column[1] for column in self.cursor.fetchall()]
        if 'messages' not in columns:
            self.cursor.execute("ALTER TABLE water_bills ADD COLUMN messages TEXT")

        self.conn.commit()

    def save_to_database(self, customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php, messages):
        self.cursor.execute('''
            INSERT INTO water_bills (
                customer_name,
                address,
                email,
                consumption,
                current_reading,
                previous_reading,
                meter_consumption,
                bill_amount_php,
                messages
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (customer_name, address, email, consumption, current_reading, previous_reading, meter_consumption, bill_amount_php, messages))

        self.conn.commit()

    def fetch_data(self):
        self.cursor.execute('SELECT * FROM water_bills')
        data = self.cursor.fetchall()
        return data

    def delete_and_clear(self, id):
        self.cursor.execute("DELETE FROM water_bills WHERE id = ?", (id,))
        self.conn.commit()
