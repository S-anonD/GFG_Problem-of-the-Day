#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def addTwoLists(self, num1, num2):
        num1 = self.trimLeadingZeroes(num1)
        num2 = self.trimLeadingZeroes(num2)
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)
        carry = [0]
        res = self.addListRec(num1, num2, carry)
        if carry[0] != 0:
            newNode = Node(carry[0])
            newNode.next = res
            res = newNode
        return self.reverse(res)
    
    def reverse(self, head):
        prev = None
        curr = head
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    def trimLeadingZeroes(self, head):
        while head and head.data == 0:
            head = head.next
        return head
    
    def addListRec(self, num1, num2, carry):
        if num1 is None and num2 is None and carry[0] == 0:
            return None
        sum = carry[0]
        if num1 is not None:
            sum += num1.data
            num1 = num1.next
        if num2 is not None:
            sum += num2.data
            num2 = num2.next
        carry[0] = sum // 10
        res = Node(sum % 10)
        res.next = self.addListRec(num1, num2, carry)
        return res
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):

        arr1 = (int(x) for x in input().split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)

        arr2 = (int(x) for x in input().split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)

        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
        print("~")

# } Driver Code Ends