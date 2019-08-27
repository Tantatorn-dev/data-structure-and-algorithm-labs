import stack

myStack = stack.Stack()

for char in "station":
    myStack.push(char)

print(myStack.items)
print(myStack.size())
print(myStack.isEmpty())
print(myStack.peek())

for i in range(myStack.size()):
    myStack.pop()

print(myStack.isEmpty())