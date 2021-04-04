import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        heapify(words)
        while words:
            pop = heappop(words)
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
