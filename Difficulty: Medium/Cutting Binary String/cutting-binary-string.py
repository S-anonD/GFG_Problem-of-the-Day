class Solution:
    def cuts(self, s):
        if s[0] == '0':
            return -1
        powersOf5 = set()
        val = 1
        while val <= 10**9:
            powersOf5.add(val)
            val *= 5
        n = len(s)
        memo = [-1] * (n + 1)
        ans = self.findMinCuts(0, s, memo, powersOf5)
        return -1 if ans >= n+1 else ans
        # code here
    
    def findMinCuts(self, i, s, memo, powersOf5):
        n = len(s)
        if i >= n:
            return 0
        if memo[i] != -1:
            return memo[i]
        ans = n+1
        num = 0
        for j in range(i, n):
            num = num * 2 + (1 if s[j] == '1' else 0)
            if s[i] != '0' and num in powersOf5:
                next_cut = self.findMinCuts(j + 1, s, memo, powersOf5)
                if next_cut != n+1:
                    ans = min(ans, 1 + next_cut)
        memo[i] = ans
        return ans
        