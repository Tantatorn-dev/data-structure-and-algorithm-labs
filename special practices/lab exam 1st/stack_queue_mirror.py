class Stack:

    def __init__(self, items=[]):
        self.items = items
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        temp = self.items.pop()
        self.items.append(temp)
        return temp
    
    def size(self):
        return len(self.items)

class Queue:

    def __init__(self, items=[]):
        self.items = items
    
    def __str__(self):
        return str(self.items)

    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def mirror(q):
    stack =Stack()

    size = q.size()
    i=0
    while i<size:
        temp = q.dequeue()
        stack.push(temp)
        q.enqueue(temp)
        i+=1 

    size = stack.size()
    i=0
    while i<size:
        q.enqueue(stack.pop())
        i+=1

    return q

myQ = Queue([1,2,3,4,5])
myQ = mirror(myQ)
print(myQ)