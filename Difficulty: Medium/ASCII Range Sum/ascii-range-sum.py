class Solution:
    def asciirange(self, s):
        res = []
        n = len(s)
        checked = set()
        reversed = s[::-1]
        for i in range(n):
            if s[i] not in checked and s.count(s[i]) >= 2:
                j = n - reversed.index(s[i]) - 1
                sum = 0
                for k in range(i + 1, j):
                    sum += ord(s[k])
                if sum != 0:
                    res.append(sum)
                checked.add(s[i])
        return res
        # code here