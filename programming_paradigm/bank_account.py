class BankAccount:
    def __init__(self,account_balance=0):
        self.balance = account_balance
        
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            return f"Deposited: ${amount}"
        else:
            return "Enter a positive amount"
    def withdraw (self,amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        elif amount <= 0:
            return "Enter a positive amount"
        else:
            return False
        pass
    def display_balance(self):
        return f"Current balance: ${self.balance}"
       
