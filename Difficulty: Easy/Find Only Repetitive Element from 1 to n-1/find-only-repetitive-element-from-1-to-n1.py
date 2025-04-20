#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        arr.sort()
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return arr[i]
        #code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        print(ob.findDuplicate(arr))
        print("~")

# } Driver Code Ends