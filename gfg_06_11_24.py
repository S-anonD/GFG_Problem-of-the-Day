# 06/11/24
# Root to leaf paths sum

class Solution:
    def treePathSum(self,root):
        if not root:
            return 0
        self.res = 0
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, node, curr_sum):
        if not node:
            return
        curr_sum = curr_sum * 10 + node.data
        if not node.left and not node.right:
            self.res += curr_sum
            return
        self.dfs(node.left, curr_sum)
        self.dfs(node.right, curr_sum)