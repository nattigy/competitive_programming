import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i*(-1) for i in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)
            if x < y:
                heappush(stones, x - y)
        return 0 if not stones else -stones[0]
