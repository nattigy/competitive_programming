def TwoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []


print(TwoSum([2, 7, 11, 15], 9))
