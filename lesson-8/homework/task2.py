import json
import os


class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} successfully!")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                print(f"Unsuccessfull.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than zero.")

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

    @staticmethod
    def from_dict(data):
        return Account(data["account_number"], data["name"], data["balance"])


class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def generate_account_number(self):
        return str(100000 + len(self.accounts))

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return

        account_number = self.generate_account_number()
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        print(f"Account created successfully! Your account number is {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print("\nAccount Details:")
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: {account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def save_to_file(self):
        try:
            with open(self.filename, "w") as file:
                json.dump({}, file, indent=4)
        except IOError:
            print("Error saving account data.")

    def load_from_file(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    self.accounts = {}
            except (IOError, json.JSONDecodeError):
                print("Error loading account data. Starting fresh.")


def main():
    bank = Bank()

    while True:
        print("\nBanking Application")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            while True:
                try:
                    initial_deposit = float(input("Enter initial deposit amount: "))
                    break
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            bank.create_account(name, initial_deposit)

        elif choice == "2":
            account_number = input("Enter account number: ")
            bank.view_account(account_number)

        elif choice == "3":
            account_number = input("Enter account number: ")
            while True:
                try:
                    amount = float(input("Enter deposit amount: "))
                    break
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            bank.deposit(account_number, amount)

        elif choice == "4":
            account_number = input("Enter account number: ")
            while True:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    break
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            bank.withdraw(account_number, amount)

        elif choice == "5":
            print("Thank you for using the bank application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()