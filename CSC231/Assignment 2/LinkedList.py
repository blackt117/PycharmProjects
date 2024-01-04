###########################
# Name: Tyler Black
# Due Date: 3/24/23
# Algorithm: Creating a linked list and node class. Node has two instance variables (self.next and self.data).
# Linked list has two instance variables (self.head and self.count). Node has two methods (__init__ and __str__).
# Linked List has 9 methods (__init__, add, is_empty, size, __iter__, append, pop, search, and remove)
#
# Resources: Dr. Pence and Runestone
####################################




class Node:
    def __init__(self, Value = None):
        '''
        Purpose: Initialization of the Node class
        Param: Value
        Return: none
        '''
        self.data = Value
        self.next = None


    def __str__(self):
        """
        Purpose: String Representation
        Param: None
        Return: None
        """
        return str(self.data)

class LinkedList:
    def __init__(self):
        '''
        Purpose: Initialization of the LinkedList class
        Param: None
        Return: None
        '''
        self.head = None
        self.count = 0

    def add(self,Value):
        '''
        Purpose: Add a node to the FRONT of the LinkedList
        Param: Value
        Return: None
        '''
        if self.head == None:
            newNode=Node(Value)
            self.head=newNode
        else:
            newNode=Node(Value)
            newNode.next=self.head
            self.head=newNode
        self.count = self.count + 1

    def is_empty(self):
        '''
        Purpose: Return a boolean value if the LinkedList is empty or not
        Param: None
        Return: Boolean Value
        '''
        return self.head == None

    def size(self):
        '''
        Purpose: To return the size of the LinkedList
        Param: None
        Return: The size of the LinkedList
        '''
        # current = self.head
        # count = 0
        # while current is not None:
        #     count = count + 1
        #     current = current.next
        return self.count

    def __iter__(self):
        '''
        Purpose: To iterate over the LinkedList properly (like a List)
        Param: None
        Return: None
        '''
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def append(self,Value):
        '''
        Purpose: To add a node at the BACK of the LinkedList
        Param: Value
        Return: None
        '''
        size = self.size()
        if size == 0:
            newNode = Node(Value)
            self.head = newNode
        else:
            newNode = Node(Value)
            current = self.head
            while current.next != None:
                current = current.next
            current.next=newNode
        self.count = self.count + 1

    def pop(self, pos = None):
        '''
        Purpose: To remove and return a node at the provided position.
        Param: pos
        Return: The node at the given position
        '''
        size= self.size()
        if size == 0:
            return ('List is Empty')
        if pos == None:
            pos = size - 1
        if not isinstance(pos,int):
            return ('Invalid Input')
        if pos >= size or pos <0:
            return ('Invalid Input')
        if pos == 0:
            current=self.head
            self.head=current.next
            current.next = None
            self.count = self.count - 1
            return current
        elif pos == size-1:
            previous = self.head
            current = self.head
            while current.next != None:
                previous = current
                current = current.next
            previous.next = None
            self.count = self.count - 1
            return current
        else:
            count = 0
            previous = self.head
            current = self.head
            while count < pos:
                previous = current
                current = current.next
                count += 1
            previous.next = current.next
            current.next = None
            self.count = self.count - 1
            return current

    def search(self,Value):
        '''
        Purpose: To check if a given value is in the LinkedList
        Param: Value
        Return: Boolean Value
        '''
        size = self.size()
        if size == 0:
            return (False, 'List is Empty')
        for index in self:
            if index.data == Value:
                return True
        return False

    def remove(self,Value):
        '''
        Purpose: To remove a value (node) from the LinkedList (not an index)
        Param: Value
        Return: None
        '''
        current = self.head
        previous= None
        while current != None:
            if current.data == Value:
                break
            previous = current
            current = current.next
        if current is None:
            raise ValueError (f'{Value} is not in List')
        if previous == None:
            self.head = current.next
            self.count = self.count - 1
        else:
            previous.next = current.next
            self.count = self.count - 1



