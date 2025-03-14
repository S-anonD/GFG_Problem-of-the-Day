class Solution:
	def minCoins(self, coins, sum):
	    dp = [[0] * (sum + 1) for _ in range(len(coins))]
	    for i in range(len(coins) - 1, -1, -1):
	        for j in range(1, sum + 1):
	            dp[i][j] = float('inf')
	            take = float('inf')
	            noTake = float('inf')
	            if j - coins[i] >= 0:
	                take = dp[i][j - coins[i]]
	                if take != float('inf'):
	                    take += 1
	            if i + 1 < len(coins):
	                noTake = dp[i + 1][j]
	            dp[i][j] = min(take, noTake)
	    if dp[0][sum] != float('inf'):
	        return dp[0][sum]
	    return -1
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends