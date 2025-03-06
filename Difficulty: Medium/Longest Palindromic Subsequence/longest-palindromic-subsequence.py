#User function Template for python3

class Solution:

    def longestPalinSubseq(self, s):
        n = len(s)
        memo = [[-1 for _ in range(n)] for _ in range(n)]
        return self.lps(s, 0, n - 1, memo)
    
    def lps(self, s, low, high, memo):
        if low > high:
            return 0
        if low == high:
            return 1
        if memo[low][high] != -1:
            return memo[low][high]
        if s[low] == s[high]:
            memo[low][high] = self.lps(s, low + 1, high - 1, memo) + 2
        else:
            memo[low][high] = max(self.lps(s, low, high - 1, memo),
            self.lps(s, low + 1, high, memo))
        return memo[low][high]
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
        print("~")
# } Driver Code Ends