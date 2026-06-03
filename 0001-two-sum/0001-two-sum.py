class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, v in enumerate(nums):
            comp = target - v
            if comp in map:
                return [i, map[comp]]
            else:
                map[v] = i