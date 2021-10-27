class BankAccount: 
    accounts = []
    def __init__(self, int_rate, account_balance):
        self.int_rate = int_rate
        self.account_balance = account_balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.account_balance +- amount
        return self

    def withdraw(self, amount):
        if (self.account_balance - amount) >= 0:
            self.account_balance -= amount
        else:
            print(f"Insufficient funds:  Charging a $5 fee")
            self.account_balance -= 5
        return self

    def display_account_info(self):
        return f"{self.account_balance}"

    def yield_interest(self):
        if (self.account_balance > 0):
            self.account_balance += (self.account_balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

# *************************************

class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            'checking': BankAccount (.01, 2000),
            "savings" : BankAccount (.07, 3000)
        }

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self


    def transfer_money(self, amount, user):
        self.account -= amount
        user.account += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

Guido = User("Guido")

Guido.account['checking'].deposit(100)
Guido.display_user_balance()

# Guido = User("Guido")
# Guido.account(100)

# Nancy = User("Nancy")
# Joe = User("Joe")

# Guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawl(45).display_user_balance()
# Nancy.make_deposit(1000).make_deposit(1000).make_withdrawl(500).make_withdrawl(300).display_user_balance()
# Joe.make_deposit(1500).make_withdrawl(1000).make_withdrawl(5000).make_withdrawl(3000).display_user_balance()