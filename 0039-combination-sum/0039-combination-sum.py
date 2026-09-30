class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # left: can still use curr idx
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()

            # right: cannot use curr idx
            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return res