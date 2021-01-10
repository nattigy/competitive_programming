class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        for i in range(R + C):
            if i == 0:
                res.append([r0, c0])
            else:
                for x in range(r0 - i, r0 + i + 1):
                    if x >= 0 and x < R:
                        for y in range(c0 - i, c0 + i + 1):
                            if y >= 0 and y < C:
                                if abs(x - r0) + abs(y - c0) == i:
                                    res.append([x, y])

        return res