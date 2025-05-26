class Solution:
	def leafNodes(self, preorder):
	    n = len(preorder)
	    inorder = sorted(preorder)
	    leaves = []
	    ind = [0]
	    self.leafNodesRec(preorder, inorder, 0, n - 1, ind, leaves)
        return leaves
	
	def binsearch(self, inorder, l, r, d):
	    mid = (l + r) // 2
	    if inorder[mid] == d:
	        return mid
        elif inorder[mid] > d:
            return self.binsearch(inorder, l, mid - 1, d)
        else:
            return self.binsearch(inorder, mid + 1, r, d)
    
    def leafNodesRec(self, preorder, inorder, l, r, ind, leaves):
        if l == r:
            leaves.append(inorder[l])
            ind[0] += 1
            return
        if l < 0 or l > r or r >= len(inorder):
            return
        loc = self.binsearch(inorder, l, r, preorder[ind[0]])
        ind[0] += 1
        self.leafNodesRec(preorder, inorder, l, loc - 1, ind, leaves)
        self.leafNodesRec(preorder, inorder, loc + 1, r, ind, leaves)
		# code here
