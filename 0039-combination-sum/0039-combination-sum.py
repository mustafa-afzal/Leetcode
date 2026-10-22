class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        path = []
        res = []
        def backtrack(sum, i):
            if sum == target:
                res.append(path.copy())
                return
            if sum > target or i >= len(candidates):
                return
            # append same number
            path.append(candidates[i])
            backtrack(sum + candidates[i], i)
            path.pop()

            # go to the next number
            backtrack(sum, i + 1)
        backtrack(0, 0)
        return res