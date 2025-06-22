class Solution:
    def minSum(self, arr):
        count = [0] * 10
        for num in arr:
            count[num] += 1
        s1 = []
        s2 = []
        firstNum = True
        for digit in range(10):
            while count[digit] > 0:
                if firstNum:
                    if not (len(s1) == 0 and digit == 0):
                        s1.append(str(digit))
                    firstNum = False
                else:
                    if not (len(s2) == 0 and digit == 0):
                        s2.append(str(digit))
                    firstNum = True
                count[digit] -= 1
        if not s1:
            s1.append("0")
        if not s2:
            s2.append("0")
        return self.addString(''.join(s1), ''.join(s2))
    
    def addString(self, s1, s2):
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry > 0:
            total = carry
            if i >= 0:
                total += int(s1[i])
            if j >= 0:
                total += int(s2[j])
            res.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1
        while res and res[-1] == '0':
            res.pop()
        return ''.join(reversed(res)) if res else "0"
        # code here