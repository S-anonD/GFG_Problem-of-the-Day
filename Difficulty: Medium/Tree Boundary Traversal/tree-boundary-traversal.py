#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def boundaryTraversal(self, root):
        res = []
        if not root:
            return res
        if not self.isLeaf(root):
            res.append(root.data)
        self.collectBoundaryLeft(root.left, res)
        self.collectLeaves(root, res)
        self.collectBoundaryRight(root.right, res)
        return res
    
    def isLeaf(self, node):
        return node.left is None and node.right is None
    
    def collectBoundaryLeft(self, root, res):
        if root is None or self.isLeaf(root):
            return
        res.append(root.data)
        if root.left:
            self.collectBoundaryLeft(root.left, res)
        elif root.right:
            self.collectBoundaryLeft(root.right, res)
    
    def collectLeaves(self, root, res):
        if root is None:
            return
        if self.isLeaf(root):
            res.append(root.data)
            return
        self.collectLeaves(root.left, res)
        self.collectLeaves(root.right, res)
    
    def collectBoundaryRight(self, root, res):
        if root is None or self.isLeaf(root):
            return
        if root.right:
            self.collectBoundaryRight(root.right, res)
        elif root.left:
            self.collectBoundaryRight(root.left, res)
        res.append(root.data)
        # Code here




#{ 
 # Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{
#  Driver Code Starts
import sys

import sys

sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    #Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        obj = Solution()
        res = obj.boundaryTraversal(root)
        for i in res:
            print(i, end=" ")
        print('')
        print("~")

# } Driver Code Ends