class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right

    def __str__(self):
        return str(self.data)


class BST:

    def __init__(self, root=None):
        self.root = root

    def addI(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            parent_p = None
            p = self.root
            while p is not None:
                parent_p = p
                p = p.left if data < p.data else p.right

            if data < parent_p.data:
                parent_p.left = Node(data)
            else:
                parent_p.right = Node(data)

    def add(self, data):
        self.root = BST._add(self.root, data)

    @staticmethod
    def _add(root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left, data)
            else:
                root.right = BST._add(root.right, data)
            return root

    def inOrder(self):
        BST._inOrder(self.root)
        print()

    @staticmethod
    def _inOrder(root):
        if root is not None:
            BST._inOrder(root.left)
            print(root.data, end=' ')
            BST._inOrder(root.right)

    def printSideway(self):
        BST._printSideway(self.root, 0)
        print()

    @staticmethod
    def _printSideway(root, level):
        if root is not None:
            BST._printSideway(root.right, level+1)
            print("   "*level, end="")
            print(root.data)
            BST._printSideway(root.left, level+1)

    def preOrder(self):
        BST._preOrder(self.root)
        print()

    @staticmethod
    def _preOrder(root):
        if root is not None:
            print(root.data, end=" ")
            BST._preOrder(root.left)
            BST._preOrder(root.right)

    def postOrder(self):
        BST._postOrder(self.root)
        print()

    @staticmethod
    def _postOrder(root):
        if root is not None:
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root.data, end=" ")

    def search(self, data):
        return BST._search(self.root, data)

    @staticmethod
    def _search(root, data):
        if root is None or root.data == data:
            return root
        if data < root.data:
            return BST._search(root.left, data)
        else:
            return BST._search(root.right, data)

    def path(self, data):
        BST._path(self.root, data)

    @staticmethod
    def _path(root, data):
        if root is None or root.data == data:
            print(root.data)
            return
        if data < root.data:
            print(root.data, end="->")
            BST._path(root.left, data)
        else:
            print(root.data, end="->")
            BST._path(root.right, data)

    def delete(self, data):
        if self.root is None:
            return
        BST._delete(self.root, data)

    @staticmethod
    def minValueNode(node):
        current = node

        while(current.left is not None):
            current = current.left

        return current

    @staticmethod
    def _delete(root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = BST._delete(root.left, data)

        elif data > root.data :
            root.right = BST._delete(root.right, data)

        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = BST.minValueNode(root.right)

            root.data = temp.data

            root.right = BST._delete(root.right, temp.data)

    def height(self):
        return BST._height(self.root)

    @staticmethod
    def _height(root):
        if not root:
            return -1
        else:
            left = BST._height(root.left)
            right = BST._height(root.right)
            if left > right:
                return left+1
            else:
                return right+1

    def depth(self,data):
        return BST._depth(self.root,data)

    @staticmethod
    def _depth(root,data):
        if root is None or root.data == data:
            return 0
        if data < root.data:
            return 1+BST._depth(root.left, data)
        else:
            return 1+BST._depth(root.right, data)


t = BST()
t.addI(10)
t.addI(5)
t.addI(2)
t.addI(3)
t.addI(23)
t.addI(32)
t.delete(10)
t.add(1)
t.add(4)
t.printSideway()
print(t.depth(1))
