class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxP = 0
        cheapest = prices[0]
        for i in range(len(prices)):
            cheapest = min(cheapest, prices[i])
            currPrice = prices[i] - cheapest
            maxP = max(currPrice, maxP)
        return maxP