import datetime as Date

class User():
    __user_list = {}
    class_name = {}
    cnt = 100000
    def __init__(self, name, email, address, account_type):
        self.__balance = 0
        self.name = name 
        self.email = email 
        self.address = address 
        self.account_type = account_type
        self.account_number = User.cnt + 1
        User.cnt+=1
        self.user_transation_history = {}
        self._user_info = {
            "Name" : self.name,
            "Email": self.email,
            "address": self.address,
            "Account type": self.account_type,
            "account_number": self.account_number,
            "loan_count": 0,
            "loan_amount": 0,
            "balance": self.__balance,
            "transaction_history": self.user_transation_history
        } 
        
        User.__user_list[self.account_number] = self._user_info
        
    # def __repr__(self) -> str:
    #     return f" Name: {self._user_info['Name']}\n Email: {self._user_info['Email']}\n Address: {self._user_info['address']}\n Account Number: {self._user_info['account_number']}\n Account type: {self._user_info['Account type']}\n Loan Count: {self._user_info['loan_count']}\n Loan Amount: {self._user_info['loan_amount']}\n Balance: {self._user_info['balance']}\n"

#Amin Section
class Admin():
    admin_ID = 100
    loan_feature = True
    total_loan = 0
    total_bank_balance = 1000000
    
    def __init__(self):
        self.passward = "Bank1234"
            
    
    def list_user_accounts(self):
        for ac_number, user_info in User._User__user_list.items():
            print(f" Account Number: {ac_number}\n Name: {user_info['Name']}\n Email: {user_info['Email']}\n Address: {user_info['address']}\n ")
            
    def delete_user_account(self, user_account_number):
        if user_account_number in User._User__user_list:
            del User._User__user_list[user_account_number]
            print(f"User account {user_account_number} deleted successfully.")
        else:
            print(f"User account {user_account_number} does not exist.")
            
    def check_total_available_balance(self):
        return f"Total available balance in the bank: {Admin.total_bank_balance}.\n"

    def check_total_loan_amount(self):
        return f"Total total in the bank: {Admin.total_loan}.\n"

    def toggle_loan_feature(self):
        enable = int(input(" 1. Enable\n 2. Disable\n "))
        if enable==1:
            Admin.loan_feature = True
            print("Loan feature is now enabled.\n")
            
        elif(enable==2):
            Admin.loan_feature = False
            print("Loan feature is now disabled.\n")
            
           
            
        print(Admin.loan_feature)
        
admin = Admin()
#User Work
def deposit(account_number, amount):
    try:
        if amount > 0:
            if account_number in User._User__user_list:
                user = User._User__user_list[account_number]
                user["balance"] += amount
                Admin.total_bank_balance += amount
                user["transaction_history"][Date.datetime.now()] = {"deposit": amount}
                print(f"{amount} taka Deposit Successfully")
                print(f"Deposited {amount}. Current balance: {user['balance']}")
            else:
                print("User not found")
        else:
            print("Invalid deposit amount")
    except ValueError as e:
        print(f"Error: {e}")
          
def withdraw(account_number, amount):
    try:
        if amount < Admin.total_bank_balance:
            if account_number in User._User__user_list:
                user = User._User__user_list[account_number]
                if amount <= user["balance"]:    
                    user["balance"] -= amount
                    Admin.total_bank_balance -= amount
                    user["transaction_history"][Date.datetime.now()] = {"withdraw": amount}
                    print(f"Withdrew {amount}. Current balance: {user['balance']}")
                else:
                    raise ValueError("Withdrawal amount exceeded. Your current balance is insufficient.\n")
        else:
            raise ValueError("bank is bankrupt")
    except ValueError as e:
        print(f"Error: {e}")
def check_balance(account_number):
    if account_number in User._User__user_list:
        user = User._User__user_list[account_number]
        b=user['balance']
        return f"Your current balance is {b}\n"
    else:
        return "User not found"

    
def check_transaction_history(account_number):
    try:
        if account_number in User._User__user_list:
            user = User._User__user_list[account_number]
            history = user["transaction_history"]
            print("Transaction History:")
            for time, transactions in history.items():
                for transaction_type, transaction_amount in transactions.items():
                    print(f" Time: {time}\n Type: {transaction_type}\n Amount: {transaction_amount}\n")
        else:
            print("User not found")
    except ValueError as e:
        print(f"Error: {e}")


def transfer_balance(sender_account_number, recipient_account_number):
    try:
        if sender_account_number in User._User__user_list:
            send_amount = int(input("Write the amount you want to transfer: "))
            if recipient_account_number  in User._User__user_list:
                sender = User._User__user_list[sender_account_number]
                recipient = User._User__user_list[recipient_account_number]
                if send_amount < sender["balance"]:
                    sender["balance"] -= send_amount
                    recipient["balance"] += send_amount
                    sender['transaction_history'][Date.datetime.now()] = {"Transfer": send_amount}
                    recipient['transaction_history'][Date.datetime.now()] = {"Recived": send_amount}
                    print(f"Transferred {send_amount} to {recipient['Name']}. Your current balance: {sender['balance' ]}")
                else:
                    raise ValueError("Transfer amount exceeded. Your current balance is insufficient.\n")
            else:
                raise ValueError(f"{recipient_account_number} Account does not exist.Please check the account number.\n")
        else:
                raise ValueError(f"{sender_account_number} Account does not exist.Please check the account number.\n")
    except ValueError as e:
        print(f"Error: {e}")
                  
def take_loan(account_number):
    try:
        amount = int(input("Write the amount you want to take:  "))
        if Admin.loan_feature:
            if account_number in User._User__user_list:
                user = User._User__user_list[account_number]
                count = user['loan_count']
                if count < 2:
                    user["loan_count"] += 1 
                    user['balance'] += amount
                    user['loan_amount'] += amount
                    Admin.total_loan += amount
                    user['transaction_history'][Date.datetime.now()] = {"Loan": amount}
                    print(f"Loan of {amount} successfully granted.\n")
                    print(f"Loan taken: {amount}. Current balance: {user['balance']}")
                else:
                    raise ValueError("You can't take a loan. You've exceeded the maximum number of allowed loans.\n")
            else:
                raise ValueError("The account is incurrect. Please check the account number aggain\n")
        else:
            raise ValueError("Loan feature is currently disabled.\n")
    except ValueError as e:
        print(f"Error: {e}")

def user_account_details(account_number):
    if account_number in User._User__user_list:
        user  = User._User__user_list[account_number]
        return f" Name: {user['Name']}\n Email: {user['Email']}\n Address: {user['address']}\n Account Number: {user['account_number']}\n Account type: {user['Account type']}\n Loan Count: {user['loan_count']}\n Loan Amount: {user['loan_amount']}\n Balance: {user['balance']}\n"      




        
            
# Testing the code
A = User("Murad", "mosaddek.habib.7@gmail.com", "Pirganj, Rangpur", "Savings")
B = User("Moosa", "U1709001@student.cuet.ac.bd", "Chittagong", "Savings")
C = User("Mosaddek", "mh.murad.2020@gmail.com", "Dhaka", "Current")
D = User("Abdullah", "U1709001@student.cuet.ac.bd", "Chittagong", "Savings")
E = User("Mosa", "mosa@example.com", "Chattagram", "Current")
F = User("Alice", "alice@example.com", "New York", "Current")
G = User("Bob", "bob@example.com", "Los Angeles", "Current")
admin = Admin()

while True:
    print("\nBanking Management System")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Create Account for New User")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        account_number = int(input("Enter your account number: "))
        if account_number in User._User__user_list:
            while True:
                print("\nUser Menu")
                print("1. Create Account") #ok
                print("2. Deposit") #ok
                print("3. Withdraw") #ok 
                print("4. Check Balance") #ok
                print("5. Transaction History") #ok
                print("6. Take Loan") #ok
                print("7. Transfer Money")#ok
                print("8. Show Details Of account Owner") #ok
                print("9. Logout") #ok
                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    name = input("Enter your name: ")
                    email = input("Enter your email: ")
                    address = input("Enter your address: ")
                    account_type = input("Enter account type (Savings/Current): ")
                    user = User(name, email, address, account_type)
                    print(f"Account created. Your account number is {user.account_number}")

                elif user_choice == "2":
                    if account_number in User._User__user_list:
                        user=account_number
                        amount = float(input("Enter the deposit amount: "))
                        deposit(account_number, amount)
                    else:
                        print("User not found")

                elif user_choice == "3":
                    if account_number in User._User__user_list:
                        user=account_number
                        amount = float(input("Enter the withdrawal amount: "))
                        withdraw(account_number, amount)
                    else:
                        print("User not found")

                elif user_choice == "4":
                    print(check_balance(account_number))

                elif user_choice == "5":
                    check_transaction_history(account_number)
                    
                elif user_choice == "6":
                    
                    take_loan(account_number)

                elif user_choice == "7":
                    sender_account_number = account_number
                    recipient_account_number = int(input("Enter recipient's account number: "))
                    
                    transfer_balance(sender_account_number, recipient_account_number)
                
                elif user_choice == "8":
                    print(user_account_details(account_number))
                    
                elif user_choice == "9":
                    break
        else:
            raise ValueError("Invalid Account Number. Please write currectly")

    elif choice == "2":
        admin_password = input("Enter admin password: password is Bank1234")
        if admin_password == admin.passward:  # Replace with your admin password
            while True:
                print("\nAdmin Menu")
                print("1. Create User Account")
                print("2. Delete User Account")
                print("3. List User Accounts")
                print("4. Total Available Balance")
                print("5. Total Loan Amount")
                print("6. Toggle Loan Feature")
                print("7. Logout")
                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    name = input("Enter user's name: ")
                    email = input("Enter user's email: ")
                    address = input("Enter user's address: ")
                    account_type = input("Enter user's account type (Savings/Current): ")
                    user = User(name, email, address, account_type)
                    print(f"Account created. Your account number is {user.account_number}")
                    

                elif admin_choice == "2":
                    account_number = int(input("Enter the user's account number to delete: "))
                    print(admin.delete_user_account(account_number))

                elif admin_choice == "3":
                    print(admin.list_user_accounts())

                elif admin_choice == "4":
                    print(admin.check_total_available_balance())

                elif admin_choice == "5":
                    print(admin.check_total_loan_amount())

                elif admin_choice == "6":
                    admin.toggle_loan_feature()

                elif admin_choice == "7":
                    break
        else:
            print('Wrong Password')
    elif choice == "3":
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                address = input("Enter your address: ")
                account_type = input("Enter account type (Savings/Current): ")
                user = User(name, email, address, account_type)
                print(f"Account created. Your account number is {user.account_number}")
                
    elif choice == "4":
        break