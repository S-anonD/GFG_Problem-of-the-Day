#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        self.solveSudokuRec(mat, 0, 0)
    
    def solveSudokuRec(self, mat, row, col):
        if row == 8 and col == 9:
            return True
        if col == 9:
            row += 1
            col = 0
        if mat[row][col] != 0:
            return self.solveSudokuRec(mat, row, col+1)
        for num in range(1, 10):
            if self.isSafe(mat, row, col, num):
                mat[row][col] = num
                if self.solveSudokuRec(mat, row, col+1):
                    return True
                mat[row][col] = 0
        return False
    
    def isSafe(self, mat, row, col, num):
        for x in range(9):
            if mat[row][x] == num:
                return False
        for x in range(9):
            if mat[x][col] == num:
                return False
        startRow = row - (row % 3)
        startCol = col - (col % 3)
        for i in range(3):
            for j in range(3):
                if mat[i + startRow][j + startCol] == num:
                    return False
        return True
        
        # Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        matrix = []
        n = 9
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.solveSudoku(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends