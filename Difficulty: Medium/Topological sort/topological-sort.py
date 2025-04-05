class Solution:
    
    def topoSort(self, V, edges):
        stack = []
        visited = [False] * V
        adj = self.constructadj(V, edges)
        for i in range(V):
            if not visited[i]:
                self.topoSortUtil(i, adj, visited, stack)
        return stack[::-1]
        # Code here
    
    def constructadj(self, V, edges):
        adj = [[] for _ in range(V)]
        for it in edges:
            adj[it[0]].append(it[1])
        return adj
    
    def topoSortUtil(self, v, adj, visited, stack):
        visited[v] = True
        for i in adj[v]:
            if not visited[i]:
                self.topoSortUtil(i, adj, visited, stack)
        stack.append(v)



#{ 
 # Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10**6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))
            adj[u].append(v)

        obj = Solution()
        res = obj.topoSort(V, edges)

        if check(adj, V, res):
            print("true")
        else:
            print("false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends