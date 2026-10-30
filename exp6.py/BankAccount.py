class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Error: Insufficient funds.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful.")
        else:
            print("Error: Insufficient funds.")


# Taking input from user
name1 = input("Enter first account holder name: ")
name2 = input("Enter second account holder name: ")

# Creating two BankAccount objects
account1 = BankAccount(name1)
account2 = BankAccount(name2)

# Deposit
amount = float(input("Enter deposit amount for first account: "))
account1.deposit(amount)

# Withdrawal
amount = float(input("Enter withdrawal amount from first account: "))
account1.withdraw(amount)

# Transfer
amount = float(input("Enter amount to transfer from first account to second account: "))
account1.transfer(amount, account2)

# Display balances
print("\n--- Account Details ---")
account1.display_balance()

print()
account2.display_balance()