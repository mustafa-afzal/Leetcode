from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dictNums = Counter(nums)
        countZero = dictNums[0]
        countOne = dictNums[1]
        countTwo = dictNums[2]
        for i in range(countZero):
            nums[i] = 0
        for i in range(countOne):
            nums[i + countZero] = 1
        for i in range(countTwo):
            nums[i + countZero + countOne] = 2
        return nums