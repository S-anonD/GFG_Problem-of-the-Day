#User function Template for python3

class Solution:

    def countPS(self, s):
        n = len(s)
        memo = [[-1 for i in range(n)] for i in range(n)]
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.isPalindrome(i, j, s, memo) == 1:
                    res += 1
        return res
    
    def isPalindrome(self, i, j, s, memo):
        if i == j:
            return 1
        if j == i + 1 and s[i] == s[j]:
            return 1
        if memo[i][j] != -1:
            return memo[i][j]
        if s[i] == s[j] and self.isPalindrome(i + 1, j - 1, s, memo):
            memo[i][j] = 1
        else:
            memo[i][j] = 0
        return memo[i][j]
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countPS(s))

        print("~")
# } Driver Code Ends