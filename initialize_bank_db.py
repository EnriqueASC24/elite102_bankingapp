import sqlite3

DB_NAME = 'example.db'


def initialize_bank_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a sample table
    print("Creating table if it does not exist...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bank_accounts
            (RoutingNumber integer primary key, 
            name text, 
            dollar_amount real, 
            account_type text)
    ''')

    print("Table created.")

    # Insert sample data
    print("Inserting sample data...")
    cursor.execute('''
        INSERT INTO bank_accounts (RoutingNumber, name, dollar_amount, account_type) VALUES
        (123456789, 'Alice', 1000.0, 'Checking'),
        (987654321, 'Bob', 2000.0, 'Savings'),
        (456789123, 'Charlie', 1500.0, 'Checking')
    ''')
    print("Sample data inserted.")
    # Commit the changes and close the connection
    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()


initialize_bank_database()
