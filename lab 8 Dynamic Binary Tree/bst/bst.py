class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right

    def __str__(self):
        return str(self.data)

class BST:

    def __init__(self,root=None):
        self.root = root 

    def addI(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            parent_p = None
            p = self.root
            while p is not None:
                parent_p = p
                p = p.left if data<p.data else p.right
            
            if data < parent_p.data:
                parent_p.left = Node(data)
            else:
                parent_p.right = Node(data)
    
    def add(self,data):
        self.root = BST._add(self.root,data)

    @staticmethod
    def _add(root,data):
        if root is None:
            return Node(data)
        else:
            if data<root.data:
                root.left = BST._add(root.left,data)
            else:
                root.right = BST._add(root.right,data)
            return root
    
    def inOrder(self):
        BST._inOrder(self.root)
        print()

    @staticmethod
    def _inOrder(root):
        if root is not None:
            BST._inOrder(root.left)
            print(root.data,end=' ')
            BST._inOrder(root.right)
    
    def printSideway(self):
        BST._printSideway(self.root,0)
        print()
    
    @staticmethod
    def _printSideway(root,level):
        if root is not None:
            BST._printSideway(root.right,level+1)
            print(' '*level,root.data,sep='')
        BST._printSideway(root.left,level+1)
        
    
t = BST()
t.addI(10)
t.addI(5)
t.addI(2)
t.addI(3)
t.inOrder()