class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return
    
    def withdraw(self, amount):
        self.balance -= amount
        print(self.balance)
        return
    
    def monies(self):
        print(self.balance)
        return
    

JamesBank = Bank(500)
JamesBank.monies()
JamesBank.deposit(500)
JamesBank.withdraw(200)

