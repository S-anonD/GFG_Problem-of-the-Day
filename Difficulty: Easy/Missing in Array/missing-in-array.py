class Solution:
    def missingNum(self, arr):
        if max(arr) == len(arr):
            return len(arr) + 1
        arr1 = set(arr)
        arr2 = set(range(1, max(arr) + 1))
        for x in arr2.difference(arr1):
            return x
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNum(arr)
    print(s)

    print("~")
# } Driver Code Ends