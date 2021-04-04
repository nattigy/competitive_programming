def FindMedian(arr):
    n = len(arr)

    maxx = 0
    for i in arr:
        if i > maxx:
            maxx = i

    newArr = [0] * (maxx + 1)
    res = []

    for i in arr:
        newArr[i] += 1

    for i in range(len(newArr)):
        if newArr[i] > 0:
            for j in range(newArr[i]):
                res.append(i)
                if len(res) == (n + 1) / 2:
                    return i


print(FindMedian([5]))
