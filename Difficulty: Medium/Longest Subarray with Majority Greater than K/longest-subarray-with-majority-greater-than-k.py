#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        prefIdx = {}
        sum, res = 0, 0
        for i in range(n):
            sum += 1 if arr[i] > k else -1
            if sum not in prefIdx:
                prefIdx[sum] = i
        if -n in prefIdx:
            return 0
        prefIdx[-n] = n
        for i in range(-n + 1, n + 1):
            if i not in prefIdx:
                prefIdx[i] = prefIdx[i - 1]
            else:
                prefIdx[i] = min(prefIdx[i], prefIdx[i - 1])
        sum = 0
        for i in range(n):
            sum += 1 if arr[i] > k else -1
            if sum > 0:
                res = i + 1
            else:
                res = max(res, i - prefIdx[sum - 1])
        return res
        # Code Here


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        
        arr = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        print("~")
        t -= 1
# } Driver Code Ends