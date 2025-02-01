class Solution:
	def isWordExist(self, mat, word):
	    wlen = len(word)
	    n, m = len(mat), len(mat[0])
	    if wlen > n*m:
	        return False
	    for i in range(n):
	        for j in range(m):
	            if mat[i][j] == word[0]:
	                if self.findMatch(mat, word, i, j, 0):
	                    return True
	    return False
	
	def findMatch(self, mat, word, x, y, widx):
	    wlen = len(word)
	    n, m = len(mat), len(mat[0])
	    if wlen == widx:
	        return True
	    if x < 0 or y < 0 or x >= n or y >= m:
	        return False
	    if mat[x][y] == word[widx]:
	        temp = mat[x][y]
	        mat[x][y] = '#'
	        res = (self.findMatch(mat, word, x-1, y, widx+1) or
	        self.findMatch(mat, word, x+1, y, widx+1) or
	        self.findMatch(mat, word, x, y-1, widx+1) or
	        self.findMatch(mat, word, x, y+1, widx+1))
	        mat[x][y] = temp
	        return res
	    return False
		#Code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends