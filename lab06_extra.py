## Extra Object-Oriented Programming questions ##

from lab06 import *
class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> eric_account = Account('Eric')
    >>> eric_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # buying dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

# Q6
class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> check = Check("Steven", 42)  # 42 dollars, payable to Steven
    >>> steven_account = CheckingAccount("Steven")
    >>> eric_account = CheckingAccount("Eric")
    >>> eric_account.deposit_check(check)  # trying to steal steven’s money
    The police have been notified.
    >>> eric_account.balance
    0
    >>> check.deposited
    False
    >>> steven_account.balance
    0
    >>> steven_account.deposit_check(check)
    42
    >>> check.deposited
    True
    >>> steven_account.deposit_check(check)  # can't cash check twice
    The police have been notified.
    """
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
    def deposit_check(self,check):
        if check.payable_to != self.holder:
            print("The police have been notified")
            check.deposited = False
        if check.depositcount > 1:
            print("The police have been notified")
            check.deposited = False
        else:
            check.deposited = True
            check.depositcount += 1
            self.balance += check.amount



class Check(object):
    def __init__(self, account_holder, amount):
        self.holder = account_holder
        self.payable_to = account_holder
        self.amount = amount
        self.deposited = True
        self.depositcount = 0


check = Check("Steven", 42)  # 42 dollars, payable to Steven
steven_account = CheckingAccount("Steven")
eric_account = CheckingAccount("Eric")
#print(eric_account.deposit_check(check) ) # trying to steal steven’s money
#the police has been notified
#print(eric_account.balance)
#0
#print( check.deposited)
#False
#print(steven_account.balance)
#0
#print(steven_account.deposit_check(check))
#42
#print(check.deposited)
#True
#print(steven_account.deposit_check(check))
#the police has been notified



# Q7
class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.pressed
    2
    >>> b2.pressed
    3
    """

    def __init__(self, *args):
        self.dicti = {"Button.pos":Button.key}
        self.poslist = []
        self.outputlist =[]


    def press(self, info):
        """Takes in a position of the button pressed, and 
        returns that button's output"""
        return ['Button.pos']


    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and 
        returns the total output"""
        self.poslist.append(Button.pos)
        for a_post in self.poslist:
            self.outputlist.append(['Button.pos'])
        Button.pressed += 1
        return self.outputlist

class Button():
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.pressed = 0
