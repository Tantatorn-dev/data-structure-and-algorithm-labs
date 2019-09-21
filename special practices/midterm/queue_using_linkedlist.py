class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "%s" % self.data

class Queue:

    def __init__(self, data=None):
        self.head = Node(data)
    
    def enqueue(self,data):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(data)
    
    def dequeue(self):
        temp = self.head.data
        self.head = self.head.next
        return temp
    
    def printAll(self):
        current = self.head
        while current != None:
            print(current.data,end=" ")
            current = current.next
        print()

myQ = Queue("motorola")

myQ.enqueue("iPhone")
myQ.enqueue("Blackberry")
myQ.printAll()


print(myQ.dequeue())
myQ.printAll()