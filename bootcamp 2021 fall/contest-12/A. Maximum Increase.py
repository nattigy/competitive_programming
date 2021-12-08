def maximumIncrease(arr):
    i = 0
    j = 0
    length = 0
    while j < len(arr):
        if j >= 1:
            if arr[j] <= arr[j - 1]:
                i = j
        length = max(length, j - i + 1)
        j += 1
    return length

_, array = input(), list(map(int, input().split()))
print(maximumIncrease(array))