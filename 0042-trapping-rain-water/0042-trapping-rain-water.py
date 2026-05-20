class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = height[0], height[len(height) - 1]
        l, r = 0, len(height) - 1
        trapped = 0
        while l <= r:
            if leftMax <= rightMax:
                leftMax = max(height[l], leftMax)
                trapped += leftMax - height[l]
                l += 1
            else:
                rightMax = max(height[r], rightMax)
                trapped += rightMax - height[r]
                r -= 1
        return trapped
            
            
                