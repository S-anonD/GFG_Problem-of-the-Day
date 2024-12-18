class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        if k > len(arr):
            return -1
        if k == 1:
            return sum(arr)
        lo = max(arr)
        hi = sum(arr)
        res = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.check(arr, k, mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res
    
    def check(self, arr, k, pageLimit):
        cnt, pageSum = 1, 0
        for pages in arr:
            if pageSum + pages > pageLimit:
                cnt += 1
                pageSum = pages
            else:
                pageSum += pages
        return cnt <= k
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends