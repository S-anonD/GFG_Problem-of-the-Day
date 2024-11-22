# 22/11/24
# Stock Buy and Sell – Max one Transaction Allowed

class Solution:
    def maximumProfit(self, prices):
        minSoFar = prices[0]
        res = 0
        
        for i in range(1, len(prices)):
            minSoFar = min(minSoFar, prices[i])
            
            res = max(res, prices[i] - minSoFar)
        
        return res