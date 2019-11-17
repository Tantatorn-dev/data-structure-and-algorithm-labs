def selection_sort(arr:list):
    n = len(arr)
    l = []
    for i in range(n):
        minIndex = arr.index(min(arr))
        l.append(arr.pop(minIndex))
    for i in range(n):
        arr.append(l[i])

arr=[1,3,2,4,5,5,10,1,7]
selection_sort(arr)
print(arr)