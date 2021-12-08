def hemoseShopping(nums, k):
    sorted = sorted(nums)
    for i in range(len(nums)):
        if nums[i] != sorted[i]:
            break
    if i == len(nums):
        return "YES"
    length = len(nums)
    i = length - k
    j = length - 1 - i
    if k >= length:
        return "NO"
    for x in range(i, j + 1):
        if nums[x] != sorted[x]:
            return "NO"
    return "YES"

tests = int(input())
ans = []
for _ in range(tests):
    n, m = list(map(int, input().split()))
    array = list(map(int, input().split()))
    ans.append(hemoseShopping(array, m))
print("\n".join(ans))