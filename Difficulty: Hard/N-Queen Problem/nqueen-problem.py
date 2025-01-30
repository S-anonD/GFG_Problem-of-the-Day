#User function Template for python3

class Solution:
    def nQueen(self, n):
        res = []
        board = []
        visited = [False] * (n+1)
        self.nQueenUtil(1, n, board, res, visited)
        return res
    
    def isSafe(self, board, currRow, currCol):
        for i in range(len(board)):
            placedRow = board[i]
            placedCol = i+1
            if abs(placedRow - currRow) == abs(placedCol - currCol):
                return False
        return True
    
    def nQueenUtil(self, col, n, board, res, visited):
        if col > n:
            res.append(board.copy())
            return
        for row in range(1, n+1):
            if not visited[row]:
                if self.isSafe(board, row, col):
                    visited[row] = True
                    board.append(row)
                    self.nQueenUtil(col+1, n, board, res, visited)
                    board.pop()
                    visited[row] = False
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends