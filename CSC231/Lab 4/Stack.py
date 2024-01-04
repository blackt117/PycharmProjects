# Name : Tyler Black
# Due Date: 2/24/23
# Purpose/Algorithm:
# Step 1: I made the top of Stack the end of the list, "Index n", and the bottom of my Stack at the beginning of the list,
# 'index 0'. Runestone does it this way, and it makes sense visually for me. Also this way is more efficient for Big O
# Step 2: Made methods for this class that were specified
# Step 3: Made modifications to the driver file to understand the process better
#
# Resources: Dr. Pence and Runestone
#
#
#
class Stack(object):
    def __init__(self):
        '''
        Purpose: Create new stack

        Parameter: Self

        Return: None
        '''
        self.myStack = [] #initalize as a list

    def __str__(self):
        '''
        Purpose: Print out a representation of the stack

        Parameter: Self

        Return: Str version of the stack
        '''
        return str(self.myStack)

    def is_empty(self):
        '''
        Purpose: Check to see if the stack is empty

        Parameter: Self

        Return: Boolean Value
        '''
        if len(self.myStack) == 0:
            return True
        else:
            return False

    def push(self,item):
        '''
        Purpose: Add an item to the stack

        Parameter: Self, item

        Return: Boolean Value
        '''
        self.myStack.append(item) #O(1), why it's created this way

    def size(self):
        '''
        Purpose: Return the length of the stack

        Parameter: Self

        Return: Length of the Stack (int)
        '''
        return len(self.myStack)

    def peek(self):
        '''
        Purpose: To view the item at the top of the stack

        Parameter: Self

        Return: Item at the top of the stack
        '''
        return self.myStack[-1]

    def pop(self):
        '''
        Purpose: To remove the item at the top of the stack

        Parameter: Self

        Return: Item at the top of the stack
        '''
        if not self.is_empty():
            return self.myStack.pop() #O(1), why it's created this way

    #just for fun
    def Bin(self, num):
        '''
        Purpose: To convert a decimal number to a binary number (positives only)

        Parameter: Self, num

        Return: Binary Representation of the Decimal Number
        '''
        BinNumber = ''
        if num == 0:
            return 0
        while num > 0:
            quotient = num // 2
            remainder = num % 2
            num = quotient
            self.myStack.append(remainder)
        while len(self.myStack) != 0:
            BinNumber = BinNumber + str(self.myStack.pop())
        return BinNumber

    #more fun
    def BaseChange(self,num):
        '''
        Purpose: To convert a decimal number to a base specified by user (positives only, up to hexadecimal)

        Parameter: Self, num

        Return: None
        '''
        BaseNumber = ''
        finalnum = num
        ui = int(input('Please enter a base '))
        Base_units = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
        if num == 0:
            return 0
        while num > 0:
            quotient = num // ui
            remainder = num % ui
            num = quotient
            self.myStack.append(Base_units[remainder])
        while len(self.myStack) != 0:
            BaseNumber = BaseNumber + str(self.myStack.pop())
        print(finalnum,'in base',ui,'is',BaseNumber)
