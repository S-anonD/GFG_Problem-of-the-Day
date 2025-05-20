class Solution(object):
    def kthSmallest(self, m, n, k):
        l, h = 1, m * n
        while l < h:
            mid = (l + h) // 2
            if self.count(mid, m, n) < k:
                l = mid + 1
            else:
                h = mid
        return l
    
    def count(self, val, m, n):
        cnt = 0
        for i in range(1, m + 1):
            cnt += min(val // i, n)
        return cnt
        #code here