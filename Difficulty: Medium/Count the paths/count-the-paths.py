class Solution:
    def countPaths(self, edges, V, src, dest):
        adj = [[] for _ in range(V)]
        for e in edges:
            adj[e[0]].append(e[1])
        memo = [-1] * V
        return self.dfs(src, dest, adj, memo)
    
    def dfs(self, u, dest, adj, memo):
        if u == dest:
            return 1
        if memo[u] != -1:
            return memo[u]
        count = 0
        for v in adj[u]:
            count += self.dfs(v, dest, adj, memo)
        memo[u] = count
        return count
        #Code here