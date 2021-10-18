#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
from functools import cache
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        def climbStairs(self, n: int) -> int:
            return self.recursion(n-1)+self.recursion(n-2)
        @cache
        def recursion(self, n) -> int:
            # if n in  cache:
            #     return cache[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            # cache[n] = self.recursion(n-1, cache)+self.recursion(n-2, cache)
            return self.recursion(n-1)+self.recursion(n-2)
# @lc code=end

