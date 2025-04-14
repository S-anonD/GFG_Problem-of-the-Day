#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [100000000] * V
        dist[src] = 0
        for i in range(V):
            for edge in edges:
                u, v, wt = edge
                if dist[u] != 100000000 and dist[u] + wt < dist[v]:
                    if i == V - 1:
                        return [-1]
                    dist[v] = dist[u] + wt
        return dist
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V = int(input())
        E = int(input())
        edges = []
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            edges.append([u, v, w])
        S = int(input())
        ob = Solution()

        res = ob.bellmanFord(V, edges, S)
        for i in res:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends