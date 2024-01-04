import fraction
# Name: Tyler Black
# Due Date: 2/3/23
# Algorithm:
# Step 1: Create a fraction.py file and create each method for the fraction class (boolean and arithmetic operations).
# Starting with __init__, getters, setters, and __str__method to showcase the variables in the standard fraction form
# Step 2: Create a fraction_test.py file to test each method created in the fraction.py file
#
# Resources: Dr. Pence, Andrew Davison, and Runestone

def main():
    FracA = fraction.Fraction(1,2)
    FracF = fraction.Fraction(5,1)
    FracG = fraction.Fraction(36,6)
    FracH = fraction.Fraction(0,5)
    FracJ = fraction.Fraction(1,4)
    print('Testing the __init__ and __str__')
    print(FracA)
    try:
        FracD = fraction.Fraction(1.25,5)
    except TypeError as Message:
        print('Tried initializing Numerator to non-integer value -> ', Message)
    try:
        FracD = fraction.Fraction(1.25,5.5)
    except TypeError as Message:
        print('Tried initializing Numerator and Denominator to non-integer value -> ', Message)
    try:
        FracD = fraction.Fraction(1,5.5)
    except TypeError as Message:
        print('Tried initializing Denominator to non-integer value -> ', Message)
    try:
        FracJ = fraction.Fraction(5, 0)
    except ValueError as Message:
        print('Tried initializing Denominator to zero -> ', Message)
    print('\nTesting whole number simplification')
    print('36/6 should reduce to 6 -> ', FracG)
    print('5/1 should reduce to 5 -> ', FracF)
    print('0/5 should reduce to 0 -> ', FracH)
    print('\nTesting the getters:')
    print('Calling getNumerator() for Frac A: should be 1 ->', FracA.getNumerator())
    print('Calling getDenominator() for Frac A: should be 2 ->', FracA.getDenominator())
    print('\nTesting the setters:')
    FracA.setNumerator(3)
    FracJ.setNumerator(2)
    print('Calling getNumerator() for Frac A: new numerator should be 3 ->', FracA.getDenominator())
    print('Calling getNumerator() for Frac J: new numerator should be 1 because of reduction (2/4) = (1/2) ->', FracJ.getNumerator())
    FracA.setDenominator(5)
    print('Calling getDenominator() for Frac A: new denominator should be 5 ->', FracA.getDenominator())
    print('FracA is now = ', FracA)
    print('FracJ is now = ', FracJ)
    try:
        FracA.setDenominator(0)
    except ValueError as Message:
        print('Tried the 0 denominator case ->', Message)
    try:
        FracA.setNumerator(5.5)
    except TypeError as Message:
        print('Tried to set the numerator to a non-integer value -> ', Message)
    try:
        FracA.setDenominator(5.5)
    except TypeError as Message:
        print('Tried to set the denominator to a non-integer value -> ', Message)
    print('Keep Going')
    print('\nTesting Boolean Operator')
    FracB = fraction.Fraction(3,6)
    FracC = fraction.Fraction(3,5)
    print('Testing FracA(3/5) == FracB (3/6): should be False -> ', FracA==FracB)
    print('Testing FracA(3/5) == FracC (3/5): should be True -> ', FracA==FracC)
    print('\nTesting Not Equal')
    print('Testing FracA(3/5) != FracB (3/6): should be True -> ', FracA != FracB)
    print('Testing FracA(3/5) != FracC (3/5): should be False -> ', FracA != FracC)
    print('\nTesting Greater than or equal to')
    print('Testing FracA(3/5) >= FracB (3/6): should be True -> ', FracA >= FracB)
    print('Testing FracA(3/5) >= FracC (3/5): should be True -> ', FracA >= FracC)
    print('\nTesting Greater than')
    print('Testing FracA(3/5) > FracB (3/6): should be True -> ', FracA > FracB)
    print('Testing FracA(3/5) > FracC (3/5): should be False -> ', FracA > FracC)
    print('\nTesting Less than or Equal to')
    print('Testing FracA(3/5) <= FracB (3/6): should be False -> ', FracA <= FracB)
    print('Testing FracA(3/5) <= FracC (3/5): should be True -> ', FracA <= FracC)
    print('\nTesting Less than')
    print('Testing FracA(3/5) < FracB (3/6): should be False -> ', FracA < FracB)
    print('Testing FracA(3/5) < FracC (3/5): should be False -> ', FracA < FracC)
    print('\nTesting Negation')
    print('Testing -FracA: Should be -3/5 - > ', -FracA)
    print('\nTesting Addition')
    print(f'{FracA} + {FracB} = ', FracA + FracB)
    print(f'{FracA} + {FracC} = ', FracA + FracC)
    print(f'{FracA} + {FracG} = ', FracA + FracG)
    print('\nTesting Subtraction')
    print(f'{FracA} - {FracB} = ', FracA - FracB)
    print(f'{FracA} - {FracC} = ', FracA - FracC)
    print(f'{FracA} - {FracG} = ', FracA - FracG)
    print('\nTesting Multiplication')
    print(f'{FracA} * {FracB} = ', FracA * FracB)
    print(f'{FracA} * {FracC} = ', FracA * FracC)
    print(f'{FracA} * {FracG} = ', FracA * FracG)
    print('\nTesting Division')
    print(f'({FracA}) / ({FracB}) = ', FracA / FracB)
    print(f'({FracA}) / ({FracC}) = ', FracA / FracC)
    print(f'{FracA} / {FracG} = ', FracA / FracG)




main()