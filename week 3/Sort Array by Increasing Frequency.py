class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = [0 for i in range(201)]
        res = []
        for i in nums:
            freq[i + 100] += 1
        
        for i in range(len(nums)):
            mn = 111
            index = 0
            for j in range(len(freq)):
                if freq[j] != 0:
                    if mn > freq[j]:
                        mn = freq[j]
                        index = j
                    elif mn == freq[j]:
                        if j > index:
                            mn = freq[j]
                            index = j
                        else:
                            mn = freq[index]
            for x in range(freq[index]):
                res.append(index - 100)
            freq[index] = 0
        return res
