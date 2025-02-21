
class Solution:
    def maxLength(self, s):
        maxlen = 0
        open = close = 0
        for ch in s:
            if ch == '(':
                open += 1
            elif ch == ')':
                close += 1
            if open == close:
                maxlen = max(maxlen, 2*close)
            elif close > open:
                 open = close = 0
        open = close = 0
        for ch in reversed(s):
            if ch == '(':
                open += 1
            elif ch == ')':
                close += 1
            if open == close:
                maxlen = max(maxlen, 2*open)
            elif open > close:
                 open = close = 0
        return maxlen
        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends