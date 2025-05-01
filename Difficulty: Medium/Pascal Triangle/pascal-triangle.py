#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self, n):
	    n -= 1
	    res = []
	    prev = 1
	    res.append(prev)
	    for i in range(1, n + 1):
	        curr = (prev * (n - i + 1)) // i
	        res.append(curr)
	        prev = curr
	    return res
	    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.nthRowOfPascalTriangle(n)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc - 1
        print("~")
# } Driver Code Ends