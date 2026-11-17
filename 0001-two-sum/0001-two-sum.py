class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in map:
                return [map[diff], i]
            map[v] = i