def makeProductEqualOne(nums):
    zeros = 0
    negatives = 0
    steps = 0
    for n in nums:
        if n < 0:
            negatives += 1
            steps += abs(n + 1)
        elif n == 0:
            zeros += 1
            steps += 1
        else:
            steps += n - 1
    
    if negatives % 2 != 0:
        if zeros == 0:
            steps += 2
    return steps

n = int(input())
nums = list(map(int, input().split()))
print(makeProductEqualOne(nums))