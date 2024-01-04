# Name : Tyler Black
# Due Date: 2/24/23
# Purpose/Algorithm:
# Step 1: I made the front of Queue the end of the list, "Index n", and rear of my Queue at the beginning of the list,
# 'index 0'. Runestone does it this way, and it makes sense visually for me.
# Step 2: Made methods for this class that were specified and copied some from my Stack class like is_empty and size
# Step 3: Made modifications to the driver file to understand the process better
#
# Resources: Dr. Pence and Runestone
#
#
#
class Queue():
    def __init__(self):
        '''
        Purpose: Create new queue

        Parameter: Self

        Return: None
        '''
        self.myQueue = [] #initalize as a list

    def __str__(self):
        '''
        Purpose: To print out a representation of the Queue

        Parameter: Self

        Return: String version of Queue
        '''
        return str(self.myQueue)

    def enqueue(self, item):
        '''
        Purpose: Add an item to the front of the queue

        Parameter: Self, item

        Return: None
        '''
        self.myQueue.insert(0,item)

    def is_empty(self):
        '''
        Purpose: Check to see if the list is empty

        Parameter: Self

        Return: Boolean Value
        '''
        if len(self.myQueue) == 0:
            return True
        else:
            return False

    def size(self):
        '''
        Purpose: To return the length of the Queue

        Parameter: Self

        Return: Length of the Queue (int)
        '''
        return len(self.myQueue)

    def dequeue(self):
        '''
        Purpose: Remove an item from the queue

        Parameter: Self

        Return: item at the front of the queue (end of the list in this case)
        '''
        if not self.is_empty():
            return self.myQueue.pop()

