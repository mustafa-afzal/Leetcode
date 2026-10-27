class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        def backtrack(path, i):
            if i == len(nums):
                res.append(path.copy())
                return
            if i > len(nums):
                return
            # include
            path.append(nums[i])
            backtrack(path, i+1)
            path.pop()

            # don't include, if skip then skip duplicates as well
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(path, i+1)
        backtrack([], 0)
        return res