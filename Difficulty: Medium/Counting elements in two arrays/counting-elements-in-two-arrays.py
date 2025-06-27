class Solution:
    def countLessEq(self, a, b):
        n, m = len(a), len(b)
        res = [0] * n
        cnt = [0] * 100001
        for i in range(m):
            cnt[b[i]] += 1
        for i in range(1, 100001):
            cnt[i] += cnt[i - 1]
        for i in range(n):
            res[i] = cnt[a[i]]
        return res
        # code here
        