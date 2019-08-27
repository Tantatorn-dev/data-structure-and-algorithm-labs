import queue as q

myQueue = q.Queue()

name = "Tantatorn"
for c in "Tantatorn":
    myQueue.enqueue(c)

print(myQueue.items)

print(myQueue.dequeue())
print(myQueue.items)