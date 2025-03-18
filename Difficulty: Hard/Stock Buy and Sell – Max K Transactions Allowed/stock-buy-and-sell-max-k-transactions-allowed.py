class Solution:
    def maxProfit(self, prices, k):
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for l in range(1, k + 1):
                dp[i][l][1] = max(dp[i + 1][l][0] - prices[i], dp[i + 1][l][1])
                dp[i][l][0] = max(prices[i] + dp[i + 1][l - 1][1], dp[i + 1][l][0])
        return dp[0][k][1]
        # code here


#{ 
 # Driver Code Starts
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends