class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = ""
        for i in s:
            for j in range(len(t)):
                if i == t[j]:
                    res = res + t[j]
                    t = t[:j] + t[j + 1 :]
                    break
        return s == res and t == ""