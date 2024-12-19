'''
Non-OOP
Bank 2
Single Account
with Functions
'''

accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
        global accountName, accountBalance, accountPassword
        accountName = name
        accountBalance = balance
        accountPassword = password

def show():
        global accountName, accountBalance, accountPassword
        print('         Name:', accountName)
        print('         Balance:', accountBalance)
        print('         Password:', accountPassword)
        print()

def getBalance(password):
        global accountName, accountBalance, accountPassword
        if password != accountPassword:
                print('Incorrect password')
                return None
        return accountBalance

def deposit(amountToDeposit, password):
        global accountName, accountBalance, accountPassword
        if amountToDeposit <0:
                print('You cannot depeosit a negative amount!')
                return None
        
        if password != accountPassword:
                print('Incorrect password')
                return None
        
        accountBalance = accountBalance + amountToDeposit
        return accountBalance

def withdraw(amountToWithdraw, password):
        global accountName, accountBalance, accountPassword
        if amountToWithdraw <0:
                print('You cannot withdraw a negative amount!')
                return None
        
        if password != accountPassword:
                print('Incorrect password for this account')
                return None
        
        if amountToWithdraw > accountBalance:
                print('You cannot withdraw more than you have in your account')
                return None
        
        accountBalance = accountBalance - amountToWithdraw
        return accountBalance
