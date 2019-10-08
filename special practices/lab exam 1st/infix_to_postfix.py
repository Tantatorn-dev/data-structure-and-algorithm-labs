class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        text = ""
        temp = self.items[::-1]
        for i in self.items:
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

def split(text):
    return [c for c in text]


def infix_to_postfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = split(infixexpr)

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower() or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return "".join(postfixList)

def evalPostfix(expr):
    stack = Stack()
    for c in expr:
        if (c in "+-*/"):
            a = stack.pop()
            b = stack.pop()
            if c=='+':
                stack.push(int(a)+int(b))
            elif c=='-':
                stack.push(int(a)-int(b))
            elif c=='*':
                stack.push(int(a)*int(b))
            elif c=='/':
                stack.push(int(a)/int(b))
        else:
            stack.push(c)
    return stack.pop()

def postfix_to_infix(expr):
    stack= Stack()
    for c in expr:
        if (c in "+-*/"):
            a = stack.pop()
            b = stack.pop()
            stack.push('('+b+c+a+')')                     
        else:
            stack.push(c)
    return stack.pop()

def findNumOperation(text):
    count = 0
    for c in text:
        if c == '-' or c == '+' or c == '*' or c == '/' or c == '^':
            count += 1
    return count


def findNumOperand(text):
    count = 0
    for c in text:
        if not(c == '-' or c == '+' or c == '*' or c == '/' or c == '(' or c == ')'):
            count += 1
    return count


print("Enter infix expression : ", end="")
inExpression = input()
print("Result posfix expression : ", end="")
print(infix_to_postfix(inExpression))
print("Number of operation : ", end="")
print(findNumOperation(inExpression))
print("Number of operand : ", end="")
print(findNumOperand(inExpression))
print(postfix_to_infix(infix_to_postfix(inExpression)))