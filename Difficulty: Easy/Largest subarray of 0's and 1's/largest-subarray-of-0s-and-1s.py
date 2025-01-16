class Solution:
    def maxLen(self, arr):
        res = 0
        count = {0:-1}
        sum = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                sum += 1
            else:
                sum -= 1
            if sum in count:
                res = max(res, i - count[sum])
            else:
                count[sum] = i
        return res
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends