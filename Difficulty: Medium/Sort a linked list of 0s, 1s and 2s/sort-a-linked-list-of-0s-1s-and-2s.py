#User function Template for python3
'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        if not head or not head.next:
            return head
        cntZero = 0
        cntOne = 0
        cntTwo = 0
        curr = head
        while curr:
            if curr.data == 0:
                cntZero += 1
            elif curr.data == 1:
                cntOne += 1
            else:
                cntTwo += 1
            curr = curr.next
        curr = head
        while cntZero:
            curr.data = 0
            curr = curr.next
            cntZero -= 1
        while cntOne:
            curr.data = 1
            curr = curr.next
            cntOne -= 1
        while cntTwo:
            curr.data = 2
            curr = curr.next
            cntTwo -= 1
        return head
        #code here
    


#{ 
 # Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().segregate(head))
        print("~")

# } Driver Code Ends