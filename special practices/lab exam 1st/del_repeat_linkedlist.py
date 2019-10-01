class Node:

    def __init__(self, data,next=None):
        self.data=data
        self.next=next
    
def createList(headData):
    head = Node(headData)
    return head

def append(head,data):
    current = head
    while current.next != None:
        current = current.next
    current.next = Node(data)

def printList(head):
    current = head
    while current != None:
        print(current.data,end=" ")
        current = current.next
    print()

def delRepeat(head):
    current = head
    while current != None:
        temp = current
        inner_current = current.next
        while inner_current != None:
            if current.data == inner_current.data:
                temp.next=inner_current.next    
                inner_current = inner_current.next
                continue
            temp = temp.next
            inner_current = inner_current.next
        current = current.next

myList = createList(1)

arr = [1,2,2,3,4,4,4,5,5,3,1,1,20]

for item in arr:
    append(myList,item)

printList(myList)
delRepeat(myList)
printList(myList)

# Work harder