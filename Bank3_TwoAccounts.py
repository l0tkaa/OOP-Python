'''Non-OOP
Bank 3
Two Accounts
with User Defined Functions and Global Variables
Operations (verbs): Create(An Account), Deposit, Withdraw, Check Balance
Data (nouns): Customer Name, Password, Balance
'''
# set global variables
account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password =''
nAccounts = 0

def newAccount(accountNumber, name, balance, password):
        #get global variables
        global account0Name, account0Balance, account0Password
        global account1Name, account1Balance, account1Password

        if accountNumber ==0:
                account0Name = name
                account0Balance = balance
                account0Password = password
        if accountNumber ==1:
                account1Name = name
                account1Balance = balance
                account1Password = password

def show():
        global account0Name, account0Balance, account0Password
        global account1Name, account1Balance, account1Password

if account0Name != '':
        print('Account 0')
        print('         Name', account0Name)
        print('         Balance', account0Balance)
        print('         Password', account0Password)
        print()
if account1Name != '':
        print('Account 1')
        print('         Name', account1Name)
        print('         Balance', account1Balance)
        print('         Password', account1Password)
        print()

def getBalance(accountNumber, password):
        global account0Name, account0Balance, account0Password
        global account1Name, account1Balance, account1Password

        if accountNumber ==0:
                if password!= account0Password:
                        print('Incorrect password')
                        return None
                return account0Balance
        
        if accountNumber ==1:
                if password != account1Password:
                        print('Incorrect password')
                        return None
                return account1Balance
print('Done')