###############
# Name: Tyler Black
# Due Date: 3/24/23
# Algorithm: Created a class for each unordered list ADT. Implemented methods of init, size, is_empty, enqueue, and dequeue respective
# of each ADT. Called to previous python files/methods when needed (for DLL, LL, and CLL).
#
#
# Resources: Dr. Pence and Runestone
#

from LinkedList import *
from DoublyLinkedList import *
from CircularlyLinkedList import *

class QueuePythonList:
    def __init__(self):
        '''
        Purpose: Initialization of a Queue using Python List
        Param: None
        Return: None
        '''
        self.list = []

    def __str__(self):
        '''
        Purpose: String Representation
        Param: None
        Return: None
        '''
        return str(self.list)

    def size(self):
        '''
        Purpose: to Return the size of the Queue
        Param: None
        Return: Integer value of the size of the Queue
        '''
        return len(self.list)

    def is_empty(self):
        '''
        Purpose: To see if the list is empty
        Param: None
        Return: Boolean Value
        '''
        if len(self.list)==0:
            return True
        else:
            return False

    def enqueue(self,item):
        '''
        Purpose: To add an item to the BACK of the queue
        Param: item
        Return: None
        '''
        self.list.insert(0,item)

    def dequeue(self):
        '''
        Purpose: To remove the item at the FRONT of the queue
        Param: None
        Return: The item at the FRONT of the queue
        '''
        if not self.is_empty():
            return self.list.pop()

class QueueLinkedList:
    def __init__(self):
        '''
        Purpose: Initialization of a Queue using a Linked List
        Param: None
        Return: None
        '''
        self.list = LinkedList()

    def size(self):
        '''
        Purpose: to Return the size of the Queue
        Param: None
        Return: Integer value of the size of the Queue
        '''
        return self.list.size()

    def is_empty(self):
        '''
        Purpose: To see if the list is empty
        Param: None
        Return: Boolean Value
        '''
        return self.list.is_empty()

    def enqueue(self,item):
        '''
        Purpose: To add an item to the BACK of the queue
        Param: item
        Return: None
        '''
        self.list.add(item)

    def dequeue(self):
        '''
        Purpose: To remove the item at the FRONT of the queue
        Param: None
        Return: The item at the FRONT of the queue
        '''
        return self.list.pop()

class QueueDoublyLinkedList:
    def __init__(self):
        '''
        Purpose: Initialization of a Queue using a DoublyLinked List
        Param: None
        Return: None
        '''
        self.list = DoublyLinkedList()

    def size(self):
        '''
        Purpose: to Return the size of the Queue
        Param: None
        Return: Integer value of the size of the Queue
        '''
        return self.list.size()

    def is_empty(self):
        '''
        Purpose: To see if the list is empty
        Param: None
        Return: Boolean Value
        '''
        return self.list.is_empty()

    def enqueue(self,item):
        '''
        Purpose: To add an item to the BACK of the queue
        Param: item
        Return: None
        '''
        self.list.add(item)

    def dequeue(self):
        '''
        Purpose: To remove the item at the FRONT of the queue
        Param: None
        Return: The item at the FRONT of the queue
        '''
        return self.list.pop()

class QueueCircularlyLinkedList:
    def __init__(self):
        '''
        Purpose: Initialization of a Queue using a CircularlyLinked List
        Param: None
        Return: None
        '''
        self.list = CircularlyLinkedList()

    def size(self):
        '''
        Purpose: to Return the size of the Queue
        Param: None
        Return: Integer value of the size of the Queue
        '''
        return self.list.size()

    def is_empty(self):
        '''
        Purpose: To see if the list is empty
        Param: None
        Return: Boolean Value
        '''
        return self.list.is_empty()

    def enqueue(self, item):
        '''
        Purpose: To add an item to the BACK of the queue
        Param: item
        Return: None
        '''
        self.list.add(item)

    def dequeue(self):
        '''
        Purpose: To remove the item at the FRONT of the queue
        Param: None
        Return: The item at the FRONT of the queue
        '''
        return self.list.pop()
