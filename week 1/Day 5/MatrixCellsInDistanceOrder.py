class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        for x in range(R):
            for y in range(C):
                res.append((abs(x - r0) + abs(y - c0), (x, y)))

        res.sort()
        for i in range(len(res)):
            res[i] = res[i][1]

        return res