def SalesByMatch(num, arr):
    res = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                res.append(arr[i])
                res.append(arr[j])
                del arr[j]
                break

    return len(res) // 2


print(SalesByMatch(9, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]))
