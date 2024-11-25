#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
	    n = len(arr)
	    currmax = arr[0]
	    currmin = arr[0]
	    maxp = arr[0]
	    
	    for i in range(1, n):
	        temp = max(arr[i], arr[i] * currmax, arr[i] * currmin)
	        currmin = min(arr[i], arr[i] * currmax, arr[i] * currmin)
	        currmax = temp
	        maxp = max(maxp, currmax)

	    return maxp
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends