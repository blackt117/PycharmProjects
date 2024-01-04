from Stack import *

stack = Stack()

print('Stack is empty? Should be True:', stack.is_empty())

# These lines push some numbers onto the stack
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)

print('\nStack is empty? Should be False:', stack.is_empty())
print('Stack size. Should be 3:', stack.size())
print('Peeking at the top item, but not popping it! Should be 3:', stack.peek())

print('\nPopping the top item:', stack.pop())
print('Popping the top item:', stack.pop())
print('Popping the top item:', stack.pop())
print('Popping the top item:', stack.pop()) #return None type because nothing is returned/no action happens when the len of stack is zero
print('\nStack is empty? should be True:', stack.is_empty())
print('\nStack size. Should be 0:', stack.size())

# just for fun
print()
print(stack.Bin(198))
print(stack.Bin(1000))
print(stack.Bin(2047))
stack.BaseChange(5551)

q=Stack()
q.push(1)
q.pop()
q.push(2)
q.push(3)
q.pop()
q.push(4)
q.pop()
q.pop()
q.push(5)
print(q)