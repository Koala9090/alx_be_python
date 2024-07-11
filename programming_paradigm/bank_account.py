class BankAccount:
    def __init__(self, account_balance=0):
        self.balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited. New balance: ${self.balance}"
        else:
            return "Enter a positive amount."

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        elif amount <= 0:
            return "Enter a positive amount."
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
       
