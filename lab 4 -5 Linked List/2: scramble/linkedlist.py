import node

# this is LinkedList naja


class List:

    def __init__(self, head=None):
        if head == None:
            self.head = None
        else:
            self.head = node.Node(head)

    def addHead(self, head):
        self.head = node.Node(head)

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node.Node(data)

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        list_str = []
        current = self.head
        while current != None:
            list_str.append(current.data)
            current = current.next
        return list_str.__str__()

    def isIn(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                return True
            current = current.next
        return False

    def before(self, data):
        current = self.head
        while current != None:
            if current.next.data == data:
                return current
            current = current.next
        return None

    def remove(self, data):
        current = self.head
        while current != None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def removeTail(self):
        current = self.head
        while current != None:
            if current.next.next == None:
                current.next = None
                return
            current = current.next

    def removeHead(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next

    def insert(self, beforeData, data):
        current = self.head
        while current != None:
            if current.data == beforeData:
                temp = current.next
                current.next = node.Node(data)
                current.next.next = temp
                return
            current = current.next

    def insertByIndex(self, index, node):
        current = self.head
        for i in range(index):
            current = current.next
        temp = current.next
        current.next = node
        current.next.next = temp

    def bottomUp(self, percent):
        size = self.size()
        amount = int(size * percent/100)
        temp = self.head

        for i in range(0, amount):
            self.head = self.head.next

        current = self.head

        for i in range(1, size-amount):
            current = current.next

        current.next = temp
        for i in range(1, amount):
            temp = temp.next
        temp.next = None

    def riffle(self, percent):
        size = self.size()
        if percent <50:
            percent = 100 -percent
        amount = int(size * percent/100)

        current = self.head
        for i in range(1, amount):
            current = current.next
        
        # cut the list
        newHead = current.next
        current.next =None

        current = self.head
        count = size - amount
        while current != None:
            if count > 0 :
                temp1 = newHead.next
                newHead.next = None
                temp2 =current.next
                current.next = newHead
                current.next.next = temp2
                current =current.next.next
                newHead = temp1
                count -= 1
            else:
                current = current.next
