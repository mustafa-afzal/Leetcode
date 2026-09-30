class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subSet = []
        def dfs(i):
            if i >= len(nums):
                res.append(subSet.copy())
                return
            
            # include it
            subSet.append(nums[i])
            dfs(i + 1)

            # don't include it
            subSet.pop()
            dfs(i + 1)
            
        dfs(0)
        return res