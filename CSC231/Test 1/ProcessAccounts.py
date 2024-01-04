# Program:    Test 1 Coding Portion
# Author:     Black, Tyler
# Course:     CSC 231
# Term:       Spring 2023



import BankAccount
import sys
import traceback

def createAccountList(fileName):
    """ This method opens a file of account information, reads the information
    and stores it into a list of BankAccount objects.
    Method ignores the first line of header information.
    (**)Does not add duplicate accounts to the accountList and prints a warning message.
    :param fileName: string
    :return: List of BankAccount objects
    """
    accountList=[]
    counter = 0
    Same=False
    with open(fileName,'r') as file:
        for line in file:
            if counter !=0:
                line=line.strip()
                line=line.split(',')
                acct = BankAccount.BankAccount(int(line[0]), line[1], line[2], float(line[3]))
            for index in accountList:

                if acct == index:
                    print('WARNING! Duplicate accounts, Account Number already exists:', index.acctNum)
                    Same=True
                if Same == False:
                    accountList.append(acct)
            counter = counter + 1
            Same=False
    print(accountList)
    return accountList      # placeholder - remove this when you write the function


def calculateAverage(accountList):
    """ This method calculates the average of
    a list of account balances and returns the result.
    :param accountList: List of BankAccount Objects
    :return: float
    """
    sum1 = 0
    for index in accountList:
        sum1= float(index.acctBal) + sum1
    return sum1/len(accountList) # placeholder - remove this when you write the function


def findBiggestBalance(accountList):
    """This method looks through a list of BankAccount objects
    and searches for the account with the biggest balance. It returns
    the information for the BankAccount object.
    :param accountList: List of BankAccount objects
    :return: BankAccount object
    """
    # max1=0
    # for index in accountList:
    #     if float(index.acctBal) >= float(max1):
    #         max2 = index
    #         max1 = index.acctBal
    # return max2    # placeholder - remove this when you write the function
    accountList.sort()
    return accountList[len(accountList)-1]


def findMedianBalance(accountList):
    """ This method finds the BankAccount object with the median
    balance and returns the BankAccount object.
    :param accountList: List of BankAccount objects
    :return: BankAccount
    """
    accountList.sort()
    return accountList[len(accountList)//2]




def updateAccountInterest(accountList):
    """ This method updates the account balances on a list of
    BankAccount objects.
    :param accountList: List of BankAccount objects
    :return: none
    """
    for index in accountList:
        index.acctBal = index.acctBal + index.calculate_interest()


def main():

    try:
        fileName = 'accounts.csv'
        accountList = createAccountList(fileName)
    except:
        print("createAccountlist has errors")
        traceback.print_exc()

    try:
        average = calculateAverage(accountList)
        print(f'Average balance: ${average:,.2f}')
    except:
        print("calculateAverage has errors")
        traceback.print_exc()

    try:
        biggestAccount = findBiggestBalance(accountList)
        print("Biggest balance: ", biggestAccount)
    except:
        print('biggestAccount has errors')
        traceback.print_exc()

    try:
        accountList.sort() # This will use your __lt__ operator, easier to find median if you sort
    except:
        print('sort has errors.')
        traceback.print_exc()

    try:
        medianBalanceAccount = findMedianBalance(accountList)
        print("Median balance: ", medianBalanceAccount)
    except:
        print("findMedianBalance has errors")
        traceback.print_exc()

    try:
        updateAccountInterest(accountList)
    except:
        print("updateAccountInterest has errors")
        traceback.print_exc()

    try:
        newAverage = calculateAverage(accountList)
        print(f"Average balance with interest: ${newAverage:,.2f}")
    except:
        print("calculateAverage has errors")
        traceback.print_exc()


main()
