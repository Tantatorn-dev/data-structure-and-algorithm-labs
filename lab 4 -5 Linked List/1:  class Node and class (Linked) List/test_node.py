import node

node1 = node.Node("cat")
node2 = node.Node("dog")
node3 = node.Node("motorola")
node4 = node.Node("iPhone")

node1.setNext(node2)
node2.setNext(node3)
node3.setNext(node4)

print(node1)
print(node1.next)
