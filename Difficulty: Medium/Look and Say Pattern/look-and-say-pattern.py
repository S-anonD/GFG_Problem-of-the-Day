class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        curr = "1"
        for i in range(2, n + 1):
            nextStr = ""
            cnt = 1
            for j in range(1, len(curr)):
                if curr[j] == curr[j - 1]:
                    cnt += 1
                else:
                    nextStr += str(cnt) + curr[j - 1]
                    cnt = 1
            nextStr += str(cnt) + curr[-1]
            curr = nextStr
        return curr
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countAndSay(n))

        print("~")
# } Driver Code Ends