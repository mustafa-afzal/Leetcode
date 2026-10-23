class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        path = []
        res = []
        candidates.sort()
        def backtrack(sum, path, i):
            if sum == target:
                res.append(path.copy())
                return
            if sum > target or i >= len(candidates):
                return
            # append and move to next idx
            path.append(candidates[i])
            backtrack(sum + candidates[i], path, i + 1)
            path.pop()

            # don't append and move to next idx
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(sum, path, i + 1)
        backtrack(0, path, 0)
        return res