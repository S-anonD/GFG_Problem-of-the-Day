# 01/11/24
# Swap and Maximise

class Solution:
    def maxSum(self,arr):
        arr.sort()
        i, j = 0, len(arr)-1
        maxsum = 0
        while i < j:
            maxsum += arr[j] - arr[i]
            maxsum += arr[j] - arr[i+1]
            i += 1
            j -= 1
        return maxsum + (arr[int(len(arr)/2)] - arr[0])