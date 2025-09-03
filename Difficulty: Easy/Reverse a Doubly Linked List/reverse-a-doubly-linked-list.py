"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        prevNode = None
        currNode = head
        while currNode is not None:
            prevNode = currNode.prev
            currNode.prev = currNode.next
            currNode.next = prevNode
            currNode = currNode.prev
        return prevNode.prev
        # code here
        
        