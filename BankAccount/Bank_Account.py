class BankAccount: 
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate	
        
    
    def deposit(self, amount):
        deposit = self.balance + amount
        self.balance = deposit
        return self.balance

    def withdraw(self, amount):
        if amount < self.balance:
            remaining = self.balance - amount
            self.balance = remaining
            return self.balance
        else:
            print("Insufficient funds: Charging a $5 fee and deduct $5")
            
    def display_account_info(self):
        return self.balance
    
    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        return self.balance
    
    
class BankAccount2: 
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate	
        
    
    def deposit(self, amount):
        deposit = self.balance + amount
        self.balance = deposit
        return self.balance

    def withdraw(self, amount):
        if amount < self.balance:
            remaining = self.balance - amount
            self.balance = remaining
            return self.balance
        else:
            return("Insufficient funds: Charging a $5 fee and deduct $5")
            
    def display_account_info(self):
        return self.balance
    
    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        return self.balance


my_account1 = BankAccount(0.05, 200)
print("Account 1 Balance:", my_account1.deposit(200))
print("Account 1 Balance:",my_account1.deposit(100))
print("Account 1 Balance:",my_account1.deposit(100))
print("Account 1 Balance:",my_account1.withdraw(100))
print("Account 1 Balance:",my_account1.display_account_info())
print("Account 1 Balance:",my_account1.yield_interest())
    
my_account2 = BankAccount2(0.05, 200)
print("Account 2 Balance:", my_account2.deposit(200))
print("Account 2 Balance:",my_account2.deposit(50))
print("Account 2 Balance:",my_account2.withdraw(470))
print("Account 2 Balance:",my_account2.withdraw(40))
print("Account 2 Balance:",my_account2.withdraw(20))
print("Account 2 Balance:",my_account2.withdraw(10))
print("Account 2 Balance:",my_account2.display_account_info())
print("Account 2 Balance:",my_account2.yield_interest())