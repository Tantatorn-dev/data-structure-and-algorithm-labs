
def printSack(prices,maxI):
    global B
    for i in range(maxI+1):
        print(B[prices[i]],end=' ')
    print()

def pick(sack,i,moneyLeft,ig):
    global N
    global B
    if ig<N:
       price = B[ig]
       if moneyLeft < price:
           pick(sack, i, moneyLeft,ig+1)
       else:
            moneyLeft -= price
            sack[i] = ig
            if moneyLeft == 0:
                printSack(sack,i)
            else:
                pick(sack,i+1,moneyLeft,ig+1)
            pick(sack,i,moneyLeft+price,ig+1)

B=[20,10,5,5,3,2,20,10]
N=len(B)
mLeft = 20
sack = N*[-1]
i= 0
ig = 0
pick(sack,i,mLeft,ig)