class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]] += 1
            else:
                dict1[nums[i]] = 1
        dictSorted = sorted(dict1.items(), key=lambda x: x[1], reverse = True)
        topkeys = []
        for i in dictSorted[:k]:
            key = i[0]
            topkeys.append(key)
        return topkeys