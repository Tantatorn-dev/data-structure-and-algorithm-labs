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


def precedence(c):
    if c=='+' or c=='-':
        return 1
    elif c=='*' or c=='/':
        return 2
    elif c=='(' or c==')':
        return 0

def infix_to_postfix(text):
    postfix=""
    stack = Stack()

    for ch in text:
        if (ch in "123456789"):
            postfix += ch
        elif ch =='(':
            stack.push('(')
        elif ch==')':
            while((not stack.isEmpty()) and stack.peek() !='('):
                a=stack.pop()
                postfix += a
            if (not stack.isEmpty() and stack.peek() != '('):
                return -1
            else:
                stack.pop()
        else:
            while(not stack.isEmpty() and precedence(ch) <= precedence(stack.peek())):
                postfix += stack.pop()
            stack.push(ch)
        
    while not stack.isEmpty():
        postfix += (stack.pop())
    
    return postfix



  


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
