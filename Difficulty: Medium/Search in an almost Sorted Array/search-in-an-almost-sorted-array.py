#{ 
 # Driver Code Starts

# } Driver Code Ends

#User function Template for python3
class Solution:
    def findTarget(self, arr, target):
        l, r = 0, len(arr) - 1
        while r >= l:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                return mid
            if mid > l and arr[mid - 1] == target:
                return mid - 1
            if mid < r and arr[mid + 1] == target:
                return mid + 1
            if arr[mid] > target:
                r = mid - 2
            else:
                l = mid + 2
        return -1
        # code here


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())  # Number of test cases

    for _ in range(t):
        arr = list(map(int, input().strip().split()))  # Read the array
        target = int(input().strip())  # Read the target

        sln = Solution()
        ans = sln.findTarget(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends