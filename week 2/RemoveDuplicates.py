class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        while i < len(S) - 1 and S != "":
            if S[i] == S[i + 1]:
                S = S[:i] + S[i + 2 :]
                i -= 1 if i > 0 else 0
            else:
                i += 1
        return S