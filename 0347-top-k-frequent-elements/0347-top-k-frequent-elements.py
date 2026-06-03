from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        dictSorted = sorted(map.items(), key=lambda x: x[1], reverse=True)

        topkeys = []
        for i in dictSorted[:k]:
            key = i[0]
            topkeys.append(key)
        return topkeys
