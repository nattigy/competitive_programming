class Solution:
    def mergeTwoLists(self, l1: List[int], l2: List[int]) -> List[int]:
        response = []
        x = 0
        y = 0
        while x < len(l1) and y < len(l2):
            if l1[x] <= l2[y]:
                response.append(l1[x])
                x += 1
            else:
                response.append(l2[y])
                y += 1
        if x < len(l1):
            while x < len(l1):
                response.append(l1[x])
                x += 1
        if y < len(l2):
            while y < len(l2):
                response.append(l2[y])
                y += 1
        return response

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        l1 = self.sortArray(nums[:mid])
        l2 = self.sortArray(nums[mid:])
        return self.mergeTwoLists(l1, l2)
