def SelectionSort(arr):
    smallest = 0
    for i in range(len(arr)):
        smallest = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(SelectionSort([64, 25, 12, 22, 11]))
