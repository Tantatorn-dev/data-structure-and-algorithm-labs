
value = [60,100,120]
weight = [10,20,30]
capacity = 50

def knapsack(capacity,weight,val,n):
    if capacity==0 or n==0:
        return 0
    
    if weight[n-1] > capacity:
        return knapsack(capacity,weight,val,n-1)
    else:
        return max(val[n-1]+knapsack(capacity-weight[n-1],weight,val,n-1),
        knapsack(capacity,weight,val,n-1))

print(knapsack(capacity,weight,value,len(value)))