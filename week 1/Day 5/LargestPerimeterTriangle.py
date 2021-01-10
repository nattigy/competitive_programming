class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        n = len(A)
        p = 0

        largest = 0
        for i in range(n - 1, -1, -1):
            largest = A[i]
            for j in range(i - 1, -1, -1):
                if A[j] > largest:
                    largest = A[j]
                    A[i], A[j] = A[j], A[i]

            if i <= n - 3:
                if A[i] + A[i + 1] > A[i + 2]:
                    p = A[i + 2] + A[i + 1] + A[i]
                    break

        return p
