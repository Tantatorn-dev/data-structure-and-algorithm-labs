arr = [2,1,3,4,5,6,9,8]

def bubble_sort(arr:list):

    length = len(arr)


    for i in range(length):

        for j in range(0,length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def recursive_bubble_sort(arr:list,index=0):
    if index == len(arr)-1:
            return
    
    for i in range(len(arr)-index-1):
        if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]

    recursive_bubble_sort(arr,i+1)


recursive_bubble_sort(arr)
print(arr)