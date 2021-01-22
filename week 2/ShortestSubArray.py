class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        sub = []
        if len(A) == 0:
            return -1
        if len(A) == 1 and A[0] < K:
            return -1
        elif len(A) == 1 and A[0] == K:
            return 1

        summ = 0
        length = 0

        fast = 0
        slow = 0
        while slow < len(A):
            summ += A[fast]
            length += 1
            if A[fast] >= K:
                return 1
            if summ >= K:
                sub.append(length)
                summ = 0
                length = 0
                slow += 1
                fast = slow
            else:
                fast += 1
            if fast == len(A):
                slow += 1
                fast = slow
                summ = 0
                length = 0

        # for i in range(len(A)):
        #     summ = A[i]
        #     if summ >= K:
        #         return 1
        #     for j in range(i+1,len(A)):
        #         summ += A[j]
        #         if summ >= K:
        #             sub.append((j+1)-i)
        #             break

        if len(sub) == 0:
            return -1

        sm = sub[0]
        for i in range(len(sub)):
            if sub[i] < sm:
                sm = sub[i]

        return sm
