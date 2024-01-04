#################################
#
# Use this file to test your Unordered List implementations. In a few places, it initializes names to either a new
# LinkedList or new DoublyLinkedList. You will need to comment/uncomment the lines appropriate to the data structure
# that you want to test. You will also need to comment/uncomment the appropriate import statement at the top.
#
# This file assumes that your LinkedList class is in a file called LinkedList.py, and that your
# DoublyLinkedList class is in DoublyLinkedList.py.
#
# You will probably want to comment out some of the test code as you build up your classes so that you can test them
# incrementally. Your Unordered List methods are tested in the same order that they appear in the Lab 04 description
#################################

from LinkedList import *
#from DoublyLinkedList import *

names = LinkedList()
#names = DoublyLinkedList()

print('List is empty? Should be True:', names.is_empty())
print('List size() should be 0:', names.size())

names.add('Alice')
print('Added Alice to the list. Size should be 1:', names.size())
print('List is empty? Should be False:', names.is_empty())

names.add('Bob')
names.add('Charlie')
print('Added Bob and Charlie. Size should be 3:', names.size())
print('Order should be Charlie, Bob, Alice')
for x in names:
    print(x)


print('\nClearing the list')
names = LinkedList()
#names = DoublyLinkedList()
names.append('Harry')
print('Appended Harry to a new, empty list. Size should be 1:', names.size())

names.append('Hermione')
names.append('Ron')
print('Appended Hermione and Ron to the list. Order should be Harry, Hermione, Ron')
for x in names:
    print(x)

print('calling pop(). Should return Ron: {}, and the size should be 2: {}'.format(names.pop(), names.size()))
print('calling pop(). Should return Hermione: {}, and the size should be 1: {}'.format(names.pop(), names.size()))
print('calling pop(). Should return Harry: {}, and the size should be 0: {}'.format(names.pop(), names.size()))

print('Appending some characters back to the list: McGonagall, Harry, Hermione, Ron, Snape')
names.append('McGonagall')
names.append('Harry')
names.append('Hermione')
names.append('Ron')
names.append('Snape')
print(names.size())

print('calling pop(4). Should return Snape: {}, and the size should be 4: {}'.format(names.pop(4), names.size()))
print('calling pop(0). Should return McGonagall: {}, and the size should be 3: {}'.format(names.pop(0), names.size()))
print('calling pop(1). Should return Hermione: {}, and the size should be 2: {}'.format(names.pop(1), names.size()))
print('List should now have Harry and Ron in that order.')
for x in names:
    print(x)

print('Searching for Harry. Should be True:', names.search('Harry'))
print('Searching for Ron. Should be True:', names.search('Ron'))
print('Searching for Tyler. Should be False:', names.search('Tyler'))

print('\nClearing the list')
names = LinkedList()
#names = DoublyLinkedList()
print('Appending some characters back to the list: McGonagall, Harry, Hermione, Ron, Snape')
names.append('McGonagall')
names.append('Harry')
names.append('Hermione')
names.append('Ron')
names.append('Snape')
names.remove('Snape')
print('called remove(\'Snape\'). Does not return anything, but list size should be 4:', names.size())
names.remove('McGonagall')
print('called remove(\'McGonagall\'). Does not return anything, but list size should be 3:', names.size())
names.remove('Hermione')
print('called remove(\'Hermione\'). Does not return anything, but list size should be 2:', names.size())
print('List should now have Harry and Ron in that order.')
for x in names:
    print(x)
print('Popping at index 0 should return Harry: ', names.pop(0))
print('Popping at index 0 should return Ron: ', names.pop(0))
print('Popping at index 0 should return List is Empty: ', names.pop(0))


##Testing more cases
print()
numbers = LinkedList()
numbers.add(1)
numbers.append(2)
numbers.append(3)
numbers.add(0)
for x in numbers:
    print(x)
print('Size should be 4: ', numbers.size())
print('Popping at index 3, should return 3: ', numbers.pop(3))
print('Should return Invalid Input, not an int: ', numbers.pop('ty'))
print('Size should be 3: ', numbers.size())
print('Added 15')
numbers.add(15)
print('Popping at index 0 should return 15: ', numbers.pop(0))
print('Popping at the last index, should return 2: ', numbers.pop())
print('Popping at the last index, should return 1: ', numbers.pop())
print('Popping at the last index, should return 0: ', numbers.pop())
print('Popping at index 0, should return List is Empty: {} and size should be 0: {}'.format(numbers.pop(0),numbers.size()))
print()
numbers.add(11)
numbers.append(12)
numbers.append(13)
numbers.remove(13)
numbers.append(14)
for x in numbers:
    print(x)
numbers.remove(11)
numbers.remove(12)
numbers.remove(14)
# numbers.remove(11) This line of code will populate an error message




