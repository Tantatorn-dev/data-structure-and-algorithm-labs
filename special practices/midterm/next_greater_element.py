def NGE(arr):
    i = 0
    length = len(arr)
    print("Element        NGE")
    while i < length:
        j = i+1
        stack = []

        while j < length:

            if arr[j] > arr[i]:
                stack.append(arr[j])
                break

            j += 1

        print(arr[i],end="   -->   ")

        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

        i += 1


NGE([4, 5, 2, 25])
NGE([13, 7, 6, 12])