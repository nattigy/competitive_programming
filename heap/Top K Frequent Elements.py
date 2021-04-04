import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heapify(nums)
        while nums:
            pop = heappop(nums)
            freq[pop] = freq.get(pop, 0) + 1
        res = []
        for i in range(k):
            mx = 0
            val = 0
            for key in freq:
                if freq[key] > mx:
                    mx = freq[key]
                    val = key
            res.append(val)
            freq[val] = 0
        return res
