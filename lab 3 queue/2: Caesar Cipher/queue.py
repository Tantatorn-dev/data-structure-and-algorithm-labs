class Queue:

    def __init__(self, list=None):
        if list == None:
            self.items=[]
        else:
            self.items=list
    
    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)