'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        result = -1
        while root is not None:
            if root.data <= k:
                result = root.data
                root = root.right
            else:
                root = root.left
        return result
        #code here