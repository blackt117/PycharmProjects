# =========================
# Name: Tyler Black
# Due Date: February 6th
# Algorithm: (this will be more like a summary, my comments go more into detail what is happening)
# Step 1: Introduction in the main function and ask users for the input file and output file
# Step 2: Keep User in While Loop until a valid input file is inputted
# Step 3: Use functions to read the input file, capture the arbitrary tokens in the input file, ask the user what they want the
#         arbitrary tokens to be, replace the arbitrary tokens in the file with the input given by the user and store each line
#         of the new resulting madLib story in a list by using string concatenation.
# Step 4: Open up the output file given by the user and write each index, which corresponds to each line the resulting madLib story,
#         line by line in the output file (making sure to add new line character)
# Step 5: Ask user if they want resulting story written in terminal. Keep user in a while loop until they enter a correct input ('y', 'Y', 'n', or 'N')
#         If they inputted 'y' or 'Y', use write_terminal to read the recently created output file line by line and output each line into the terminal by using string
#         concatenation (make sure to not include new line character)
# Step 6: Ask user if they want to play the game again. Keep user in a while loop until they enter a correct input ('y', 'Y', 'n', or 'N'). If they inputted 'n' or 'N',
#         change the value of the boolean flag: play_game to break the while loop and stop the program
#
#Resources: Dr. Pence, Prior Knowledge, Andrew Davison, and Google (geeksforgeeks)
#
def check_file(filename):
    '''
    Purpose: To check validity of the user's input file. Boolean flag is implemented to keep asking the user for an input file
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
    '''
    Purpose: To read the input file, gather the correct number and type of tokens (look at side note) in the txt file game,
    ask the user what they want the tokens to be, and replace the current arbitrary tokens with the user's input. Each line is then stored
    in a list for future purposes.

    Side Note: Tokens are "action words" in a Madlib game. In this version of the game, a token is marked by the character
    '<' to the left and the character '>' to the right. Tokens are in the middle of these characters

    Parameter: Filename (input file, .txt document)

    Return: A list containing the new lines of the MadLib game called newFile
    '''
    # token='' #needed to store the arbitrary token in the txtfile
    token_def='' #stores the user's input for their token
    newFile=[] #stores the newlines for the entire madlib game result
    char_count='' #used as a flag to say we have registered a token
    newLine='' #captures the characters for the new line for the madgame result
    new_Char='' #captures each specific character to be added to the newLine variable. This is required since string concentation is crucial for this program
    with open (filename,'r') as file: #open file for reading
        beg_index = 0 #used to capture the index of char '<'
        for line in file:   #read each line
            newLine = ''    #reintialize newLine after each line is read to ensure there are no carry over from the previous line
            for index in range(len(line)):  #manipulate the sentence of the inputfile to act as "list"
                new_Char = line[index]  #initialize new_char as a character from the line being read.
                if line[index] == '>' and char_count == True:    #working backwards, seeing if we've registered a token and in that range;
                        #once we hit the character '>', we are no longer in that range. char_count makes sure we registered a token and not an independent '>'
                    char_count = False    #changed to say we are no longer in a token
                    new_Char=''     #But instead of capturing '>' in our new File, we need to add '' (empty string)
                if char_count == True:   #Signaling we are in the token range and add empty string to the newline and not the characters in the arbitrary token
                    new_Char=''
                if line[index] == '<': #Flagging the potential start of a token
                    beg_index=index     #Store the index
                    token = find_token_one(beg_index,line)  #Call find_token_one to find the arbitrary token, if we've actually hit one
                    if token == None:     #Special Case if there's an independent '<'
                        new_Char = '<'
                    else:
                        token_def = ask_tokens(token)  #Call ask_tokens to ask user what they want the token to be.
                            #The start of the token '<' is added the user token (by replacement) and char_count is signaled that we are in a token. Don't add the characters
                            # of the arbitrary token, using empty string
                        new_Char=str(token_def)
                        char_count= True #to signal we are in an arbitrary token range
                if line[index] == '\n': #since strip() cannot be used, new line character must be replaced
                    new_Char=''
                newLine=newLine+new_Char #concentate each string character into newline
            newFile.append(newLine) #Add each new modified line to the list NewFile
    return newFile #return the list for future purposes


def find_token_one (beg_index,line):
    '''
    Purpose: To find the specific arbitrary tokens in the input txt file. Each game has different ones. Additionally, to ensure the program is capturing
    tokens and not independent '<' and '>' characters.

    Parameters: beg_index (the index number of the potential start of a token), line (each line read from the txt file)

    Return: The arbitrary token in the txt file
    '''
    token='' #for string concentation
    for index in range(beg_index+1,len(line)): #manipulate the sentence of the inputfile to act as "list". Also to start at
        #index of '<' character to store only the characters of the arbitrary token
        if line[index] == '>': #We've reached the end of the arbtirary token, return the result.
            return token
        elif line[index] == '-': #Special cases in which the arbitrary token has two words joined by a hypen (hypen is removed for a space)
            token = str(token) + ' '
        else:
            token = str(token) + line[index]



def ask_tokens (token):
    '''
    Purpose: To ask the user what they want to replace the arbitrary token with and capture that word for future purposes.

    Parameter: Token (the arbitrary token in the original txt file, found in find_token_one)

    Return: tokendef (what the user inputs for the arbitrary token, a "definite token")
    '''
    tokendef=''
    if token[0] in ('a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') : #Modified for correct grammar ('an' before a vowel, 'a' before a non vowel)
        tokendef= input("Please type an " + str(token)+': ')
    elif token[0] == ' ' and token[1] in ('a','e','i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'): #Special case of the "-ing verb"
        #or if theres a case where the arbitrary token at index 0 is a '-' (hypen) and at index 1 the character is a vowel
        tokendef= input("Please type an " + str(token)+': ')
    else:
        tokendef=input('Please type a ' + str(token)+': ')
    return tokendef

def write_file(filename,newFile):
    '''
    Purpose: To write the resulting madLib story into an output file the user selected/chose

    Parameter: filename (the output file the user inputted) and newFile (the list with the lines of the resulting madlib
    story)

    Return: None
    '''
    with open (filename,'w') as file:
        for index in newFile: #Each index (in this case each line of the madLib story is written into the output file)
            file.write(str(index) + '\n') #Have to add back new line character


def write_terminal(filename):
    '''
    Purpose: To write into the terminal the madLib story if the user chooses to see the resulting madLIb story in terminal

    Parameter: filename (the output file that was the madLib story was written into)

    Return: None
    '''
    print() #for spacing
    print('Here is the resulting MadLib:')
    Result_Char='' #to capture each character in each line of the output file
    with open (filename,'r') as file: #open outputfile for reading, each line is read and outputted into the terminal
        for line in file:
            Result_Line = '' #the total string concentation of each line. Reset to empty string before a new line is read
            for index in range(len(line)): #have to index the lines like a list
                if line[index] == '\n': #have to get rid of the new line character
                    Result_Char=''
                else:
                    Result_Char=line[index] #everything is echoed from the output file except new line character
                Result_Line = Result_Line + Result_Char #string concatenation
            print(Result_Line) #print each resulting line; line by line


def main():
    '''
    Purpose: Where the flow and execution of the program happens

    Parameters: None

    Return: None
    '''
    play_game = True # Boolean Flag, so this program plays like a game
    while play_game: #while the Boolean flag is true; a value of false breaks the loop
        print('Welcome to the game of Mad Libs. ') #Introduction
        print('I will ask you to provide several words and phrases to fill in a mad lib story. ')
        print('The result will be written to an output file. ')
        print() #for spacing
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
        outputfile = input('Output file name: ')  # Ask user for output file
        print() #for spacing
        newFile = readfile(inputfile)  # call readfile() to read and store information about the input file. It's passed the inputfile, NewFile is returned
        #(the list of the resulting madLibs game (line by line))
        write_file(outputfile, newFile) #call write_file() to write the resulting madLib story in the outputfile the user inputted
        print() #for spacing
        print('Your MadLib story has been created. ')
        result_story= input ('Do you want to see the resulting story? (Y|N) ') #ask if the user wants to see the story in the terminal, capture the response
        while result_story not in ('Yy') and result_story not in ('Nn'): #keeps user in a loop until a correct response is given ('y', 'Y', 'n', or 'N')
            result_story = input('Invalid Response, Please enter (Y|N): ')
        if result_story in 'Yy':
            write_terminal(outputfile) #call this function if user inputs "y" or "Y"
        print()  # for spacing
        play_game = input('Do you want to process another Mad Lib? (Y|N) ') #ask if the user wants to play the game again, capture the response
        while play_game not in ('Yy') and play_game not in ('Nn'): #keeps user in a loop until a correct response is given ('y', 'Y', 'n', or 'N')
                play_game = input('Invalid Response, Please enter (Y|N): ')
        if play_game in ('Nn') : #break the overall main() loop if the user inputs 'N' or 'n'
            play_game=False #change the value of the boolean flag
            print('Thank you for playing my Program!')
        print()  # for spacing


main()