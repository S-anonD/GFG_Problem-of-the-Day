class Solution:
    def uniquePaths(self, grid):
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
            return 0
        dp = [[0] * m for _ in range(n)]
        dp[n - 1][m - 1] = 1
        for j in range(m - 2, -1, -1):
            if grid[n - 1][j] == 1:
                break
            else:
                dp[n - 1][j] = 1
        for i in range(n - 2, -1, -1):
            if grid[i][m - 1] == 1:
                break
            else:
                dp[i][m - 1] = 1
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]
        # code here 