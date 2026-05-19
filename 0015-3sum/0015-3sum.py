class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        r = len(nums) - 1
        res = []
        nums = sorted(nums)
        for i in range(0, r):
            l, r = i + 1, len(nums) - 1
            if i != 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
            