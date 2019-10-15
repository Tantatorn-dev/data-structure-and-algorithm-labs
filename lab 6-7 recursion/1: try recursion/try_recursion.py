def fac(n):
    if n==1:
        return 1
    if n==0:
        return 1
    return n*fac(n-1)

def sum1ToN(n):
    if n==1:
        return 1
    return n+sum1ToN(n-1)

def printNTo1(n):
    print(n)
    if n==1:
        return
    printNTo1(n-1)

def print1ToN(n):
    if n==1:
        return
    print1ToN(n-1)
    print(n)

def fib(n):
    if n==2 or n==1:
        return 1
    return fib(n-1)+fib(n-2)

def binarySearch(lo,hi,x,l):
    pass
# not enough! must push myself harder

print(fac(3))
print(sum1ToN(10))
print()
printNTo1(5)
print1ToN(5)
print("fibonacci: ",end="")
print(fib(12))