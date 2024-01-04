###########################
# Name: Tyler Black
# Due Date: 3/24/23
# Algorithm: Creating a Circularlylinkedlist and node class. Node has two instance variables (self.next and self.data).
# CircularlyLinked list has three instance variables (self.head, self.last, and self.count). Node has two methods (__init__ and __str__).
# CircularlyLinked List has 9 methods (__init__, add, is_empty, size, __iter__, append, pop, search, and remove)
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
        """String"""
        return str(self.data)

class CircularlyLinkedList:
    def __init__(self):
        '''
        Purpose: Initialization of the CircularlyLinkedList class
        Param: None
        Return: None
        '''
        self.head = None
        self.last = None
        self.count = 0

    def add(self,Value):
        '''
        Purpose: Add a node to the FRONT of the CircularlyLinkedList
        Param: Value
        Return: None
        '''
        if self.head == None:
            newNode=Node(Value)
            self.head=newNode
            self.last = newNode
            self.head.next = self.last
            self.last.next = self.head
        else:
            newNode=Node(Value)
            newNode.next = self.head
            self.head = newNode
            self.last.next = self.head
        self.count = self.count + 1

    def is_empty(self):
        '''
        Purpose: Return a boolean value if the CircularlyLinkedList is empty or not
        Param: None
        Return: Boolean Value
        '''
        return self.head == None

    def size(self):
        '''
        Purpose: To return the size of the CircularlyLinkedList
        Param: None
        Return: The size of the CircularlyLinkedList
        '''
        # current = self.head
        # count = 0
        # while current is not None:
        #     count = count + 1
        #     current = current.next
        return self.count

    def __iter__(self):
        '''
        Purpose: To iterate over the CircularlyLinkedList properly (like a List)
        Param: None
        Return: None
        '''
        counter = 0
        size = self.size()
        current = self.head
        while current is not None and counter < size:
            yield current
            current = current.next
            counter = counter + 1

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
            self.last = newNode
            self.head.next = self.last
            newNode.next = self.head
        else:
            newNode = Node(Value)
            self.last.next = newNode
            self.last = newNode
            newNode.next = self.head
        self.count = self.count + 1

    def pop(self, pos = None):
        '''
        Purpose: To remove and return a node at the provided position.
        Param: pos
        Return: The node at the given position
        '''
        size= self.size()
        if size == 0:
            return None
        if pos == None:
            pos = size - 1
        if not isinstance(pos,int):
            return ('Invalid Input')
        if pos >= size or pos < 0:
            return ('Invalid Input')
        if pos == 0:
            if self.head == self.last:
                first = self.head
                self.head = None
                self.last = None
                self.count = self.count - 1
                return first
            else:
                current = self.head
                self.head = current.next
                self.last.next = self.head
                self.count = self.count - 1
                return current
        elif pos == size-1:
            previous = self.head
            current = self.head
            counter = 0
            while counter < pos:
                previous = current
                current = current.next
                counter += 1
            previous.next = self.head
            self.last = previous
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
        Purpose: To check if a given value is in the CircularlyLinkedList
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
        Purpose: To remove a value (node) from the CircularlyLinkedList (not an index)
        Param: Value
        Return: None
        '''
        previous= None
        NotHead = False
        if Value == self.head.data:
            current= self.head
        else:
            previous = self.head
            current = self.head.next
            while current != self.head:
                if current.data == Value:
                    break
                previous = current
                current = current.next
                NotHead = True
        if current is self.head and NotHead:
            raise ValueError (f'{Value} is not in List')
        if previous == None:
            if current.next == self.last:
                self.head = None
                self.last = None
                self.count = self.count - 1
            else:
                self.head = current.next
                self.last.next = self.head
                self.count = self.count - 1
        elif current == self.last:
            previous.next = self.head
            self.last = previous
            self.count = self.count - 1
        else:
            # if current.next == self.last:
            #     temp = current.next
            #     temp.next = self.head
            #     previous.next = temp
            #     self.last = temp
            # else:
            #     previous.next = current.next
            previous.next = current.next
            self.count = self.count - 1