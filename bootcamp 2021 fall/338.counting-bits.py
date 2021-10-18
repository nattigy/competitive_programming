#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for i in range(n+1)]
        for i in range(n+1):
            c = i
            while c != 0:
                r = c%2
                c = c//2
                if r == 1:
                    res[i] = res[i]+1
        return res
# @lc code=end

