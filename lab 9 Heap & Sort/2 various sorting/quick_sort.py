def partition(arr,l,h):
    pivot = arr[h]

    i = l -1
    for j in range(l,h):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1

def quick_sort(arr,l,h):
    if l < h:
        pi = partition(arr,l,h)

        quick_sort(arr,l,pi-1)
        quick_sort(arr,pi+1,h)

arr = [1,3,5,6,2,12,10,8,9]
quick_sort(arr,0,8)
print(arr)