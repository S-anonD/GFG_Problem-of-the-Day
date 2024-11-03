# 03/11/24
# Is Linked List Length Even?

class Solution:
    def isLengthEven(self, head):
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        return count%2==0