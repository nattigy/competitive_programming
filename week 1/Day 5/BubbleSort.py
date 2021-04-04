def BubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(BubbleSort([12, 5, 111, 200, 1000, 10, 1, 2]))
