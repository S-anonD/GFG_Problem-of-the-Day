class Solution:
    def findMinCycle(self, V, edges):
        adj = self.constructadj(V, edges)
        mincycle = float('inf')
        for edge in edges:
            u, v, w = edge
            dist = self.shortestPath(V, adj, u, v)
            if dist != float('inf'):
                mincycle = min(mincycle, dist + w)
        return mincycle
    
    def constructadj(self, V, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v, w = edge
            adj[u].append((v, w))
            adj[v].append((u, w))
        return adj
    
    def shortestPath(self, V, adj, src, dest):
        dist = [float('inf')] * V
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if (u == src and v == dest) or (u == dest and v == src):
                    continue
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist[dest]
        # code here
        

        



#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import heapq

# Position this line where user code will be pasted.


def main():
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v, w = map(int, input().split())
            edges.append([u, v, w])
            edges.append([v, u, w])  # Since the graph is undirected

        obj = Solution()
        res = obj.findMinCycle(V, edges)

        print(res)


if __name__ == "__main__":
    main()

# } Driver Code Ends