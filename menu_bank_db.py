import sqlite3
import initialize_bank_db
user_name = "Family"
password = "password123"
database_name = "bank_accounts"


id1 = 0
name1 = ""
account_amount1 = 0.0
account_type1 = ""

def security_check():
    safe = 0
    while safe == 0:
        try:
            input_username = input("Enter username: ")
            input_password = input("Enter password: ")
        except:
            print("Invalid Value try again")
        else:
            safe = 1

    if input_username == user_name and input_password == password:
        print("Access granted.")
        return False
    else:
        print("Access denied. Incorrect username or password. Try again.")
        return True
    
def bank_menu():
    print("Welcome to the Texas_branch_bank_app Menu!")
    print("1. View all accounts")
    print("2. Create a new bank account")
    print("3. Deposit money into an account")
    print("4. Withdraw money from an account")
    print("5. Check account balance")
    print("6. Exit")



def selection():
    safe = 0
    while safe == 0:
        try:
            number = int(input('Enter the number of your choice[1-5]:  '))
        except:
            print("Invalid Value try again")
        else:
            safe = 1
    safe = 0
    while safe == 0:
        try:
            if number == 1:
                view_account()
            elif number == 2:
                create_account()
            elif number == 3:
                deposit_into_account()
            elif number == 4:
                withdraw_into_account()
            elif number == 5:
                check_account_balance()
            elif number == 6:
                print(f"Have a great day!")
                return 1
            return 0
        except:
            print("Invalid Value try again")
        else:
            safe = 1
    

def view_account():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Get all rows from the Bank table
    print("Fetching all rows from the bank_accounts table...")
    results = cursor.execute(f'''
        SELECT id, name, account_type FROM {database_name}
    ''')

    print("Results:")
    for row in results:
        print(row)

    connection.close()

def create_account():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    id1 = 1

    results = cursor.execute(f'''
        SELECT * FROM {database_name}
    ''')

    for i in results:
        id1 += 1

    name1 = input("Name of bank account user: ")
    initial_deposit1 = float(input("How much would you like to deposit: "))
    account_type1 = input("What will the type(Savings or Checking): ")

    results = cursor.execute(f'''
       INSERT INTO bank_accounts (id, name, dollar_amount, account_type) VALUES
        ({id1}, '{name1}', {initial_deposit1}, '{account_type1}');
    ''')

    results = cursor.execute(f'''
        SELECT * FROM {database_name}
    ''')

    print("Results:")
    for row in results:
        print(row)

    connection.commit()
    connection.close()

def id_checker(id):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    list_of_ID = cursor.execute(f'''
        SELECT id FROM {database_name}
    ''')

    for ids in list_of_ID:
        if f"({id},)" == str(ids):
            return True    
    connection.close()

def current_amount(id):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    account_amount1 = cursor.execute(f'''
        SELECT dollar_amount FROM {database_name} WHERE id = {id}
    ''')
    for i in account_amount1:
        return i[0]
    connection.close()

def deposit_into_account():
    view_account()
    id1 = int(input("Select the id of the account you want to deposit money: "))
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    if id_checker(id1):
        amount_depositing = float(input("How much would you like to deposit: "))
        cursor.execute(f'''
        UPDATE {database_name}
        SET dollar_amount = {current_amount(id1) + amount_depositing}
        WHERE id = {id1};
        ''')
    else:
        print("Sorry try again")
    connection.commit()
    connection.close()

def withdraw_into_account():
    view_account()
    id1 = int(input("Select the id of the account you want to withdraw money: "))
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    if id_checker(id1):
        amount_depositing = float(input("How much would you like to withdraw: "))
        cursor.execute(f'''
        UPDATE {database_name}
        SET dollar_amount = {current_amount(id1) - amount_depositing}
        WHERE id = {id1};
        ''')
    else:
        print("Sorry try again")
    connection.commit()
    connection.close()

def reset_database():
    initialize_bank_db.initialize_bank_database()

def check_account_balance():
    view_account()
    id1 = int(input("Select the id of the account you want deposit to see new balance: "))
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Get all rows from the Bank table
    print("Fetching information from the bank_accounts table...")
    results = cursor.execute(f'''
        SELECT name, dollar_amount FROM {database_name} WHERE id = {id1}
    ''')

    print("Results:")
    for row in results:
        print(row)

    connection.close()

reset_database()

safe = True
while safe:
    safe = security_check()

loop = 0
while loop == 0:
    bank_menu()
    loop = selection()
