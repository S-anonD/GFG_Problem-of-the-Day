#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
	    n = len(arr)
	    arr.sort()
	    left, right = 0, n - 1
	    while left < right:
	        sum = arr[left] + arr[right]
	        if sum == target:
	            return True
	        elif sum < target:
	            left += 1
	        else:
	            right -= 1
	    return False
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends