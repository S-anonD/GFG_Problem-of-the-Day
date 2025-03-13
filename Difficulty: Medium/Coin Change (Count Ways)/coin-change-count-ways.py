class Solution:
    def count(self, coins, sum):
        memo = [[-1 for _ in range(sum + 1)] for _ in range(len(coins))]
        return self.countRec(coins, len(coins), sum, memo)
    
    def countRec(self, coins, n, sum, memo):
        if sum == 0:
            return 1
        if sum < 0 or n == 0:
            return 0
        if memo[n - 1][sum] != -1:
            return memo[n - 1][sum]
        memo[n - 1][sum] = (self.countRec(coins, n, sum - coins[n - 1], memo) +
        self.countRec(coins, n - 1, sum, memo))
        return memo[n - 1][sum]
        # code here 



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        coins = list(map(int, input().strip().split()))
        sum = int(input())
        ob = Solution()
        print(ob.count(coins, sum))

        print("~")

# } Driver Code Ends