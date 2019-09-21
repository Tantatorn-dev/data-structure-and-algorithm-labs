class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "output : %s"%self.data

class LinkedList:

    def __init__(self, head=None):
        if head == None:
            self.head = None
        else:
            self.head = Node(head)

    def append(self, data):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(data)

    def __str__(self):
        list_str = []
        current = self.head
        while current != None:
            list_str.append(current.data)
            current = current.next
        return list_str.__str__()

    def findMid(self):
        ptrA = self.head
        ptrB = self.head

        i = 0
        while ptrA.next != None:
            if i % 2 == 0:
                ptrB = ptrB.next
            ptrA = ptrA.next
            i+=1
        
        return ptrB
        

elements = LinkedList(1)

for i in range(2,6):
    elements.append(i)

print(elements)

print(elements.findMid().data)
