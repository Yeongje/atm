
class Accounts():

    def __init__(self, pinNumber):
        self.pinNumber = pinNumber
        self.accountId = pinNumber

        self.balance = 0


    def withdraw(self, credit):
        if self.balance < credit:
            pass
        else:
            self.balance -= credit


    def deposit(self, credit):
        self.balance += credit


