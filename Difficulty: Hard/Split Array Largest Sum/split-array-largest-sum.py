class Solution:
    def splitArray(self, arr, k):
        n = len(arr)
        start, end = max(arr), sum(arr)
        ans = 0
        while start <= end:
            mid = (start + end) // 2
            if self.check(mid, arr, k):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
    
    def check(self, mid, arr, k):
        n = len(arr)
        count, total = 0, 0
        for num in arr:
            if num > mid:
                return False
            total += num
            if total > mid:
                count += 1
                total = num
        count += 1
        return count <= k
        # code here
        