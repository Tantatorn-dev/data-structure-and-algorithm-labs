class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        text = ""
        temp = self.items[::-1]
        for i in items:
            text += str(i)
        return text

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, i):
        return self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        temp = self.items.pop()
        self.items.append(temp)
        return temp

def precedence(ch):
    if ch == '+' or ch == '-':
        return 1
    elif ch == '*' or ch == '/':
        return 2
    elif ch == '^':
        return 3

def notGreater(stack, ch):
    try:
        a = precedence(ch)
        b = precedence(stack.peek())
        return True if a <= b else False
    except KeyError:
        return False


def infix_to_postfix(text):
    outText = ""
    myStack = Stack()
    for ch in text:
        if not(ch == '+' or ch == '-' or ch == '*' or ch == '/'):
            outText += ch
        elif ch == '(':
            myStack.push(ch)
        elif ch == ')':
            while ((not myStack.isEmpty()) and myStack.peek() != '('):
                a = myStack.pop()
                outText += a
            if ((not myStack.isEmpty()) and myStack.peek() != '('):
                return -1
            else:
                myStack.pop()

        else:
            while(not myStack.isEmpty() and notGreater(myStack,ch)):
                outText += myStack.pop()
            myStack.push(ch)
    
    while not myStack.isEmpty():
        outText += myStack.pop()
    
    return outText

def findNumOperation(text):
    count = 0
    for c in text:
        if c == '-' or c == '+' or c == '*' or c == '/' or c=='^':
            count += 1
    return count


def findNumOperand(text):
    count = 0
    for c in text:
        if not(c == '-' or c == '+' or c == '*' or c == '/' or c== '(' or c==')'):
            count += 1
    return count


print("Enter infix expression : ", end="")
inExpression = input()
print("Result posfix expression : ",end="")
print(infix_to_postfix(inExpression))
print("Number of operation : ",end="")
print(findNumOperation(inExpression))
print("Number of operand : ",end="")
print(findNumOperand(inExpression))
