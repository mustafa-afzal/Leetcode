class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        def backtrack(path, i):
            if i == len(nums):
                print(path, "Res: ", res)
                if path not in res:
                    res.append(path.copy())
                return
            if i > len(nums):
                return
            # include
            path.append(nums[i])
            backtrack(path, i+1)
            path.pop()

            # don't include
            backtrack(path, i+1)
        backtrack([], 0)
        return res