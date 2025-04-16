#User function template for Python

class Solution:
	def floydWarshall(self, dist):
	    V = len(dist)
	    INF = 10**8
	    for k in range(V):
	        for i in range(V):
	            for j in range(V):
	                if dist[i][k] != INF and dist[k][j] != INF:
	                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
		#Code here


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        obj = Solution()
        obj.floydWarshall(matrix)
        for _ in range(n):
            for __ in range(n):
                print(matrix[_][__], end=" ")
            print()
        print("~")

# } Driver Code Ends