class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        path = []
        res = []
        n = len(nums)
        def dfs(path, i):
            if i == n:
                res.append(path.copy())
            if i >= n or len(path) > n:
                return
            # include
            path.append(nums[i])
            dfs(path, i + 1)
            path.pop()

            # don't include
            dfs(path, i + 1)
        dfs(path, 0)
        return res