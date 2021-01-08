def FindMedian(arr):
    smallest = 0
    n = len(arr)
    for i in range(n):
        smallest = arr[i]
        for j in range(i + 1, n):
            if arr[j] < smallest:
                smallest = arr[j]
                arr[i], arr[j] = arr[j], arr[i]
        if i == (n - 1) / 2:
            return arr[i]


print(FindMedian([0, 1, 2, 4, 6, 5, 3]))
