import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = max(piles)
        while l <= r:
            mid = (l + r) // 2
            pileTime = 0
            for i in range(len(piles)):
                pileTime += math.ceil(piles[i] / mid)
            if pileTime <= h:
                minK = min(mid, minK)
                r = mid - 1
            else:
                l = mid + 1
        return minK