def longJumps(nums):
    dp = [0 for i in nums]
    length = len(nums)
    for i in range(length - 1, -1, -1):
        add = 0
        index = nums[i] + i
        if index < length:
            add += dp[index]
        dp[i] = nums[i] + add

    return max(dp)

test = int(input())
ans = []
for _ in range(test):
    length = int(input())
    nums = input().strip().split(" ")
    arr = []
    for n in nums:
        arr.append(int(n))
    ans.append(longJumps(arr))
for a in ans:
    print(a)
