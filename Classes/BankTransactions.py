class BankAccount():
    def __init__(self, new_name, checking_balance, savings_balance):
        self.name = new_name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
    
    def deposit_checking(self, amount):
        if amount > 0:
            self.checking_balance += amount
    
    def deposit_savings(self, amount):
        if amount > 0:
            self.savings_balance += amount
        
    def withdraw_checking(self, amount):
        if amount > 0:
            self.checking_balance -= amount
        
    def withdraw_savings(self, amount):
        if amount > 0:
            self.savings_balance -= amount
        
    def transfer_to_savings(self, amount):
        if amount > 0:
            self.checking_balance -= amount
            self.savings_balance += amount
    
if __name__ == "__main__":
    account = BankAccount("Mickey", 100.00, 100.00)
    account.checking_balance = 100
    account.savings_balance = 100
    account.withdraw_savings(-5)
    account.withdraw_checking(-5)
    account.transfer_to_savings(-5)

    print(account.name)
    print(f'${account.checking_balance:.2f}')
    print(f'${account.savings_balance:.2f}')