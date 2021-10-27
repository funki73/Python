class BankAccount: 
    accounts = []
    def __init__(self, int_rate, account_balance):
        self.int_rate = int_rate
        self.account_balance = account_balance
        BankAccount.accounts.append(self) # Did not have in original code.

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

        #       In my orginal code  - incorrect.
        # if self.account_balance < amount: 
        #     print(f"Insufficient funds:  Charging a $5 fee")
        #     self.account_balance -= 5 + amount
        # else:
        #     self.account_balance -= amount
        # return self

    def display_account_info(self):
        print(f"Account Balance: {self.account_balance}")
        return self

    def yield_interest(self):
        if (self.account_balance > 0):
            self.account_balance += (self.account_balance * self.int_rate)
        return self
        # if self.int_rate <= 0:  My original Code
        #     print(f"No interest earned.")  My original Code
        # else:  My original Code
        #     self.account_balance += self.account_balance * self.int_rate:  My original Code
        # return self:  My original Code

    @classmethod #did not have in orginal code
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

        Checking = BankAccount(.06,3000)
        Savings = BankAccount (.05,4000)

        Checking.deposit(2300).deposit(650).deposit(450).withdraw(1000).yield_interest().display_account_info()
        Savings.deposit(15).deposit(150).withdraw(5).withdraw(10).withdraw(50).withdraw(5).yield_interest().display_account_info()

        BankAccount.print_all_accounts()


# The class should also have the following methods:
# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

# don't forget to add some default values for these parameters!