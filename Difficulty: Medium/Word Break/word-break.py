class Solution:
    def wordBreak(self, s, dictionary):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for w in dictionary:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:start + len(w)] == w:
                    dp[i] = True
                    break
        return 1 if dp[n] else 0
        # code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        s = input().strip()
        dictionary = input().strip().split()
        ob = Solution()
        res = ob.wordBreak(s, dictionary)
        if res:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends