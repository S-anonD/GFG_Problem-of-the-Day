#User function Template for python3

class Solution:
    def numIslands(self, grid):
        row, col = len(grid), len(grid[0])
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 'L':
                    self.dfs(grid, r, c)
                    count += 1
        return count
        # code here
    
    def isSafe(self, grid, r, c):
        row, col = len(grid), len(grid[0])
        return (0 <= r < row) and (0 <= c < col) and grid[r][c] == 'L'
    
    def dfs(self, grid, r, c):
        rNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        cNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        grid[r][c] = 'W'
        for k in range(8):
            newR = r + rNbr[k]
            newC = c + cNbr[k]
            if self.isSafe(grid, newR, newC):
                self.dfs(grid, newR, newC)


#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input().strip())
        m = int(input().strip())
        grid = [input().strip().split() for _ in range(n)]

        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends