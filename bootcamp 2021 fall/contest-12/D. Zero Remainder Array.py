from collections import defaultdict

def zeroRemainderArray(k, nums):
    mods = sorted([k - (i % k) for i in nums])
    counts = defaultdict(int)
    max_val = 0
    max_key = 0
    for m in mods:
        if m != 0 and m % k != 0:
            counts[m] += 1
            if max_val <= counts[m]:
                max_val = counts[m]
                max_key = m
    if not counts:
        return 0
    return (max_val - 1) * k + max_key + 1

tests = int(input())
ans = []
for _ in range(tests):
    _, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ans.append(zeroRemainderArray(k, nums))
print(*ans, sep="\n")
    