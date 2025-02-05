#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        preindex = [0]
        return self.buildTreeRecur(inorder, preorder, preindex, 0, len(preorder)-1)
    
    def search(self, inorder, val, left, right):
        for i in range(left, right+1):
            if inorder[i] == val:
                return i
        return -1
    
    def buildTreeRecur(self, inorder, preorder, preindex, left, right):
        if left > right:
            return None
        rootval = preorder[preindex[0]]
        preindex[0] += 1
        root = Node(rootval)
        index = self.search(inorder, rootval, left, right)
        root.left = self.buildTreeRecur(inorder, preorder, preindex, left, index-1)
        root.right = self.buildTreeRecur(inorder, preorder, preindex, index+1, right)
        return root
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildTree(inorder, preorder)
        printPostorder(root)
        print()

# } Driver Code Ends