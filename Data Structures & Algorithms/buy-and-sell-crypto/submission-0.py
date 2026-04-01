class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        maxp=0
        for i in range(len(prices)):
            lowest=min(lowest,prices[i])
            profit=prices[i]-lowest
            maxp=max(maxp,profit)
        
        return maxp
        