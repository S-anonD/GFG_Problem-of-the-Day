
class Solution:
    def decodedString(self, s):
        numst = []
        chst = []
        temp = ""
        res = ""
        i = 0
        while i < len(s):
            cnt = 0
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    cnt = cnt * 10 + int(s[i])
                    i += 1
                i -= 1
                numst.append(cnt)
            elif s[i] == "]":
                temp = ""
                cnt = numst.pop()
                while chst[-1] != "[":
                    temp = chst.pop() + temp
                chst.pop()
                res = temp * cnt
                for c in res:
                    chst.append(c)
                res = ""
            else:
                chst.append(s[i])
            i += 1
        while chst:
            res = chst.pop() + res
        return res
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends