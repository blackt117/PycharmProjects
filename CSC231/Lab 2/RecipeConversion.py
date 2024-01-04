from fraction import *
# Name: Tyler Black
# Due Date: 2/10/23
# Algorithm:
# Instructor Comments:
# Step 1:The goal of this program is to convert the measured amount of ingredients in a recipe, based on a provided conversion factor,
#        to vary the number of servings.
# Step 2: You should fully step through this code and make sure what you are working with before you try to write the two functions above.
# Step 3: Go through the function removeMeasure and add comments to show me that you understand what the code is doing.
# Step 4: Go through the function scanAsFraction and add comments to show me that you understand what the code is doing.
# Step 5: Step through main and follow what the program is doing!!
# Step 6: Do not modify main, removeMeasure or scanAsFraction - you can add comments.
#
# My Comments:
# Step 1: Ask user for input and output files. Give user three attempts to put in a correct file. Raise IOError if user does not.
# Step 2: Ask user for conversion factor. Make this factor into a fraction using scanAsFraction
# Step 3: Create an output file named 'conv_' + input file to avoid overwriting
# Step 4: Read each line in the inputfile and store the numerical instructions (fracPart) using ScanAsFraction and non-numerical instructions of each line (linePart)
# using removeMeasure().
# Step 5: Multiply the conv_factor by the fracPart to obtain the new numerical instructions and concate this with linePart. Write this concatenation line by line in the
# output file.
# Step 6: Close input and output files and write a completion message to the user.
#
#
# Resources: Dr. Pence



def getFile():
    '''
    Returns as a tuple the file name entered by the user and the
    open file object. If the file exceeds three attempts of opening
    successfully, an IO exception is raised.
    '''
    # code goes here
    attempts = 0 #counter for the number of incorrect attempts
    opened = False  #flag to say a correct file hasn't been opened yet
    while attempts < 3 and not opened: #a while loop to allow the user to input three files
        try:
            file_name = input('Enter the recipe file name: ')
            input_file = open(file_name, 'r') # this part of the code will only be opened if it's a correct file
            opened = True # this breaks the loop
        except FileNotFoundError:
            attempts += 1 #increase counter since an invalid input file is entered
            print('Didn\'t open. You get three attempts. Attempt #', attempts) # tell user how many attempts they've used
    if attempts == 3: #if after the loop has ended, raise an error to allow the code to 'run'/"end politely" and not pop up error messages
        raise IOError ('Unable to successfully open recipe. End.')
    return (file_name, input_file) #for future purposes, only will happen if a correct input file is added


# don't touch removeMeasure
def removeMeasure(line):
    '''
    Returns provided line with any initial digits and fractions (and any surrounding blanks) removed.
    '''
    k = 0
    blank_char = ' ' #variable for space character

    while k < len(line) and (line[k].isdigit() or line[k] in ('/', blank_char)): # iterate through the line and dont include digit strings, the '/',
        # or the space character, the first part of the code is always the numbers so once it's not one of these characters, start at this index
        k = k + 1
    return line[k:len(line)] #use splicing to include only non digit string characters (need to keep this code for later, no modifications)


# don't touch scanAsFraction
def scanAsFraction(line):
    '''
    Scans all digits, including fractions, and returns as a Fraction
    object. For example, '1/2' would return as Fraction value 1/2,
    '2' would return as Fraction 2/1, and '2 1/2' would return as
    Fraction value 3/2.
    '''
    completed_scan = False # boolean flag to say you haven't iterated over the line yet
    value_as_frac = Fraction(0, 1) # initialization. Calls fraction class. Essentially zero. Using this also for mixed fractions like 1 1/2.
    # So the code is written as 1 1/2 will be operated like 1/1 + 1/2 which is 3/2 using our fraction class.

    while not completed_scan:
        k = 0 #indexing purposes
        while k < len(line) and line[k].isdigit():
            k = k + 1 # updated index to make sure you're iterating over the line and you're including the numerator, if of course
            #a digit is present

        numerator = int(line[0:k]) #first digit captured will be your numerator, type cast the string to an integer

        if k < len(line) and line[k] == '/': # the second part of this AND statement makes sure you're in a fraction
            k = k + 1 #update k to not include the '/' character
            start = k # create a new variable to store this value
            while k < len(line) and line[k].isdigit():
                k = k + 1 #update k

            denominator = int(line[start:k]) #capture the denominator
        else:
            denominator = 1 # if the next character is a space. This line is big for mixed fractions. Ex, 1 1/2 is captured as two
            #fractions... 1/1 and 1/2. value_as_frac creates the fraction form of this mixed fraction by adding 1/1 to 1/2.
        value_as_frac = value_as_frac + Fraction(numerator, denominator) #zero plus whatever you scanned as the fraction
        #Also needed for mixed fractions

        if k == len(line): #This line will only be hit if the line is empty
            completed_scan = True
        else:
            line = line[k:len(line)].strip() #reinitialize line. We iterate over the new line, without the values we already captured;
                                        #strip gets rid of the space at the beginning of the line and new line character at the end
            if not line[0].isdigit(): # the case where the spliced line in the previous line no longer has numbers
                completed_scan = True  #break the loop

    return value_as_frac #return the Fraction you created by reading the line. Could just be one fraction (1/2) or
    # an addition of two fractions 1/1 +1/2 (mixed fraction in the cake.txt file)

def convertLine(line, factor):
    '''
    If line begins with a digit, then returns line with the value
    incremented by factor. Otherwise, returns line unaltered.
    (For example, for a factor of 2, '1/4 cup sugar' returns as
    '1/2 cup sugar and '2 cups sugar' returns as '4 cups sugar'.)
    '''
    # code goes here
    # The idea is that you are going to step through the line of the recipe
    # if you find the digit in the line
    # scan through the line looking for the fraction and mulitply it by the factor to create a new fraction
    # then you need to build the new line by removing the original measure and putting the new fraciton measure in the line
    # return the new line
    # this method should utilize the scanasfraction and removemeasure functions


    if line[0].isdigit(): #to make sure the initial part of the line is a number. cake.txt number instructions are always at the beginning
        linePart= removeMeasure(line) #capture the non-numerical instructions of the document
        fracPart = scanAsFraction(line) #capture the numerical instructions of the document
        newFrac = factor * fracPart #times the numerical instructions of the document by the conv_factor (factor)
        conv_line = str(newFrac) + ' ' + linePart #use string concatenation to combine the new 'fracPart' and the 'linePart'
        return conv_line #for future purposes, to write this line into the output file
    else: # no need to modify line that has no numerical instruction
        return line


# Do not change anything below this line!
# You are responsible for writing the 2 empty functions above
# ---- main
# This is where the program begins running
# Step through this and make sure you understand what main is doing
# display welcome
def main():
    '''
    Created a Main Function.

    Purpose: Where the flow and execution of the program happens

    Parameter: None

    Return: None
    '''

    print('This program will convert a given recipe to a different')
    print('quantity based on a specified conversion factor. Enter a')
    print('factor of 1/2 to halve, 2 to double, 3 to triple, etc.\n')
    try:
        file_name, input_file = getFile()  # get file name and open file, give the user only three attempts to put a valid input file
        conv_factor = input('Enter the conversion factor: ') # get conversion factor
        conv_factor = scanAsFraction(conv_factor) #convert the conv_factor into a fraction
        output_file_name = 'conv_' + file_name  #to avoid overwriting
        output_file = open(output_file_name, 'w') # open output file named 'conv_' + file_name
        # convert recipe
        empty_str = '' #flag to see if we've reached the end of the txt file
        recipe_line = input_file.readline()  #you are converting the recipe line by line
        while recipe_line != empty_str:     #while we haven't gotten to the end of the file
            recipe_line = convertLine(recipe_line, conv_factor)    #create the new line of the conversion recipe
            output_file.write(recipe_line)      #write the new line to the new file
            recipe_line = input_file.readline()   #get the next line of the original recipe (cake.txt)
        # close files
        input_file.close()
        output_file.close()
        # display completion message to user
        print('Converted recipe in file: ', output_file_name)
    except IOError as err_mesg:  # catch file open error
        print(err_mesg)

main()