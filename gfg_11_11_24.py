# 11/11/24
# Make array elements unique

class Solution:
    def minIncrements(self, arr):
        arr.sort()
        count = 0
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                count += arr[i-1] + 1 - arr[i]
                arr[i] = arr[i-1] + 1
        return count