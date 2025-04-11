class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        adj = self.constructAdj(edges, V)
        pq = []
        dist = [sys.maxsize] * V
        heapq.heappush(pq, [0, src])
        dist[src] = 0
        while pq:
            u = heapq.heappop(pq)[1]
            for x in adj[u]:
                v, weight = x[0], x[1]
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, [dist[v], v])
        return dist
    
    def constructAdj(self, edges, V):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v, wt = edge
            adj[u].append([v, wt])
            adj[v].append([u, wt])
        return adj
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

        src = int(input())

        obj = Solution()
        res = obj.dijkstra(V, edges, src)

        print(" ".join(map(str, res)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends