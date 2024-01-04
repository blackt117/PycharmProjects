class FootMeasure (object):
    def __init__(self, feet = 0, inches = 0): # keywords allow the data to be initialzed to a certain value (0 for both variables) instead
        # of NONE data type if no values are passed to the class
        """
        Purpose: Inits FootMeasure with values feet and inches


        Parameter: self, numerator, denominator

        Return: None
        """
        self.feet = feet #store feet data
        self.inches = inches #store inches data

    def __str__(self):
        '''
        Purpose: To provide a measurement in feet and/or inches when print() is invoked. What is returned is based on the input provided.
        Ex., FootMeasure() -> 0 ft. 0 in., FootMeasure(feet=5) - > 5 ft., FootMeasure(1,5) -> 1 ft. 5 in., FootMeasure(7,34) - > 9 ft. 10 in,
        FootMeasure(inches=68) -> 5 ft. 8 in., etc

        Parameters: self.feet and self.inches

        Return: Feet Measurement based on the input provided
        '''
        if self.feet == 0: #case where no feet is entered or there are no resulting feet
            self.feet= self.inches//12 # convert into feet
            self.inches = self.inches%12 # remaining inches
            if self.inches ==0 and self.feet !=0:
                return str(self.feet) + ' ft.' # cases such as 60 inches = 5 ft.
            else:
                return str(self.feet) + ' ft.' + ' ' + str(self.inches) +' in.' # for cases such as 0 ft. 0 in and 5 ft. 8 in.
        elif self.inches ==0:
            return str(self.feet) + ' ft.' #feet will just be returned as is
        else:
            if self.inches >=12: # if inches need to be modified to feet first. Such as 4 ft. 24 in. case
                self.feet = self.feet + self.inches//12 # convert to feet and add that value to the current foot value
                self.inches= self.inches % 12 # remaining inches
            if self.inches ==0: #no remaining inches -> 4 ft. 24 in. should be 6 ft. (inches are evenly divisible by 12)
                return str(self.feet) + ' ft.'
            else:
                return str(self.feet) + ' ft.' + ' ' + str(self.inches) +' in.' # if there's remaining inches, this covers the 0 ft. 0 in case
                # as well

    def __repr__(self): #copy str method
        '''
        Purpose: To provide a measurement in feet and/or inches when print() is invoked. What is returned is based on the input provided.
        Ex., FootMeasure() -> 0 ft. 0 in., FootMeasure(feet=5) - > 5 ft., FootMeasure(1,5) -> 1 ft. 5 in., FootMeasure(7,34) - > 9 ft. 10 in,
        FootMeasure(inches=68) -> 5 ft. 8 in., etc.
        In this case the repr and str methods are the same. Repr is more for debugging/development.

        Parameters: self.feet and self.inches

        Return: Feet Measurement based on the input provided
        '''
        if self.feet == 0:
            self.feet = self.inches // 12
            self.inches = self.inches % 12
            if self.inches == 0 and self.feet != 0:
                return str(self.feet) + ' ft.'
            else:
                return str(self.feet) + ' ft.' + ' ' + str(self.inches) + ' in.'
        elif self.inches == 0:
            return str(self.feet) + ' ft.'
        else:
            if self.inches >= 12:
                self.feet = self.feet + self.inches // 12
                self.inches = self.inches % 12
            if self.inches == 0:
                return str(self.feet) + ' ft.'
            else:
                return str(self.feet) + ' ft.' + ' ' + str(self.inches) + ' in.'

    def __add__(self,rightMeasure): #convert both measurements to inches
        """
        Purpose: Returns a new 'modified' FootMeasurement equal to self + (addition) rightMeasure

        Parameter: self and rightMeasure

        Return: A new 'modified' FootMeasurement equal to self + rightMeasure
        """
        leftinches = self.feet * 12 # convert left operand's feet to inches
        leftinches = leftinches + self.inches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the left operand
        rightinches = rightMeasure.feet * 12 # convert right operand's feet to inches
        rightinches = rightMeasure.inches + rightinches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the right operand
        totalinches = rightinches + leftinches #add the total inches for both operands
        totalfeet = totalinches // 12 # convert this result to feet
        totalinches = totalinches % 12 # store the remaining inches
        return FootMeasure(totalfeet, totalinches) #return the result of totalfeet and totalinches being passed through this class

    def __le__(self,rightMeasure): #convert both measurements to inches
        '''
        Purpose: To test whether self (leftMeasure) is less than OR equal to another FootMeasurement(rightMeasure)

        Parameter: self and rightMeasure

        Return: Boolean Value(True or false)
        '''
        leftinches = self.feet * 12 # convert left operand's feet to inches
        leftinches = leftinches + self.inches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the left operand
        rightinches = rightMeasure.feet * 12 # convert right operand's feet to inches
        rightinches = rightMeasure.inches + rightinches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the right operand
        return leftinches <= rightinches #return the comparsion of the right inches and left inches given the respective boolean operator

    def __lt__(self,rightMeasure): #convert both measurements to inches
        '''
        Purpose: To test whether self (leftMeasure) is less than another FootMeasurement(rightMeasure)

        Parameter: self and rightMeasure

        Return: Boolean Value(True or false)
        '''
        leftinches = self.feet * 12 # convert left operand's feet to inches
        leftinches = leftinches + self.inches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the left operand
        rightinches = rightMeasure.feet * 12 # convert right operand's feet to inches
        rightinches = rightMeasure.inches + rightinches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the right operand
        return leftinches < rightinches #return the comparsion of the right inches and left inches given the respective boolean operator

    def __eq__(self,rightMeasure): #convert both measurements to inches
        '''
        Purpose: To test whether self (leftMeasure) is equal to another FootMeasurement(rightMeasure)

        Parameter: self and rightMeasure

        Return: Boolean Value(True or false)
        '''
        leftinches = self.feet * 12 # convert left operand's feet to inches
        leftinches = leftinches + self.inches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the left operand
        rightinches = rightMeasure.feet * 12 # convert right operand's feet to inches
        rightinches = rightMeasure.inches + rightinches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the right operand
        return leftinches == rightinches #return the comparsion of the right inches and left inches given the respective boolean operator

    def __ne__(self,rightMeasure): #convert both measurements to inches
        '''
        # Purpose: To test whether self (leftMeasure) is NOT equal to another FootMeasurement(rightMeasure)
        #
        # Parameter: self and rightMeasure
        #
        # Return: Boolean Value(True or false)
        # '''
        leftinches = self.feet * 12 # convert left operand's feet to inches
        leftinches = leftinches + self.inches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the left operand
        rightinches = rightMeasure.feet * 12 # convert right operand's feet to inches
        rightinches = rightMeasure.inches + rightinches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the right operand
        return leftinches != rightinches #return the comparsion of the right inches and left inches given the respective boolean operator


        # return not (self == rightMeasure) (Another way)

    def __gt__(self,rightMeasure): #convert both measurements to inches
        '''
        Purpose: To test whether self (leftMeasure) is greater than another FootMeasurement(rightMeasure)

        Parameter: self and rightMeasure

        Return: Boolean Value(True or false)
        '''
        leftinches = self.feet * 12 # convert left operand's feet to inches
        leftinches = leftinches + self.inches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the left operand
        rightinches = rightMeasure.feet * 12 # convert right operand's feet to inches
        rightinches = rightMeasure.inches + rightinches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the right operand
        return leftinches > rightinches #return the comparsion of the right inches and left inches given the respective boolean operator

    def __ge__(self,rightMeasure): #convert both measurements to inches
        '''
        Purpose: To test whether self (leftMeasure) is greater than OR equal another FootMeasurement(rightMeasure)

        Parameter: self and rightMeasure

        Return: Boolean Value(True or false)
        '''
        leftinches = self.feet * 12 # convert left operand's feet to inches
        leftinches = leftinches + self.inches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the left operand
        rightinches = rightMeasure.feet * 12 # convert right operand's feet to inches
        rightinches = rightMeasure.inches + rightinches # add the feet inches (previous step) to 'free standing" inches to get the total
        #inches for the right operand
        return leftinches >= rightinches #return the comparsion of the right inches and left inches given the respective boolean operator

        #return not (self < rightMeasure) (another way)