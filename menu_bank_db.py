import sqlite3


def main():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Get all rows from the Bank table
    print("Fetching all rows from the bank_accounts table...")
    results = cursor.execute('''
        SELECT * FROM bank_accounts
    ''')

    print("Results:")
    for row in results:
        print(row)

    # Get all bank accounts with a balance greater than 1000
    print("Fetching bank accounts with balance greater than 1000...")
    results = cursor.execute('''
        SELECT * FROM bank_accounts WHERE dollar_amount > 1000
    ''')
    print("Results:")
    for row in results:
        print(row)

    connection.close()


if __name__ == "__main__":
    main()
