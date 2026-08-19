class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        res = 1
        for i in range(len(nums)):
            answer[i] = res
            res *= nums[i]
        res = 1
        for i in range(len(nums) -1, -1, -1):
            answer[i] *= res
            res *= nums[i]
        return answer