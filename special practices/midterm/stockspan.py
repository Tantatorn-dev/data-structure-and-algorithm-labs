def calculateSpan(prices):
    i = 0
    stack = []
    while i<len(prices):
        count = 0
        j = i
        while j >= 0 :
            if prices[j] > prices[i]:
                break
            count += 1
            j-=1
        stack.append(count)
        i+=1       
    return stack

print(calculateSpan([100,80,60,70,60,75,85]))