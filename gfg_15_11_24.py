# 15/11/24
# Second Largest

class Solution:
    def getSecondLargest(self, arr):
        targ = max(arr)
        temp = [x for x in arr if x != targ]
        if temp != []:
            return max(temp)
        return -1