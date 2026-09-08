class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLen = 0
        for i in numsSet:
            if i - 1 not in numsSet:
                j = i
                length = 0
                while j in numsSet:
                    j += 1
                    length += 1
                maxLen = max(length, maxLen)
        return maxLen