arr = [2,1,3,4,5,6,9,8]

def bubble_sort(arr:list):

    length = len(arr)


    for i in range(length):

        for j in range(0,length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort(arr)
print(arr)