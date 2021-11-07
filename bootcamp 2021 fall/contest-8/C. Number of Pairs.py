from math import comb
def numberOfPairs(nums, left, right):
    nums.sort()
    length = len(nums)
    i = 0
    j = length - 1
    count = 0
    while i < j and j >= 0 and i < length:
        if nums[i] + nums[j] < left:
            count += j - i
            i += 1
        else:
            j -= 1
    i = 0
    j = length - 1
    while i < j and i < length and j >= 0:
        if nums[i] + nums[j] > right:
            count += j - i
            j -= 1
        else:
            i += 1
    return comb(length, 2) - count

tests = int(input())
ans = []
for _ in range(tests):
    [_, left, right] = input().split(" ")
    third = input().split(" ")
    arr = []
    for t in third:
        arr.append(int(t))
    ans.append(numberOfPairs(arr, int(left), int(right)))
for a in ans:
    print(a)
