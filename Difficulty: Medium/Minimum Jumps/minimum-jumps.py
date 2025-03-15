class Solution:
	def minJumps(self, arr):
	    n = len(arr)
	    if arr[0] == 0:
	        return -1
	    maxreach, curreach = 0, 0
	    jump = 0
	    for i in range(n):
	        maxreach = max(maxreach, i + arr[i])
	        if maxreach >= n - 1:
	            return jump + 1
	        if i == curreach:
	            if i == maxreach:
	                return -1
	            else:
	                jump += 1
	                curreach = maxreach
	    return -1
	    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends