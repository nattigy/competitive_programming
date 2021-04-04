import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        arr = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(arr, (i + j, [i,j]))
        i = 0
        res = []
        while i < k and arr:
            res.append(heapq.heappop(arr)[1])
            i += 1
        return res
        
