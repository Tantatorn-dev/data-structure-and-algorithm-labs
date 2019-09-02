import linkedlist

myList = linkedlist.List("Zaku I")

myList.append("Zaku 2")
myList.append("Gundam")

print(myList)
print(myList.size())
print(myList.isIn("Gundam"))
print(myList.before("Gundam"))

myList.insert("Zaku I","GM 2")
print(myList)

myList.removeHead()
myList.removeTail()
print(myList)

