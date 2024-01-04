# Name : Tyler Black
# Due Date: 2/24/23
# Purpose/Algorithm:
# Step 1: I made the front of deque the end of the list, "Index n", and rear of my deque at the beginning of the list,
# 'index 0'. Runestone does it this way, and it makes sense visually for me.
# Step 2: Made methods for this class that were specified and copied some from my Stack and Queue classes like is_empty and size
# Step 3: Made modifications to the driver file to understand the process better
#
# Resources: Dr. Pence and Runestone

class Deque:
    def __init__(self):
        '''
        Purpose: Create new deque

        Parameter: Self

        Return: None
        '''
        self.myDeque = []

    def __str__(self):
        '''
        Purpose: Print a representation of the deque

        Parameter: Self

        Return: None
        '''
        return str(self.myDeque)

    def is_empty(self):
        '''
        Purpose: Check to see if the deque is empty

        Parameter: Self

        Return: Boolean Value
        '''
        if len(self.myDeque) == 0:
            return True
        else:
            return False

    def size(self):
        '''
        Purpose: To return the length of the deque

        Parameter: Self

        Return: The length of the dequeue (int)
        '''
        return len(self.myDeque)

    def add_front(self, item):
        '''
        Purpose: To add an item at the front of the deque (end of the list for this setup)

        Parameter: Self, item

        Return: None
        '''
        self.myDeque.append(item)

    def add_rear(self,item):
        '''
        Purpose: To add an item at the rear of the deque (beginning of the list for this setup)

        Parameter: Self, item

        Return: None
        '''
        self.myDeque.insert(0,item)

    def remove_front(self):
        '''
        Purpose: To remove and return an item at the front of the deque (end of the list for this setup)

        Parameter: Self

        Return: item at the front of the deque
        '''
        if not self.is_empty(): #to make sure there are no errors formulated
            return self.myDeque.pop()

    def remove_rear(self):
        '''
        Purpose: To remove and return an item at the rear of the deque (beginning of the list for this setup)

        Parameter: Self

        Return: Item at the rear of the deque
        '''
        if not self.is_empty(): #to make sure there are no errors formulated
            return self.myDeque.pop(0)