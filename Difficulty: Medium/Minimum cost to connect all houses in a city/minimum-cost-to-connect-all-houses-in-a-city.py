#User function Template for python3
class Solution:
    def minCost(self, houses):
        n = len(houses)
        minHeap = [(0, 0)]
        visited = [False] * n
        totalCost = 0
        while minHeap:
            cost, u = heapq.heappop(minHeap)
            if visited[u]:
                continue
            visited[u] = True
            totalCost += cost
            for v in range(n):
                if not visited[v]:
                    dist = self.manhattanDistance(houses[u], houses[v])
                    heapq.heappush(minHeap, (dist, v))
        return totalCost
    
    def manhattanDistance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
import heapq
      # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []

        for _ in range(n):
            temp = list(map(int, input().split()))
            edges.append(temp)

        obj = Solution()
        print(obj.minCost(edges))
        print("~")
# } Driver Code Ends