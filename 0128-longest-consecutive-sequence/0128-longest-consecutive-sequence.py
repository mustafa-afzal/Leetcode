class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLen = 0
        for i in numsSet:
            if i - 1 not in numsSet:
                j = i
                length = 1
                while i + length in numsSet:
                    length += 1
                maxLen = max(length, maxLen)
        return maxLen
            