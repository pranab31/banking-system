from time import time

accounts = {}

def create_account(first_name, last_name, initial_balance):
    account_number = str(time()).replace('.', '')
    accounts[account_number] = {
        'first_name': first_name,
        'last_name': last_name,
        'balance': initial_balance
    }
    return account_number

def deposit(account_number, amount):
    try:
        account_info = accounts[account_number]
        account_info['balance'] += amount
    except KeyError:
        return False
    return account_info['balance']

def withdrawal(account_number, amount):
    try:
        account_info = accounts[account_number]
        account_info['balance'] -= amount
    except KeyError:
        return False
    return account_info['balance']

def get_balance(account_number):
    try:
        return accounts[account_number]['balance']
    except KeyError:
        return False

while True:
    print('1> New account')
    print('2> Deposit')
    print('3> withdrawal')
    print('4> See balance')
    print('5> Show all acounts')
    print('q> Exit')
    print("Please enter your choice: ",end=' ')
    user_input = input()
    if user_input == "1":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        initial_balance = float(input("Enter initial balance: "))
        account_number = create_account(first_name, last_name, initial_balance)
        print("Your account number is : {}".format(account_number))
    elif user_input == "2":
        account_number  = input("User account number: ")
        amount = float(input("Enter deposit amount: "))
        current_balance = deposit(account_number, amount)
        if current_balance is not False:
            print("Now your current balance is: {}".format(current_balance))
        else:
            print("Account not found. Please enter correct account number.")
    elif user_input == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdrawal: "))
        current_balance = withdrawal(account_number, amount)
        if current_balance is not False:
            print("Your current balance is: {}".format(current_balance))
        else:
            print("Account not found. Please enter correct account number.")
    elif user_input == "4":
        account_number = input('Enter account number: ')
        current_balance = get_balance(account_number)
        if current_balance is not False:
            print("Your current balance is : {}".format(current_balance))
        else:
            print('Account not found. Please enter correct account number.')
    elif user_input == "5":
        for account_number, account_info in accounts.items():
            print("account number: {}, account holder name: {} {}, balance: {}".format(account_number, account_info['first_name'], account_info['last_name'], account_info['balance']))
    elif user_input == "q":
        print("Thank you..")
        break
    else:
        print("Please enter correct option.")
