from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqNums = Counter(nums)
        numsSorted = sorted(freqNums.items(), 
            key = lambda x: x[1], reverse=True)
        topKeys = []
        for i in numsSorted[:k]:
            key = i[0]
            topKeys.append(key)
        return topKeys
