class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i, v in enumerate(nums):
            if v in dict1:
                dict1[v] += 1
            else:
                dict1[v] = 1

        dictSorted = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        topKeys = []
        for i in dictSorted[:k]:
            key = i[0]
            topKeys.append(key)

        return topKeys