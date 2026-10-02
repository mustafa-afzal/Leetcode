class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue

                path.append(nums[i])
                dfs(path)
                path.pop()
        dfs([])
        return res
            
                