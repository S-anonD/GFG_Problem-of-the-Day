# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):
        mp = {}
        res, prefSum = 0, 0
        for i in range(len(arr)):
            prefSum += arr[i]
            if prefSum == k:
                res = i + 1
            elif (prefSum - k) in mp:
                res = max(res, i - mp[prefSum - k])
            if prefSum not in mp:
                mp[prefSum] = i
        return res
        # code here
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends