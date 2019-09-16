import linkedlist
import node

myList = linkedlist.List(1)

for i in range(2, 11):
    myList.append(i)
print(myList)

myList.riffle(60)
print(myList)

myList.deRiffle(60)
print(myList)
