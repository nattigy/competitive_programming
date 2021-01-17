class Solution:
    def isValid(self, s: str) -> bool:
        # "()[]{}"
        opened = "([{"
        closed = ")]}"
        i = 0
        if len(s) == 1:
            return False
        while s != "" and i < len(s):
            if s[i] in closed:
                if i == 0:
                    return False
                if opened.index(s[i - 1]) == closed.index(s[i]):
                    s = s[: i - 1] + s[i + 1 :]
                    i -= 1
                else:
                    return False
            else:
                i += 1

        if s == "":
            return True
        return False
