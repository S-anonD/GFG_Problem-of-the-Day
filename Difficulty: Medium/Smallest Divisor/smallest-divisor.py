class Solution:
    def smallestDivisor(self, arr, k):
        low = 1
        high = max(arr)
        res = -1
        while low <= high:
            mid = low + (high - low) // 2
            sum = 0
            for ele in arr:
                sum += (ele + mid - 1) // mid
            if sum <= k:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
        # Code here