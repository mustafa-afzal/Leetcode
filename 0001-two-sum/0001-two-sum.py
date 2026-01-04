class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dict1 and dict1[comp] != i:
                return i, dict1[comp]

        

            