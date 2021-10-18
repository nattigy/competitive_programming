#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.recursion(nums)
    
    def recursion(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        lists = self.recursion(nums[1:])
        for ls in lists:
            temp = [x for x in ls]
            for i in range(len(ls)):
                temp.insert(i, nums[0])
                res.append(temp)
                temp = [x for x in ls]
            temp.append(nums[0])
            res.append(temp)
        return res
# @lc code=end

