class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance +- amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

        # print(self.name)- My original Code - incorrect
        # print(self.email)- My original Code - incorrect
        # print(self.account_balance)- My original Code - incorrect

    def transfer_money(self, amount, user):  #did not have this code in original answer
        self.account_balance -= amount  #did not have this code in original answer
        user.account_balance += amount  #did not have this code in original answer
        self.display_user_balance()  #did not have this code in original answer
        user.display_user_balance()  #did not have this code in original answer
        return self

Guido = User("Guido")
Nancy = User("Nancy")
Joe = User("Joe")

Guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawl(45).display_user_balance()
Nancy.make_deposit(1000).make_deposit(1000).make_withdrawl(500).make_withdrawl(300).display_user_balance()
Joe.make_deposit(1500).make_withdrawl(1000).make_withdrawl(5000).make_withdrawl(3000).display_user_balance()

# Guido.make_deposit(100)
# Guido.make_deposit(200)
# Guido.make_deposit(50)
# Guido.make_withdrawl(45)
# Guido.display_user_balance()

# Nancy.make_deposit(1000)
# Nancy.make_deposit(1000)
# Nancy.make_withdrawl(500)
# Nancy.make_withdrawl(300)
# Nancy.display_user_balance()

# Joe.make_deposit(1500)
# Joe.make_withdrawl(1000)
# Joe.make_withdrawl(5000)
# Joe.make_withdrawl(3000)
# Joe.display_user_balance()

# Nancy.transfer_money(400, Guido)

# guido = User("Guido", "Guido@mail.com") - My original Code - incorrect
# guido.account_balance = "$150" - My original Code - incorrect
# print(guido.name) - My original Code - incorrect
# print(guido.email) - My original Code - incorrect
# print(guido.account_balance)- My original Code - incorrect

# nancy = User("Nancy", "nancy@mail.com")- My original Code - incorrect
# nancy.make_withdrawl = "$200"- My original Code - incorrect
# print(nancy.make_withdrawl)- My original Code - incorrect
# print(nancy.account_balance)- My original Code - incorrect


# *****************************************************

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified

# display_user_balance(self) - have this method print the user's name and account balance to the terminal*
# eg. "User: Guido van Rossum, Balance: $150*

# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

