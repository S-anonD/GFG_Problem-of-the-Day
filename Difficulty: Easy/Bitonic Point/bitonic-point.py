#User function Template for python3
class Solution:

	def findMaximum(self, arr):
	    n = len(arr)
	    if n == 1 or arr[0] > arr[1]:
	        return arr[0]
	    if arr[n - 1] > arr[n - 2]:
	        return arr[n - 1]
	    lo, hi = 1, n - 2
	    while lo <= hi:
	        mid = lo + (hi - lo) // 2
	        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
	            return arr[mid]
	        if arr[mid] < arr[mid + 1]:
	            lo = mid + 1
	        else:
	            hi = mid - 1
	    return arr[hi]
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends