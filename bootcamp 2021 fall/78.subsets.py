#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.recursion(nums)

    def recursion(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        result = self.recursion(nums[1:])
        result.extend([[nums[0]]+s for s in result])
        result.append([nums[0]])
        distinct = []
        visited = {}
        for l in result:
            if tuple(l) not in visited:
                distinct.append(l)
                visited[tuple(l)] = tuple(l)
        return distinct
# @lc code=end

