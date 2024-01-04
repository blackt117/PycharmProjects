from Queue import *

queue = Queue()

print('Queue is empty? Should be True:', queue.is_empty())

# These lines add some people to the end of the queue
queue.enqueue('Alice')
queue.enqueue('Bob')
queue.enqueue('Camille')
print(queue)
print('\nQueue is empty? Should be False:', queue.is_empty())
print('Queue size. Should be 3:', queue.size())

# These lines remove people from the front of the queue
print('\nDequeueing the front of the queue. Sbould be Alice:', queue.dequeue())
print('Dequeueing the front of the queue. Should be Bob:', queue.dequeue())
print('Dequeueing the front of the queue. Should be Camille:', queue.dequeue())
print('Dequeueing the front of the queue. Should be None:', queue.dequeue()) #the list/queue is empty so pop/dequeue returns nothing
print('\nQueue is empty? Should be True:', queue.is_empty())
print('Queue size. Should be 0:', queue.size())

q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.dequeue()
print(q)
