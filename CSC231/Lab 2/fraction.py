class Fraction (object):
    def __init__(self, numerator, denominator):
        """
        Purpose: Inits Fraction with values numerator and denominator
        Raises a TypeError Exception if a non integer value is provided for the numerator or denominator
        Raises a ValueError exception if a value of zero is provided for the denominator

        Parameter: self, numerator, denominator

        Return: None
        """
        if isinstance(numerator, int) and isinstance(denominator,int):
            if denominator == 0:
                raise ValueError('Divide by Zero Error')
            self.__numerator = numerator
            self.__denominator = denominator
            self.reduce()
        elif isinstance(numerator, int) == False and isinstance(denominator, int) == False:
            raise TypeError('Numerator and Denominator must be an Integer')
        elif isinstance(denominator, int) == False:
            raise TypeError('Denominator must be an Integer')
        else:
            raise TypeError('Numerator must be an Integer')


    def getNumerator(self):
        """
        Purpose: Returns the numerator of a Fraction

        Parameter: Self

        Return: self.__numerator
        """
        return self.__numerator

    def getDenominator(self):
        """
        Purpose: Returns the denominator of a Fraction

        Parameter: Self

        Return: self.__denominator
        """
        return self.__denominator

    def setNumerator(self,value):
        """
        Purpose: Sets the numerator of a Fraction to the provided value
        Raises a TypeError Exception if a non integer value is provided

        Parameter: Self and value

        Return: None
        """
        if isinstance(value, int):
            self.__numerator = value
            self.reduce()
        else:
            raise TypeError('Numerator must be an Integer')

    def setDenominator(self,value):
        """
        Purpose: Sets the denominator of a Fraction to the provided value.
        Raises a ValueError exception if a value of zero is provided
        and Raises a TypeError Exception if a non integer value is provided

        Parameter: self and value

        Return: None
        """
        if isinstance(value, int):
            if value==0:
                raise ValueError ('Divide by Zero Error')
            self.__denominator = value
            self.reduce()
        else:
            raise TypeError('Denominator must be an Integer')

    def __str__(self):
        '''
        Purpose: To provide the Numerators and Denominators of fraction in Standard Fraction Form, i.e., (numerator/denominator)
        when print() is invoked. Reduce to a whole number if necessary -> 0/1 = 0 and 5/1 = 5

        Parameters: self.__numerator and self.__denominator (self)

        Return: Fraction form of the numerator and denominator
        '''
        if self.__numerator == 0:
            return str(0)
        elif self.__denominator == 1:
            return str(self.__numerator)
        else:
            return str(self.__numerator)+'/'+str(self.__denominator)

    def __calcGCD(self):
        '''
        Purpose: Calculate the greatest common divisor (GCD) of both the numerator and denominator

        Parameters: self.__numerator and self.__denominator (self)

        Return: The GCD
        '''
        maxValue = abs(max(self.__numerator, self.__denominator))
        minValue = abs(min(self.__numerator, self.__denominator))
        while minValue != 0:
            temp = minValue
            minValue = maxValue % minValue
            maxValue = temp
        return maxValue

    def reduce(self):
        '''
        Purpose: Set the new values of self.__numerator and self.__denominator by using integer division between the initial
        values of self.__numerator and self.__denominator with the GCD of the initial two values of these variables, respectively

        Parameter: self

        Return: None
        '''
        gcd = self.__calcGCD()
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd

    def __neg__(self):
        """
        Purpose: Returns a new Fraction equal to the negation of self

        Parameter: Self

        Return: Negated Fraction
        """
        return Fraction(-self.__numerator, self.__denominator)

    def __eq__(self,rightFrac):
        '''
        Purpose: To test whether two fractions are equal to one another

        Parameter: self and rightFrac

        Return: Boolean Value(True or false)
        '''
        if self.__numerator == rightFrac.getNumerator() and \
            self.__denominator == rightFrac.getDenominator():
            return True
        else:
            return False

    def __ne__(self,rightFrac):
        '''
        Purpose: To test whether two fractions are NOT equal to one another

        Parameter: self and rightFrac

        Return: Boolean Value(True or false)
        '''
        if self.__numerator == rightFrac.getNumerator() and \
            self.__denominator == rightFrac.getDenominator():
            return False
        else:
            return True

    def __ge__(self,rightFrac):
        '''
        Purpose: To test whether self (leftFrac) is greater than OR equal to another fraction(rightFrac)

        Parameter: self and rightFrac

        Return: Boolean Value(True or false)
        '''
        First_CrossMulti = self.__numerator * rightFrac.getDenominator()
        Second_CrossMulti = self.__denominator * rightFrac.getNumerator()

        return First_CrossMulti >= Second_CrossMulti

    def __gt__(self,rightFrac):
        '''
        Purpose: To test whether self (leftFrac) is greater than another fraction(rightFrac)

        Parameter: self and rightFrac

        Return: Boolean Value(True or false)
        '''
        First_CrossMulti = self.__numerator * rightFrac.getDenominator()
        Second_CrossMulti = self.__denominator * rightFrac.getNumerator()

        return First_CrossMulti > Second_CrossMulti

    def __lt__(self,rightFrac):
        '''
        Purpose: To test whether self (leftFrac) is less than another fraction(rightFrac)

        Parameter: self and rightFrac

        Return: Boolean Value(True or false)
        '''
        First_CrossMulti = self.__numerator * rightFrac.getDenominator()
        Second_CrossMulti = self.__denominator * rightFrac.getNumerator()

        return First_CrossMulti < Second_CrossMulti

    def __le__(self,rightFrac):
        '''
        Purpose: To test whether self (leftFrac) is less than OR equal to another fraction(rightFrac)

        Parameter: self and rightFrac

        Return: Boolean Value(True or false)
        '''
        First_CrossMulti = self.__numerator * rightFrac.getDenominator()
        Second_CrossMulti = self.__denominator * rightFrac.getNumerator()

        return First_CrossMulti <= Second_CrossMulti

    def __add__(self, rightFrac):
        """
        Purpose: Returns a new reduced Fraction equal to self + (addition) rightFrac

        Parameter: self and rightFrac

        Return: A new reduced Fraction equal to self + rightFrac
        """
        numer = self.__numerator * rightFrac.getDenominator() + rightFrac.getNumerator() * self.__denominator
        denom = self.__denominator * rightFrac.getDenominator()

        return Fraction(numer,denom)

    def __sub__(self, rightFrac):
        """
        Purpose: Returns a new reduced Fraction equal to self - (subtraction) rightFrac

        Parameter: self and rightFrac

        Return: A new reduced Fraction equal to self - rightFrac
        """
        return self + (-rightFrac)

    def __mul__ (self,rightFrac):
        """
        Purpose: Returns a new reduced Fraction equal to self * (multiplication) rightFrac

        Parameter: self and rightFrac

        Return: A new reduced Fraction equal to self * rightFrac
        """
        numer = self.__numerator * rightFrac.getNumerator()
        denom = self.__denominator * rightFrac.getDenominator()
        return Fraction(numer,denom)

    def __truediv__(self,rightFrac):
        """
        Purpose: Returns a new reduced Fraction equal to self / (division) rightFrac

        Parameter: self and rightFrac

        Return: A new reduced Fraction equal to self / rightFrac
        """
        numer = self.__numerator * rightFrac.getDenominator()
        denom = self.__denominator * rightFrac.getNumerator()
        return Fraction(numer,denom)