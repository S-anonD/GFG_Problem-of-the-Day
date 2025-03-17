class Solution:
    def equalPartition(self, arr):
        arrsum = sum(arr)
        n = len(arr)
        if arrsum % 2 != 0:
            return False
        arrsum //= 2
        dp = [[False] * (arrsum + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, arrsum + 1):
                if j < arr[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
        return dp[n][arrsum]
        # code here


#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends