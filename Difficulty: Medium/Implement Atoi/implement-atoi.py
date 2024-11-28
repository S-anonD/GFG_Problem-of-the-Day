#User function template for Python
class Solution:
    def myAtoi(self, s):
        check = 2**31
        res = 0
        i = 0
        sign = 1
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        while i < len(s) and ('0' <= s[i] <= '9'):
            res = 10 * res + (ord(s[i]) - ord('0'))
            if res > check:
                if sign == 1:
                    return check - 1
                else:
                    return sign * check
            i += 1
        return res * sign
        # Code here


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends