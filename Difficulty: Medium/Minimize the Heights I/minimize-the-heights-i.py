#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        n = len(arr)
        arr.sort()
        res = arr[n-1] - arr[0]
        for i in range(1, n):
            minH = min(arr[0]+k, arr[i]-k)
            maxH = max(arr[i-1]+k, arr[n-1]-k)
            res = min(res, maxH-minH)
        return res
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends
