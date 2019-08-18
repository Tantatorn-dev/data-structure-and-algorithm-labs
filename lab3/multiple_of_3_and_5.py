def multiple_of_3_and_5(n):
    sum = 0
    for i in range(1,n+1):
        if i%3 == 0 or i%5 == 0:
            sum+=i
    return sum
