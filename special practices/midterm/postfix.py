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
        return self.items == []

    def peek(self):
        return self.items[-1]


def evalPostfix(expression: str) -> int:

    stack = Stack()

    for ch in expression:

        if ch == "+" or ch == "-" or ch == "*" or ch == "/":
            a = int(stack.pop())
            b = int(stack.pop())
            if ch == "+":
                stack.push(a+b)
            elif ch == "-":
                stack.push(a-b)
            elif ch == "*":
                stack.push(a*b)
            elif ch == "/":
                stack.push(a/b)
        else:
            stack.push(ch)
    return int(stack.items.pop())

print(evalPostfix("138*+"))
