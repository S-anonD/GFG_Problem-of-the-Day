class Solution:
    def maxGold(self, mat):
        n, m = len(mat), len(mat[0])
        for y in range(m - 2, -1, -1):
            for x in range(n):
                maxprev = 0
                if self.isValid(x - 1, y + 1, n, m):
                    maxprev = max(maxprev, mat[x - 1][y + 1])
                if self.isValid(x, y + 1, n, m):
                    maxprev = max(maxprev, mat[x][y + 1])
                if self.isValid(x + 1, y + 1, n, m):
                    maxprev = max(maxprev, mat[x + 1][y + 1])
                mat[x][y] += maxprev
        res = max(mat[i][0] for i in range(n))
        return res
        # code here
    
    def isValid(self, x, y, n, m):
        return 0 <= x < n and 0 <= y < m