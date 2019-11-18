def insertion_sort(arr:list):
    
    for i in range(1,len(arr)):

        key = arr[i]

        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [1,2,5,4,3,9,8]
insertion_sort(arr)
print(arr)