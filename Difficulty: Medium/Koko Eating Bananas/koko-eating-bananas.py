#User function Template for python3

class Solution:
    def kokoEat(self,arr,k):
        lo = 1
        hi = max(arr)
        res = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.check(arr, mid, k) == True:
                hi = mid - 1
                res = mid
            else:
                lo = mid + 1
        return res
    
    def check(self, arr, mid, k):
        hours = 0
        for i in range(len(arr)):
            hours += arr[i] // mid
            if arr[i] % mid != 0:
                hours += 1
        return hours <= k
        # Code here