
class BankAccount:
    def __init__(self):
        self._balance = 0# Protected - children can access
        self.__account_id = "ACC123"# Private - only this class

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Amount must be positive")

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
# Can access _balance from parent
        interest = self._balance * rate
        self._balance += interest

# Usage
account = BankAccount()
account.deposit(1000)
# account.add_interest(0.05)
# print(account.__account_id)
print(account._balance)# 1050.0

print(account.get_balance())# 1050.0