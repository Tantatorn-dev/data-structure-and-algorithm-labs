def fac(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    return n*fac(n-1)


def sum1ToN(n):
    if n == 1:
        return 1
    return n+sum1ToN(n-1)


def printNTo1(n):
    print(n)
    if n == 1:
        return
    printNTo1(n-1)


def print1ToN(n):
    if n == 1:
        return
    print1ToN(n-1)
    print(n)


def fib(n):
    if n == 2 or n == 1:
        return 1
    return fib(n-1)+fib(n-2)


def binarySearch(lo, hi, x, l):
    pass

# not enough! must push myself harder


"""
print(fac(3))
print(sum1ToN(10))
print()
printNTo1(5)
print1ToN(5)
print("fibonacci: ",end="")
print(fib(12))
"""

myList = []


def appendNajaB(myList: list, n: int):
    if n == 1:
        myList.append(n)
        return
    else:
        myList.append(n)
        appendNajaB(myList, n-1)


def appendNaja(myList: list, n: int):
    if n == 1:
        myList.append(n)
        return
    else:
        appendNaja(myList, n-1)
        myList.append(n)


def printListForward(myList, n):
    if n != 0:
        printListForward(myList, n-1)
        print(myList[n-1])
    else:
        return


def printListBackward(myList, n):
    print(myList[n-1])
    if n == 1:
        return
    printListBackward(myList, n-1)


"""
appendNaja(myList,10)
printListBackward(myList,len(myList))
"""


class Node():
    def __init__(self, data, next=None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next


head = Node(1)


def append(head: Node, newData):
    current = head
    while current.next != None:
        current = current.next
    current.next = Node(newData)


def printList(head: Node):
    if head == None:
        return
    print(head.data)
    printList(head.next)


"""
for i in range(10):
    append(head,i)

printList(head)
"""

def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 
    if n == 1: 
        print ("Move disk 1 from rod",from_rod,"to rod",to_rod )
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print ("Move disk",n,"from rod",from_rod,"to rod",to_rod )
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
    