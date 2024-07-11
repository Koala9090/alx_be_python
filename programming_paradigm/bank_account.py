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
            return f"Withdrew: ${amount}"
        elif amount <= 0:
            return "enter a positive amount"
        elif amount > self.balance:
            return f"Insufficient funds."
        pass
    def display_balance(self):
        return f"Current Balance: ${self.balance}"
       
