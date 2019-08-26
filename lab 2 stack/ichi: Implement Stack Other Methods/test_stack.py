import stack

myStack = stack.Stack()

for char in "Tantatorn":
    myStack.push(char)

print(myStack.items)
print(myStack.size())
print(myStack.isEmpty())
print(myStack.peek())

for i in range(9):
    myStack.pop()

print(myStack.isEmpty())