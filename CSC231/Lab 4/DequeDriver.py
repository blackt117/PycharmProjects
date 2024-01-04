from Deque import *

deque = Deque()

print('Deque is empty? Should be True:', deque.is_empty())

# These lines add some people to the rear of the deque
deque.add_rear('Horatio')
deque.add_rear('Inez')
deque.add_rear('Jessica')
print(deque)
print('\nRemoving from the end of the deque. Should be Jessica:', deque.remove_rear())

# Add someone to the front of the deque
deque.add_front('ReallyImportantPerson')
print(deque)
print('\nRemoving from the front of the deque. Should be ReallyImportantPerson:', deque.remove_front())


print('\nDeque is empty? Should be False:', deque.is_empty())
print('Deque size. Should be 2:', deque.size())

print('\nRemoving from the front of deque. Should be Horatio:', deque.remove_front())
print('Removing from the front of deque. Should be Inez:', deque.remove_front())
print('Removing from the front of deque. Should be None:', deque.remove_front()) #deque is empty, therefore remove_front does
#not get activated, thus nothing is returned
print('Removing from the end of the deque. Should be None:', deque.remove_rear()) #deque is empty, therefore remove_rear does
#not get activated, thus nothing is returned

print('\nDeque size. Should be 0:', deque.size())
print('Deque is empty? Should be True:', deque.is_empty())

d = Deque()
d.add_front('Alice')
d.add_front('Bob')
d.add_rear('Charles')
d.add_rear('Daniella')
d.add_front('Erin')
d.remove_rear()
d.remove_front()
d.add_rear('Fran')
print(d)