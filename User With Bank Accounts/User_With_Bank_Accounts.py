class BankAccount: 
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate	
        all_accounts = []
        
    
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
            print("Insufficient funds")
            
    def display_account_info(self):
        return self.balance
    
    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        return self.balance


class User:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def bank_deposit(self, amount):
        self.account.deposit(amount)
        return self.account.balance

    def bank_withdraw(self, amount):
        self.account.withdraw(amount)
        return self.account.balance

    def bank_display_account_info(self):
        self.account.display_account_info()
        return self.account.balance

jimmy = User("Jimmy", "Smith")
print("Checking Balance:", jimmy.bank_deposit(2000))
print("Checking Balance After Withdraw:", jimmy.bank_withdraw(200))
print("Current Balance:", jimmy.bank_display_account_info())
jimmy = User("Jimmy", "Smith")
print("Saving Balance:", jimmy.bank_deposit(100))
print("Saving Balance After Withdraw:", jimmy.bank_withdraw(50))
print("Current Balance:", jimmy.bank_display_account_info())