class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "%s" % self.data


class CircleLinkedlist:

    def __init__(self, head=None):
        self.head = Node(head)

    def append(self, data):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(data)

    def circling(self):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = self.head
            
    def printAll(self):
        current = self.head
        while current != None:
            print(current)
            current = current.next

    def executeJosephus(self, m):
        current1 = self.head
        current2 = self.head
        while id(current1.next) != id(current1):
            count = 1
            while count != m:
                current2 = current1
                current1 = current1.next
                count += 1
            
            current2.next = current1.next
            current1 = current2.next
        current1.next = None


elements = CircleLinkedlist(1)

for i in range(2, 5):
    elements.append(i)

elements.circling()
elements.executeJosephus(2)

elements.printAll()

"""
print("Input: ", end="")

circleLength = input(" n= ")
countToChooseNext = input(" m= ")
"""