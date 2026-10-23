class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for num in nums:
                if num in path:
                    continue
                # append num
                path.append(num)
                backtrack(path)
                path.pop()
        backtrack([])
        return res
