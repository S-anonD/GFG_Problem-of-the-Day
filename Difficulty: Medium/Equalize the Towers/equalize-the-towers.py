class Solution:
    def minCost(self, heights, cost):
        n = len(heights)
        mini, maxi = min(heights), max(heights)
        low = mini
        high = maxi
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            val1 = self.findCost(heights, cost, mid - 1)
            val2 = self.findCost(heights, cost, mid)
            val3 = self.findCost(heights, cost, mid + 1)
            if val2 <= val1 and val2 <= val3:
                ans = val2
                break
            elif val1 >= val2 and val2 >= val3:
                low = mid + 1
            elif val2 >= val1 and val3 >= val2:
                high = mid - 1
        return ans
    
    def findCost(self, heights, cost, h):
        res = 0
        n = len(heights)
        for i in range(n):
            res += cost[i] * abs(heights[i] - h)
        return res
        # code here