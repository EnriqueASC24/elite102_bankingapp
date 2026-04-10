import sqlite3
user_name = "Family_accounts_love"
password = "password123"
database_name = "bank_accounts"

id = 0
name = ""
account_amount = 0.0
account_type = ""

def security_check():
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")

    if input_username == user_name and input_password == password:
        print("Access granted.")
        return False
    else:
        print("Access denied. Incorrect username or password. Try again.")
        return True
    
def bank_menu():
    print("Welcome to the Bank Menu!")
    print("1. View all accounts")
    print("2. Create a new bank account")
    print("3. Deposit money into an account")
    print("4. Withdraw money from an account")
    print("5. Check account balance")
    print("6. Exit")



def main():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Get all rows from the Bank table
    print("Fetching all rows from the bank_accounts table...")
    results = cursor.execute(f'''
        SELECT * FROM {database_name}
    ''')

    print("Results:")
    for row in results:
        print(row)

    # Get all bank accounts with a balance greater than 1000
    print("Fetching bank accounts with balance greater than 1000...")
    results = cursor.execute(f'''
        SELECT * FROM {database_name} WHERE dollar_amount > 1000
    ''')
    print("Results:")
    for row in results:
        print(row)

    connection.close()

safe = True
while safe:
    safe = security_check()
main()
