
class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, maxlen = 0, 1
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if maxlen < 2:
                    start, maxlen = i, 2
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if k > maxlen:
                        start, maxlen = i, k
        return s[start:start + maxlen]
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends