#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
        }
        return self.recursion(digits, letters)
    def recursion(self, digits, letters):
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return letters[int(digits[0])]
        result = self.recursion(digits[1:], letters)
        temp = []
        for l in letters[int(digits[0])]:
            for i in range(len(result)):
                temp.append(l+result[i])
        return temp
# @lc code=end

