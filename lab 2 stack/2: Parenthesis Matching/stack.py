class Stack:

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[len(self.items)-1]
