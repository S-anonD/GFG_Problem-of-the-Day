class Solution:
    def getLastMoment(self, n, left, right):
        res = 0
        for i in range(len(left)):
            res = max(res, left[i])
        for i in range(len(right)):
            res = max(res, n - right[i])
        return res
        # code here