import linkedlist 

myList = linkedlist.List(1)

for i in range(2,11):
    myList.append(i)
print(myList)

myList.bottomUp(30)
print(myList)

myList.riffle(60)
print(myList)