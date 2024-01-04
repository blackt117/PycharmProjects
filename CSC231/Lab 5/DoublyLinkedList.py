###########################
# Name: Tyler Black
# Due Date: 3/20/23
# Algorithm: Creating a DoublyLinked list and node class. Node has three instance variables (self.next, self.previous and self.data).
# DoublyLinkedList has three instance variables (self.head, self.tail, and self.count). Node has two methods (__init__ and __str__).
# DoublyLinkedList has 9 methods (__init__, add, is_empty, size, __iter__, append, pop, search, and remove)
#
# Resources: Dr. Pence and Runestone
####################################

class Node:
    def __init__(self, Value = None):
        '''
        Purpose: Initialization of the Node class
        Param: Value
        Return: None
        '''
        self.data = Value
        self.next = None
        self.previous = None

    def __str__(self):
        '''
        Purpose: String Representation
        Param: None
        Return: None
        '''
        return str(self.data)

class DoublyLinkedList:

    def __init__(self):
        '''
        Purpose: Initialization of the DoublyLinkedList class
        Param: None
        Return: None
        '''
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        '''
        Purpose: Return a boolean value if the DoublyLinkedList is empty or not
        Param: None
        Return: Boolean Value
        '''
        return self.head == None

    def size(self):
        '''
        Purpose: To return the size of the DoublyLinkedList
        Param: None
        Return: The size of the DoublyLinkedList
        '''
        return self.count

    def __iter__(self):
        '''
        Purpose: To iterate over the DoublyLinkedList properly (like a List)
        Param: None
        Return: None
        '''
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def add(self,Value):
        '''
        Purpose: Add a node to the FRONT of the DoublyLinkedList
        Param: Value
        Return: None
        '''
        if self.head == None:
            newNode=Node(Value)
            self.head=newNode
            self.tail=newNode
        else:
            newNode=Node(Value)
            newNode.next=self.head
            self.head.previous = newNode
            self.head=newNode
        self.count = self.count + 1

    def append(self,Value):
        '''
        Purpose: To add a node at the BACK of the DoublyLinkedList
        Param: Value
        Return: None
        '''
        size = self.size()
        if size == 0:
            newNode = Node(Value)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(Value)
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
        self.count = self.count + 1

    def pop(self, pos=None):
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
            return('Invalid Input')
        if pos >= size:
            return ('Invalid Input')
        if pos == 0:
            current = self.head
            self.head = current.next
            if self.head != None:
                self.head.previous = None
            current.next = None
            self.count = self.count - 1
            return current
        elif pos == size - 1:
            last = self.tail
            self.tail = self.tail.previous
            last.previous = None
            self.tail.next = None
            self.count = self.count - 1
            return last
        else:
            count = 0
            previous = self.head
            current = self.head
            while count < pos:
                previous = current
                current = current.next
                count +=1
            previous.next = current.next
            temp = current.next
            temp.previous = previous
            current.next = None
            self.count = self.count - 1
            return current

    def search(self, Value):
        '''
        Purpose: To check if a given value is in the DoublyLinkedList
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

    def remove(self, Value):
        '''
        Purpose: To remove a value (node) from the DoublyLinkedList (not an index)
        Param: Value
        Return: None
        '''
        current = self.head
        previous = None
        while current != None:
            if current.data == Value:
                break
            previous = current
            current = current.next
        if current is None:
            raise ValueError (f'{Value} is not in List')
        if previous == None:
            self.head = current.next
            if self.head != None:
                self.head.previous = None
            self.count = self.count - 1
        elif current.next == None:
            self.tail = previous
            previous.next = None
            self.count = self.count - 1
        else:
            previous.next = current.next
            self.count = self.count - 1


