class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an optional initial balance.
        :param initial_balance: The starting balance for the account. Defaults to 0.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        :param amount: The amount to deposit.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if funds are sufficient.
        :param amount: The amount to withdraw.
        :return: True if withdrawal is successful, False otherwise.
        """
        if amount > self.__account_balance:
            return False
        elif amount > 0:
            self.__account_balance -= amount
            return True
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")
            return False

    def display_balance(self):
        """
        Display the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

# main-0.py

import sys
from bank_account import BankAccount

def main():
    """
    Main function to interact with the BankAccount class via command line arguments.
    """
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
