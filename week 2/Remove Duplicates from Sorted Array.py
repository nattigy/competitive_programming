class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        length = len(nums)
        i = 1
        curr = 0
        while i < length:
            if nums[curr] == nums[i]:
                nums.pop(i)
                length -= 1
            else:
                curr = i
                i += 1
        
        return len(nums)
