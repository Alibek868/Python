class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

account = Account("John Doe", 1000)


account.deposit(500)   
account.deposit(-100)  


account.withdraw(200)  
account.withdraw(2000) 
account.withdraw(-50)  
print(account)  
