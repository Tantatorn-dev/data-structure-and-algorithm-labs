import stack

myStr = "[(1+3)+{2-1}]"
myStack = stack.Stack()
err = False

for char in myStr:
    if char == '(' or char == '{' or char == '[':
        myStack.push(char)
    elif char == ')' or char == '}' or char == ']':
        if myStack.isEmpty():
            err = True
        else:
            op = myStack.pop()
            if not ((op == '(' and char == ')') or (op == '[' and char == ']') or (op == '{' and char == '}')):
                err = True

if err:
    print("MISMATCH")
else:
    if myStack == []:
        print("MISMATCH open paren. exceed")
    else:
        print("MATCH")
