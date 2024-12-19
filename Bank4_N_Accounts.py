'''
Non-OOP Bank
Version 4
Any number of accounts
Using lists, user defined functions, and global variables

Operations (verbs): Create(An Account), Deposit, Withdraw, Check Balance
Data (nouns): Customer Name, Password, Balance
'''
#set global variables (the lists are set to empty)
accountNamesList = []
accountBalancesList = []
accountPasswordsList = []

def newAccount(name, balance, password):
        #get global variables
        global accountNamesList, accountBalancesList, accountPasswordsList
        accountNamesList.append(name)
        accountBalancesList.append(balance)
        accountPasswordsList.append(password)

def show(accountNumber):
        global accountNamesList, accountBalancesList, accountPasswordsList
        print('Account', accountNumber)
        print('         Name', accountNamesList[accountNumber])
        print('         Balance: ', accountBalancesList[accountNumber])
        print('         Password:', accountPasswordsList[accountNumber])
        print()

def getBalance(accountNumber, password):
        global accountNamesList, accountBalancesList, accountPasswordsList
        if password != accountPasswordsList[accountNumber]:
                print('Incorrect password')
                return None
        return accountBalancesList[accountNumber]

print("Joe's account is account number:" len(accountNamesList)) #returns the len of the list as the users account number

newAccount("Mary", 12345, 'nuts')

while True:
        print()
        print('Press b to get the balance')
        print('Press d to make a deposit')
        print('Press n to create a new account')
        print('Press w to make a withdrawal')
        print('Press s to show all accounts')
        print('Press q to quit')
        print()

        action = input('What do you want to do?')
        action = action.lower()
        action = action[0]
        print()

        if action == 'b':
                print('Get Balance:')
                userAccountNumber = input('Please enter your account number')
                userAccountNumber = int(userAccountNumber)
                userPassword = input('Please enter the password: ')
                theBalance = getBalance(userAccountNumber, userPassword)
                if theBalance is not None:
                        print('Your balance is: ', theBalance)
print('Done')