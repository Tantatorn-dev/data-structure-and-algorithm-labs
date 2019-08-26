class Stack:

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items=list
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()

