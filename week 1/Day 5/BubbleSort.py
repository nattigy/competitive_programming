def BubbleSort(arr):
    notSorted = True
    while notSorted:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                notSorted = True
            else:
                notSorted = False

    return arr


print(BubbleSort([10, 5, 6, 7, 9]))
