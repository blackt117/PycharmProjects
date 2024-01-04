# ==========================================
# Tyler Black
# Due: 1/27/2023
# Algorithm:
    # Step 1: Copy Code from Canvas
    # Step 2: Modify Code (only the main() is modified)
    # Step 3: Enter Input Statement asking if it's the user's first semester
    # Step 4: Iterate Input Statement in a while loop until a correct input is entered ('y', 'Y' , 'N', or 'n')
    # Step 5: Use selective control (if/else) for correct GPA calculation based off the input entered in the previous step
            #if input is ('Y' or 'y'), cumulative_gpa_info is set to (0,0),
            #If not, user is asked for total_credits and cumulative_gpa which are then assigned to
            # cumulative_gpa_info = (total_credits, cumlative_gpa)
# References: Dr. Pence, Prior Knowledge, and Andrew Davidson
#===========================================
# Semester GPA Calculation
# Purpose: This program will calculate a student’s semester #grade
# by using the students previous credits/GPA and then asking the #student
# for their letter grades and the matching credit hours for that #grade.
# The program will print out the students semester  GPA followed by a #cumulative
# GPA

# ----function definition section
# Here is where you are going to put all of your function definitions
def getGrades():
    '''
    Purpose: To get all of the semester grades the user would like to # use in
    the calculation We will handle prompting the user for the letter grade and the
    credit hours, for as many classes as they want. We will do error handling to make
    sure it is a correct letter grade.We are going to store the grades and credit
    hours in a list of sublists.

    Parameters: none

    Return: The value returned is a list of sublists, in which each sublists contains
    the letter grade for a given course and the associated  # number of credits, for
    example[[‘A’, 3], [‘B’, 4], [‘A’, 3], [‘C’, 3]
    '''
    #create a list to hold each of the (grade,points) pairings
    semester_info = []
    #create a Boolean flag to handle how many times we prompt the user
    more_grades = True
    #use the empty string variable to determine when the user is done
    empty_str = ''
    #while the user still wants to enter more_grades
    while more_grades:
    # prompt the user for the first grade
        course_grade = input('Enter grade (hit Enter if done): ')
        while course_grade not in ('A','B','C','D','F', empty_str):
            course_grade = input('Enter letter grade received: ')
            # if the user didn’t enter a grade they must be done
        if course_grade == empty_str:
                # since they are done we need to flip the flag
            more_grades = False
        else:
            # since they entered a grade we need to ask for the credits
            num_credits = int(input('Enter number of credits: '))
            # add the (grade, credits) pairing to the list
            semester_info.append([num_credits, course_grade])
        #course_grade = input('Enter letter grade received: ')
        # return the list of grades and credits back to main
    return semester_info

def convertGrade(grade):
    '''
    Purpose: To convert a letter grade to its corresponding numerical value. This value is used to calculate the quality points that are used to
    calculate the GPA.

    Parameters: a string containing the letter grade, called grade

    Return: an integer value containing the corresponding quality points
    '''
    if grade == 'F':
        return 0
    else:
    # calculation for quality points
        return 4 - (ord(grade) - ord('A'))


def calculateGPA(sem_grades_info, cumulative_gpa_info):
    '''
    Purpose: To get all of the semester grades the user would like to use in the calculation.
    We will handle prompting the user for the letter grade
    and the credit hours, for as many classes as they want. We will do error
    handling to make sure it is a correct letter grade. We are going to store
    the grades and credit hours in a list of sublists.

    Parameters or Arguments: the semester grades, and the cumulative gpa info
    we got earlier.

    Return: The value returned is a list of sublists, in which each sublists
    contains the letter grade for a given course and the associated number of
    '''
    #create two variables for the credit hours and quality points
    #used for summing up totals
    sem_quality_pts = 0
    sem_credits = 0
    #create two variables that hold a copy from the tuple we passed in
    #tuple can’t be changed, se we must make a copy that we can update
    current_cumulative_gpa, total_credits = cumulative_gpa_info
    #for each of the credit,grade pairings in the list
    for k in range(len(sem_grades_info)):
    # store the first credits,grade pairing into new variables
        num_credits, letter_grade = sem_grades_info[k]
    # totaling up the quality points using the numcredits and
    #our helper function to give us the quality points of that grade
        sem_quality_pts = sem_quality_pts + num_credits * convertGrade(letter_grade)
    #totaling up the credits for the semester
        sem_credits = sem_credits + num_credits
    #calculation for the semester gpa
        sem_gpa = sem_quality_pts / sem_credits
    #calculation for the cumulative gpa
        new_cumulative_gpa = (((current_cumulative_gpa * total_credits) + (sem_gpa * sem_credits)) / (total_credits + sem_credits))
    # return the semester gpa and the new cumulative gpa
    return (sem_gpa, new_cumulative_gpa)

# -----main section
# Here is where your program flow and execution is going to happen
def main():
    '''
    Here is where your program flow and execution is going to happen
    '''
    print('This program calculates semester and cumulative GPAs\n')
# get current GPA info
    total_credits = int(input('Enter total number of earned credits: '))
    cumulative_gpa = float(input('Enter your current cumulative GPA: '))
    cumulative_gpa_info = (cumulative_gpa, total_credits)
# get current semester grade info
    print()   #for spacing purposes
# call the function getGrades() and store the results into semester_grades
    semester_grades = getGrades()
# Note: semester_grades will take on the same type as the values returned
# from getGrades()
# calculate semester gpa and new cumulative gpa
# we call the function calculateGPA and we pass it the list of semester
# grades and the tuple holding the cumulative info
# then we store the results from calculateGPA into two variables.
    sem_gpa, cumulative_gpa =  calculateGPA(semester_grades,cumulative_gpa_info)
# display semester gpa and new cumulative gpa
    print('\nYour semester GPA is', format(sem_gpa, '.2f'))
    print('Your new cumulative GPA is', format(cumulative_gpa, '.2f'))

main()