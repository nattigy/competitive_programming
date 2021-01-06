def InsertionSort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                for k in range(j - 1, -1, -1):
                    if arr[k] > arr[k + 1]:
                        arr[k], arr[k + 1] = arr[k + 1], arr[k]

    return arr


print(InsertionSort([11, 12, 13, 5, 6]))