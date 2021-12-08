import heapq

def absentRemainder(n, nums):
    min_heap = nums[:]
    heapq.heapify(min_heap)
    max_heap = [-1*i for i in nums]
    heapq.heapify(max_heap)
    i = 0
    ans = []
    while i < n//2:
        maxx = heapq.heappop(max_heap)*-1
        minn = heapq.heappop(min_heap)
        if maxx != minn:
            ans.append([maxx, minn])
        i += 1
    return ans

tests = int(input())
ans = []
for _ in range(tests):
    n = int(input())
    nums = list(map(int, input().split()))
    ans.append(absentRemainder(n, nums))
    
for a in ans:
    for x in a:
        print(*x)