#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        n = len(s)
        res = 0
        lastIndex = [-1] * 26
        start = 0
        for end in range(n):
            start = max(start, lastIndex[ord(s[end]) - ord('a')] + 1)
            res = max(res, end - start + 1)
            lastIndex[ord(s[end]) - ord('a')] = end
        return res
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends