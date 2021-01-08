class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = 0
        for i in range(len(arr2)):
            for j in range(n, len(arr1)):
                for k in range(j, len(arr1)):
                    if arr2[i] == arr1[k]:
                        arr1[j], arr1[k] = arr1[k], arr1[j]
                        n += 1
                        break
            if i + 1 == len(arr2):
                smallest = 0
                for x in range(n, len(arr1)):
                    smallest = arr1[x]
                    for y in range(x + 1, len(arr1)):
                        if arr1[y] < smallest:
                            smallest = arr1[y]
                            arr1[x], arr1[y] = arr1[y], arr1[x]

        return arr1