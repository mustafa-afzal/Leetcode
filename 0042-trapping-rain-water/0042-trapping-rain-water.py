class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        trapped = 0
        while l <= r:
            if leftMax <= rightMax:
                leftMax = max(leftMax, height[l])
                trapped += leftMax - height[l]
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                trapped += rightMax - height[r]
                r -= 1
        return trapped

