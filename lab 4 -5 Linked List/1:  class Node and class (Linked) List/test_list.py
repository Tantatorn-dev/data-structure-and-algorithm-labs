import linkedlist

myList = linkedlist.List("Zaku I")

myList.append("Zaku II")
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

myList.addHead("Sazabi")
print(myList)
