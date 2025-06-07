class Solution:
    def isSumString (self, s):
        n = len(s)
        for len1 in range(1, n):
            for len2 in range(1, n - len1):
                if self.checkSequence(s, 0, len1, len2):
                    return True
        return False
    
    def addStrings(self, num1, num2):
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        len1 = len(num1)
        len2 = len(num2)
        sum = ""
        carry = 0
        for i in range(len2):
            d1 = ord(num1[len1 - 1 - i]) - ord('0')
            d2 = ord(num2[len2 - 1 - i]) - ord('0')
            digit = (d1 + d2 + carry) % 10
            carry = (d1 + d2 + carry) // 10
            sum = chr(digit + ord('0')) + sum
        for i in range(len2, len1):
            d = ord(num1[len1 - 1 - i]) - ord('0')
            digit = (d + carry) % 10
            carry = (d + carry) // 10
            sum = chr(digit + ord('0')) + sum
        if carry:
            sum = chr(carry + ord('0')) + sum
        return sum
    
    def checkSequence(self, s, start, len1, len2):
        part1 = s[start:start + len1]
        part2 = s[start + len1:start + len1 + len2]
        expectedSum = self.addStrings(part1, part2)
        sumLen = len(expectedSum)
        if start + len1 + len2 + sumLen > len(s):
            return False
        if expectedSum == s[start + len1 + len2 : start + len1 + len2 + sumLen]:
            if start + len1 + len2 + sumLen == len(s):
                return True
            return self.checkSequence(s, start + len1, len2, sumLen)
        return False
        # code here 