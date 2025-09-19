class Solution:
    def minParentheses(self, s):
        balance = 0
        unmatchedClosing = 0
        for c in s:
            if c == "(":
                balance += 1
            elif c == ")":
                balance -= 1
                if balance < 0:
                    unmatchedClosing += 1
                    balance = 0
        return balance + unmatchedClosing
        # code here
        
        