#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        span = [0] * n
        stk = []
        for i in range(n):
            while stk and arr[stk[-1]] <= arr[i]:
                stk.pop()
            if not stk:
                span[i] = i + 1
            else:
                span[i] = i - stk[-1]
            stk.append(i)
        return span
        #write code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends