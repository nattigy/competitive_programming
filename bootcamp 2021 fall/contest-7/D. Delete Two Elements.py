from collections import defaultdict


def deleteTwoElements(nums):
    mean = sum(nums) / len(nums)
    # sum of the two numbers
    k = 2 * mean
    compliments = defaultdict(int)
    count = 0
    for i in nums:
        if i in compliments:
            count += compliments[i]
        compliments[k - i] = compliments.get(k - i, 0) + 1
    return count


tests = int(input())
ans = []
for _ in range(tests):
    length = int(input())
    elements = input().rstrip().split(" ")
    ans.append(deleteTwoElements([int(i) for i in elements]))
for a in ans:
    print(a)
