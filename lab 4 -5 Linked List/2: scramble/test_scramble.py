import linkedlist
import node

myList = linkedlist.List(1)

for i in range(2, 31):
    myList.append(i)
print(myList)

myList.bottomUp(10)
print(myList)

myList.deBottomUp(10)
print(myList)

myList.riffle(10)
print(myList)

myList.deRiffle(10)
print(myList)


