from LinkedList import *
from car import *

def check_file(filename):
    '''
    Purpose: To check validity of the user's input file. Boolean flag is implemented to keep asking the user of an inputfile
    until a valid name is entered.

    Parameter: Filename (input file from user)

    Return: Check (Boolean Flag/Variable, 1 if file is valid/correct, 0 if file is invalid/incorrect)
    '''

    with open (filename,'r') as file:
        for line in file:
            Check=1 #This line will only be reached if a valid inputfile is entered. Tells the program to quit asking for
            #an input file
    return 1

def readfile (filename):
    cars = LinkedList()
    counter = 0
    with open(filename,'r') as file:
        for line in file:
            if counter !=0:
                line=line.strip()
                line=line.split(',')
                car1 = Car(line[0], line[1], line[2])
                cars.append(car1)
            counter = counter + 1
    return cars



def sortlist(cars):
    sortedCars = LinkedList()
    sortedCars.append(cars.head)
    current = cars.head.next
    while current != None:
        if current.data.year == int(1994):
            previous.next = current
        elif current.data.year < int(1998):
            sortedCars.add(current)
        else:
            sortedCars.append(current)
        previous = current
        current = current.next
    print('The new sorted list is:')
    for x in sortedCars:
        print(x)



def search(mileage,filename):
    found = False
    counter = 0
    with open(filename,'r') as file:
        for line in file:
            if counter !=0:
                line=line.strip()
                line=line.split(',')
                if mileage == int(line[1]):
                    found = True
                    print(f'The specifications of this car are, Year: {line[0]}, Mileage: {line[1]}, Year: {line[2]}')
                    break
            counter = counter + 1
    if found != True:
        print('Sorry the car is not existent')




def writefile(inputfile):
    counter = 0
    newlist = []
    with open(inputfile, 'r') as file:
        for line in file:
            line = line.strip()
            if counter != 0:
                line = line.split(',')
                newprice = int(line[2]) - (.1 * int(line[2]))
                newlist.append(f'{line[0]}     {line[1]}                         {newprice}')
            else:
                newlist.append(line)
            counter = counter + 1
    with open('ford_escorts_sale.csv', 'w') as file1:
        for x in newlist:
            file1.write(str(x) + '\n')


def main():
    print('Hello welcome to my program')
    inputfile = input('Input file name: ') #Ask user for input file
    Check=0 # Boolean Flag, to keep asking the user for a file if they've entered an invalid one
    try: #error handling
        Check=check_file(inputfile) #call this function to check the validity of the file, Check is returned
    except FileNotFoundError:
        inputfile = input("File not found. Try again: ") #capture and ask the user for a new input file if
        #their previous one was invalid
    while Check !=1: #continue to check validity (Check will be '1' if the file is valid; thus the loop will break once the file is
            #valid)
        try:
            Check = check_file(inputfile)
        except FileNotFoundError:
            inputfile = input("File not found. Try again: ") #continue to ask and capture the user's filenames until correct file is
                #inputted
    cars = readfile(inputfile)
    print()
    print('So far the list of cars is: ')
    for x in cars:
        print(x)
    print()
    writefile(inputfile)
    Mileage = int(input('Please enter a Mileage of a car you would like to search for '))
    search(Mileage,inputfile)
    print()
    sortlist(cars)



main()
