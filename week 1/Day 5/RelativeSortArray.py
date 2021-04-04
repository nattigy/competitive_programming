class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = 0
        for i in range(len(arr2)):
            for j in range(n, len(arr1)):
                if arr2[i] == arr1[j]:
                    arr1[j], arr1[n] = arr1[n], arr1[j]
                    n += 1

            if i + 1 == len(arr2):
                newArr = sorted(arr1[n:])
                for x in range(len(newArr)):
                    arr1[n] = newArr[x]
                    n += 1

        return arr1