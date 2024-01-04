############
# Name: Tyler Black
# Due Date: 03/31/23
# Algorithm: Created functions for binary search, sequential search, and smart sequential search. Additionally, I wrote
# a recursion function to find the max value in a list of numbers. Finally, I wrote a hash function to deal with
# integers and strings, and functions to handle collisions with open addressing (via linear probing) and chaining
# Resources: Dr. Pence, Runestone, and Andrew
###############


def binary_search (list1,value):
    '''
    Purpose: To search for a value in a list using binary search
    Param: List of numbers and target Value
    Return: Boolean Value, if the value is in the list
    '''
    list1.sort()
    found = False
    first = 0
    last = len(list1)-1
    while first <= last and not found:
        mid = (first + last) // 2
        if value < list1[mid]:
            last = mid -1 #// search first half
        elif value > list1[mid]:
            first = mid + 1 #// search last half
        else:
            found = True #// item found
    if not found:
        mid = False
    else:
        mid = True
    return mid


def sequential_search (list1,value):
    '''
    Purpose: To search for a value in a list using sequential search
    Param: List of numbers and a target value
    Return: A tuple (boolean value if the value is in the list, integer value if value is in list
    (index spot) or NONE if not)
    '''
    found = False
    loc = 0
    inde = None
    while loc < len(list1) and not found:
        if value == list1[loc]: #// target found
            inde = loc
            found = True
        else: #// keep Searching
            loc = loc + 1
    return (found, inde)

def smart_sequential_search(list1, value):
    '''
    Purpose: To search for a value in a list using smart sequential search
    Param: List of numbers and a target value
    Return: A tuple (boolean value if the value is in the list, integer value if value is in list
    (index spot) or NONE if not)
    '''
    list1.sort()
    done = False
    found = False
    loc = 0
    while loc < len(list1) and not done:
        if value <= list1[loc]: #// either found the item, or we’ve gone past where it should be
            done = True
        else: #// keep searching
            loc = loc + 1
    if loc == len(list1) or value != list1[loc]:
        loc = None
    else:
        found = True
    return (found,loc)

def recursive_max (list1):
    '''
    Purpose: To find the max value in a list using recursion
    Param: List of numbers
    Return: Max value in the list
    '''
    if len(list1) == 1:
        return list1[0]
    else:
        result = recursive_max(list1[1:])
        return max(result,list1[0])

import random

def hashFuncInt(value,list_size):
    '''
    Purpose: To create a hash given the length of a list for an integer value
    Param: int value, list_size
    Return: Hash Value
    '''
    idx_result = value % list_size
    return idx_result

def hashStrings(value,list_size):
    '''
    Purpose: To create a hash given the length of a list for a string value
    Param: string value, list_size
    Return: Hash Value
    '''
    total = 0
    for char in value:
        total += ord(char)
    idx_result = total % list_size
    return idx_result


def testhashStringsChain():
    '''
    Purpose: To solve hash collisions by the use of chaining for string data types and prints the stored list
    Param: None
    Return: None
    '''
    names = [[] for i in range (0,5)]
    testData = ['john', 'jacob', 'henry']
    for item in testData:
        id =hashStrings(item,len(names))
        names[id].append(item)
    print(names)


def testHashOpenAdd():
    '''
    Purpose: To solve hash collisions by the use of open addressing (via linear probing) for int data types and
    prints the stored list. Additionally, prints where collisions occur and where the value is put into (index).
    Param: None
    Return: None
    '''
    ZipCode = [None] *30
    for i in range(0,30):
        zip = random.randint(10000,99999)
        result_idx = hashFuncInt(zip, len(ZipCode))
        if ZipCode[result_idx] != None:
            print(f'First Collision at spot {result_idx} for {zip}')
            ind_spot = result_idx
            count = 0
            while ZipCode[result_idx] is not None:
                if count != 0:
                    print(f'Collision at {ind_spot}')
                if result_idx == len(ZipCode):
                    result_idx = 0
                else:
                    if result_idx == len(ZipCode)-1:
                        result_idx = 0
                    else:
                        result_idx += 1
                ind_spot = result_idx
                count +=1
            print(f'Putting {zip} ultimately in spot {result_idx}')
            ZipCode[result_idx] = zip
        else:
            ZipCode[result_idx]=zip
            print(f'Putting {zip} in spot {result_idx}')
    print(ZipCode)

def testHashIntChain():
    '''
    Purpose: To solve hash collisions by the use of chaining for int data types and prints the stored list.
    Additionally, asks the user for an input and searches whether the input is in the hash table
    Param: None
    Return: None
    '''
    ZipCode = [[] for i in range(0, 20)]
    testData = []
    for i in range(0, 15):
        randNum = random.randint(10000, 99999)
        testData.append(randNum)

    for item in testData:
        id = hashFuncInt(item, len(ZipCode))
        ZipCode[id].append(item)
    print(ZipCode)
    print()
    target = int(input('Enter a Zipcode: '))
    result = hashFuncInt(target, len(ZipCode))  # hash tables are used for Google search
    print(f'{target} is in list (T/F)')
    if target in ZipCode[result]:
        print(True)
    else:
        print(False)


def main ():
    print('Testing Binary Search')
    print('2 is in list [1,5,6,7,4,2], should return True:',binary_search([1,5,6,7,4,2],2))
    print('7 is in list [1,5,6,7,4,2], should return True:',binary_search([1,5,6,7,4,2],7))
    print('1 is in list [1,5,6,7,4,2], should return True:',binary_search([1,5,6,7,4,2],1))
    print('8 is not in list [1,5,6,7,4,2], should return False:',binary_search([1,5,6,7,4,2],8))
    print('-1 is not in list [1,5,6,7,4,2], should return False:',binary_search([1,5,6,7,4,2],-1))
    print('\nTesting Sequential Search')
    print('31 is in list [11,23,58,31,56,77,43,12,65,19] at spot 3, should return (True,3):', sequential_search([11,23,58,31,56,77,43,12,65,19],31))
    print('11 is in list [11,23,58,31,56,77,43,12,65,19] at spot 0, should return (True,0):', sequential_search([11,23,58,31,56,77,43,12,65,19],11))
    print('19 is in list [11,23,58,31,56,77,43,12,65,19] at spot 9, should return (True,9):', sequential_search([11,23,58,31,56,77,43,12,65,19],19))
    print('0 is not in list [11,23,58,31,56,77,43,12,65,19], should return (False,None):', sequential_search([11,23,58,31,56,77,43,12,65,19],0))
    print('100 is not in list [11,23,58,31,56,77,43,12,65,19], should return (False,None):', sequential_search([11,23,58,31,56,77,43,12,65,19],100))
    print('\nTesting Smart Sequential Search')
    print('31 is in list [1,4,5,23,31,56,57,71,105] at spot 4, should return (True,4):',  smart_sequential_search([1,4,5,23,31,56,57,71,105],31))
    print('106 is not in list [1,4,5,23,31,56,57,71,105], should return (False,None):', smart_sequential_search([1,4,5,23,31,56,57,71,105],106))
    print('105 is in list [1,4,5,23,31,56,57,71,105] at spot 8, should return (True,8):',  smart_sequential_search([1,4,5,23,31,56,57,71,105],105))
    print('1 is in list [1,4,5,23,31,56,57,71,105] at spot 0, should return (True,0):',  smart_sequential_search([1,4,5,23,31,56,57,71,105],1))
    print('-1 is not in list [1,4,5,23,31,56,57,71,105], should return (False,None):',smart_sequential_search([1, 4, 5, 23, 31, 56, 57, 71, 105],-1))
    print('\nTesting Recursion')
    print('The max value in [25,16,10,1] should be 25:', recursive_max([25,16,10,1]))
    print('The max value in [25,16,10,50] should be 50:',recursive_max([25,16,10,50]))
    print('The max value in [24,2] should be 24:',recursive_max([24,2]))
    print()
    print('Testing Hashing')
    print('Hashing via Open Addressing for Int Values')
    testHashOpenAdd()
    print()
    print('Hashing via chaining for String Values')
    testhashStringsChain()
    print()
    print('Hashing via chaining for Int Values')
    testHashIntChain()

main()