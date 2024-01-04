#################################
#
# Use this file to test your Unordered List implementations. In a few places, it initializes names to either a new
# LinkedList or new DoublyLinkedList. You will need to comment/uncomment the lines appropraite to the data structure
# that you want to test. You will also need to comment/uncomment the appropriate import statement at the top.
#
# This file assumes that your LinkedList class is in a file called LinkedList.py, and that your
# DoublyLinkedList class is in DoublyLinkedList.py.
#
# You will probably want to comment out some of the test code as you build up your classes so that you can test them
# incrementally. Your Unordered List methods are tested in the same order that they appear in the Lab 04 description
#################################





from DoublyLinkedList import *

names = DoublyLinkedList()

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

names = DoublyLinkedList()
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
print('Trying to pop a string data type, should return Invalid Input:',names.pop('tyler'))
print('calling pop(4). Should return Snape: {}, and the size should be 4: {}'.format(names.pop(4), names.size()))
print('calling pop(0). Should return McGonagall: {}, and the size should be 3: {}'.format(names.pop(0), names.size()))
print('calling pop(1). Should return Hermione: {}, and the size should be 2: {}'.format(names.pop(1), names.size()))
print('List should now have Harry and Ron in that order.')
for x in names:
    print(x)

print('Searching for Harry. Should be True:', names.search('Harry'))
print('Searching for Ron. Should be True:', names.search('Ron'))

print('\nClearing the list')

names = DoublyLinkedList()
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
print()

## Testing more cases
digits = DoublyLinkedList()
digits.add(0)
digits.append(1)
digits.add(2)
digits.append(3)
digits.add(10)
digits.append(11)
for x in digits:
    print(x)
print()
print('Size should be 6: ', digits.size())
print('Popping last index, should return 11: ', digits.pop())
print('Popping index 2, should return 0: ', digits.pop(2))
print('Popping index 4, should return Invalid Input due to the index being out of range: ', digits.pop(4))
print('Popping last index, should return 3: ', digits.pop())
digits.remove(10) #removing 10
# print(digits.remove(20)) This line of code will populate an error message.
print('Searching for value: 10, should return false: ', digits.search(10))
print('Size should be 2: ', digits.size())

#extra cases to nail home concepts for me
print('Digits in order:')
for x in digits:
    print(x)
print('Removed 1')
digits.remove(1)
print('Digits in order:')
for x in digits:
    print(x)
print()
print("Added 8 then 9 then removed 2")
digits.add(8)
digits.add(9)
digits.remove(2)
print('The tail should be 8:',digits.tail)
print('Appended 15 then 11')
digits.append(15)
digits.append(11)
print('The tail should be 11:', digits.tail)
print('The size should be 4:',digits.size())
print('Popping at index 2 should be 15:',digits.pop(2))
print('Popping at last index should be 11:', digits.pop())
print('Tail should be 8:', digits.tail)
print('Head should be 9:',digits.head)
print()
digits.append(17)
digits.remove(17)
print('Appended and removed 17')
print('Tail should be 8:',digits.tail)
print('Head should be 9:', digits.head)
digits.append(10)
print('Appended 10, popping at index 1 should give 8:',digits.pop(1))
for x in digits:
    print(x)
print()
print('Tail should be 10:',digits.tail)
print('Head should be 9:',digits.head)
digits.add(7)
digits.remove(7)
print('Added and removed 7')
print()
print('Head should be 9:',digits.head)
print('Head.previous should be None:',digits.head.previous)
print()
print('Removed 9 and 10')
digits.remove(9)
print('After removing 9, head should be 10:',digits.head)
print('Head.previous should be None:',digits.head.previous)
digits.remove(10)
# digits.remove(1)..... this line of code will also give back an error message
print()
print('Appended 7 then added 9 then 10 and removed 7')
digits.append(7)
digits.add(9)
digits.add(10)
digits.remove(7)
print('Tail.next should be None:',digits.tail.next)
print('Tail should be 9:',digits.tail)
print('Head should be 10:',digits.head)
print('Head.previous should be None:',digits.head.previous)
print('List is not empty, False:',digits.is_empty())
digits.pop()
digits.pop()
print('List is empty after popping twice, True:',digits.is_empty())







