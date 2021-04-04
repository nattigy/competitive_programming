class Solution:
    def binarySearch(self, nums: List[int], small: int, large: int, target: int) -> int:
        if small > large:
            return -1
        if small == large:
            if nums[small] == target:
                return small
            return -1
        mid = (small + large) // 2
        if target < nums[mid]:
            return self.binarySearch(nums, small, mid-1, target)
        elif target > nums[mid]:
            return self.binarySearch(nums, mid+1, large, target)
        else:
            return mid

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums)-1, target)
        