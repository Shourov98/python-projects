class BankAccount:
    def __init__(self, holder_name, initial_balance):
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            self.balance += amount
            print(f"Deposit successful! New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance. Transaction failed.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current balance: ${self.balance:.2f}")


# Default user details
DEFAULT_USER_NAME = "John Doe"
DEFAULT_INITIAL_BALANCE = 1000.00

# Create a bank account instance with default values
account = BankAccount(DEFAULT_USER_NAME, DEFAULT_INITIAL_BALANCE)

# Menu-driven interface
def banking_menu():
    print("\nWelcome to the Banking Management System")
    print(f"Account Holder: {account.holder_name}")
    print(f"Initial Balance: ${account.balance:.2f}")
    
    while True:
        print("\nChoose an operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Inquiry")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                amount = float(input("Enter amount to deposit: $"))
                account.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter amount to withdraw: $"))
                account.withdraw(amount)
            elif choice == 3:
                account.get_balance()
            elif choice == 4:
                print("Thank you for using the Banking Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    banking_menu()
