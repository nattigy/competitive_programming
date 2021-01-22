def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    equal = []
    pivot = arr[0]
    for i in range(len(arr)):
        if arr[i] == pivot:
            equal.append(arr[i])
        elif arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    l = quickSort(left)
    r = quickSort(right)
    print(*l,*equal,*r)
    return l + equal + r

quickSort([9 ,8 ,6 ,7 ,3, 5 ,4 ,1 ,2])