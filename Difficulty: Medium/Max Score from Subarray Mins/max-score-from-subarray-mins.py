class Solution:
    def maxSum(self, arr):
        n = len(arr)
        res = arr[0] + arr[1]
        for i in range(1, n - 1):
            res = max(res, arr[i] + arr[i + 1])
        return res
        # code here
        
    
