class BankAccount:
    def __init__(self, name, account_no):
        self.name = name
        self.account_no = account_no

    def display(self):
        print("\nAccount Holder:", self.name)
        print("Account Number:", self.account_no)


name1 = input("Enter first account holder name: ")
acc1 = input("Enter first account number: ")

name2 = input("Enter second account holder name: ")
acc2 = input("Enter second account number: ")

account1 = BankAccount(name1, acc1)
account2 = BankAccount(name2, acc2)

print("\n--- Account Details ---")
account1.display()
account2.display()