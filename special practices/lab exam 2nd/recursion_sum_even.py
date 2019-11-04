# return sum of "even" number in the list

l = [1,2,3,4,5,6,8,10]

def sumEven(l,index=0):
    if index == len(l):
        return 0
    if l[index] % 2 ==0:
        return l[index]+sumEven(l,index+1)
    else:
        return sumEven(l,index+1)

print(sumEven(l))