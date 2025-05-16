class Solution:
	def sortArray(self, arr, A, B, C):
	    arrtosort = []
	    for i in range(len(arr)):
	        e = A * arr[i] ** 2 + B * arr[i] + C
	        arrtosort.append(e)
	    return sorted(arrtosort)
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        a = int(input())
        b = int(input())
        c = int(input())

        ob = Solution()
        ans = ob.sortArray(arr, a, b, c)
        print(' '.join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends