class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

root = Node(27)

def add(root: Node, data):
    if root == None:
        return Node(data)
    else:
        if data < root.data:
            root.left = add(root.left, data)
        else:
            root.right = add(root.right, data)
        return root

add(root,14)
add(root, 35)
add(root,10)
add(root,31)
add(root,42)
add(root,19)

def printSideway(root: Node, level: int):
    if root is None:
        return

    printSideway(root.right, level+1)
    print('   '*level, root.data)
    printSideway(root.left, level+1)

def search(root:Node, data):
    if root.data == data:
        return root
    else:
        if data<root.data:
            return search(root.left,data)
        else:
            return search(root.right,data)

def inOrder(root:Node):
    if root == None:
        return 
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)

def preOrder(root:Node):
    if root == None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root:Node):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")

def minValueNode(root):
    if root.left is None:
        return root
    return minValueNode(root.left)

def delete(root,data):

    if root == None:
        return root
    
    if data < root.data:
        root.left= delete(root.left,data)
    elif data > root.data:
        root.right=delete(root.right,data)
    else:
        if root.right == None:
            return root.left
        elif root.left == None:
            return root.right
        
        temp = root.right
        min_val = temp.data
        while temp.left != None:
            temp = temp.left
            min_val = temp.data
        
        root.data = min_val

        root.right = delete(root.right,root.data)

    return root
        


delete(root,27)
printSideway(root, 0)

"""
print(search(root,19))
"""

print()