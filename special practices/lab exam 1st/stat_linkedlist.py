class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        arr = []
        while current != None:
            arr.append(current.data)
            current = current.next
        return str(arr)

    def __len__(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        if self.head == None:
            self.head = self.Node(data)
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = self.Node(data)

    def remove(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                prev.next = current.next
                break
            prev = current
            current = current.next

    def add(self, data):
        if self.head == None:
            self.head = self.Node(data)

        # Special case for head at end
        elif self.head.data >= data:
            temp = self.head
            self.head = self.Node(data)
            self.head.next = temp 

        else:

            # Locate the node before the point of insertion
            current = self.head
            while(current.next != None and
                  current.next.data < data):
                current = current.next

            temp = current.next
            current.next = self.Node(data)
            current.next.next = temp

    def getMean(self):
        current = self.head
        res = 0
        while current != None:
            res += current.data
            current =current.next
        return res/len(self)
    
    def getMode(self):
        amount = {}
        current = self.head
        while current!=None:
            amount[current.data] = 0
            current = current.next

        current = self.head
        while current!=None:
            amount[current.data] += 1
            current = current.next

        res=[]
        max_count = 0
        for item in amount:
            if amount[item]>max_count:
                max_count = amount[item]
        
        for item in amount:
            if amount[item] == max_count:
                res.append(item)

        return res
    
    def getMedian(self):
        pass

ll = LinkedList()
ll.add(3)
ll.add(5)
ll.add(5)
ll.add(5)
ll.add(1)
ll.add(1)
ll.add(1)
ll.add(8)
ll.add(9)
print(ll)
print(ll)
print(ll.getMean())
print(ll.getMode())