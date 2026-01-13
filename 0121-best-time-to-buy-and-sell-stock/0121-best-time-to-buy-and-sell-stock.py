class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        maxP = 0
        for i in range(len(prices)):
            if prices[i] < cheapest:
                cheapest = prices[i]
            currP = prices[i] - cheapest
            maxP = max(currP, maxP)
        return maxP