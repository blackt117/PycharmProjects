# Program:    Test 1 Coding Portion
# Author:     Black, Tyler
# Course:     CSC 231
# Term:       Spring 2023


class BankAccount:
    def __init__(self, acctNum, fName, lName, acctBal):
        ''' This method initializes the public variables needed
        to create a bank account object.
        :param acctNum: integer
        :param fName: string
        :param lName: string
        :param acctBal: float
        :return: none
        '''

        self.acctNum = acctNum
        self.fName = fName
        self.lName= lName
        self.acctBal = acctBal
        pass

    def __str__(self):
        ''' This method creates a user friendly readable version of a
        bank account object and returns the string.
        :return: string
        '''
        acctBal = format(self.acctBal,',.2f')
        return str(self.acctNum)+','+self.lName + ',' + self.fName + ':' + ' ' + '$' + acctBal
        # return f'{self.acctNum},{self.lName}, {self.fName}: ${self.acctBal:.2f}'
        pass

    def deposit(self, amt):
        ''' This method adds the amt to the account balance.
        :param amt: float
        :return: none
        '''
        self.acctBal = amt + self.acctBal
        pass

    def withdraw(self, amt):
        ''' This method subtracts the amt from the account balance.
        :param amt: float
        :return: none
        '''
        self.acctBal = self.acctBal - amt
        pass

    def calculate_interest(self):
        ''' This method calculates the interest on an account balance
        with the formula (0.15 * account balance) and returns the amount
        of interest earned
        :return: float.
        '''
        interest = self.acctBal * .015
        return interest
        pass

    def __lt__(self,rightSide):
        ''' This method compares two account balances from two account objects
        and returns true if the left account balance < right account balance, false otherwise
        :param rightSide: BankAccount object
        :return: Boolean
        '''
        return self.acctBal < rightSide.acctBal
        pass

    def __eq__(self,rightSide):
        ''' This method compares two account numbers from two account objects
        and returns true if they are equivalent, false otherwise.
        :param rightSide: BankAccount object
        :return: Boolean
        '''
        return self.acctNum == rightSide.acctNum
        pass

