#
# @lc app=leetcode id=1901 lang=python3
#
# [1901] Find a Peak Element II
#

# @lc code=start
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                cond = True
                d = [mat[i][j-1] if j-1 >= 0 else -1,
                     mat[i-1][j] if i-1 >= 0 else -1,
                     mat[i][j+1] if j+1 < len(mat[0]) else -1,
                     mat[i+1][j] if i+1 < len(mat) else -1]
                for k in range(len(d)):
                    if mat[i][j] < d[k]:
                        cond = False
                        continue
                if cond:
                    return [i,j]
# @lc code=end

