# 09/11/24
# Minimum sum

class Solution:
    def addString(self, s1, s2):
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0
        res = ""
        
        while i >= 0 and j >= 0:
            sum_ = int(s1[i]) + int(s2[j]) + carry
            res += str(sum_ % 10)
            carry = sum_ // 10
            i -= 1
            j -= 1
        
        if i == 0:
            sum_ = int(s1[i]) + carry
            res += str(sum_ % 10)
            carry = sum_ // 10
        
        if carry > 0:
            res += str(carry)
        
        res = res.rstrip('0')
        
        return res[::-1]
    
    def minSum(self, arr):
        arr.sort()
        s1 = ""
        s2 = ""
        
        for i in range(0, len(arr), 2):
            s1 += str(arr[i])
        for i in range(1, len(arr), 2):
            s2 += str(arr[i])
        
        return self.addString(s1, s2)