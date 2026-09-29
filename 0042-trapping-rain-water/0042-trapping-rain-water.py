class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        trapped = 0
        while l <= r:
            if lMax <= rMax:
                lMax = max(lMax, height[l])
                trapped += lMax - height[l]
                l += 1
            else:
                rMax = max(rMax, height[r])
                trapped += rMax - height[r]
                r -= 1
        return trapped