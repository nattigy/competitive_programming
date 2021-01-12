class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        nums = []

        for i in range(1, n + 1):
            res.append("Push")
            nums.append(i)
            if i not in target:
                res.append("Pop")
                nums.pop()
            if len(target) == len(nums):
                break

        return res