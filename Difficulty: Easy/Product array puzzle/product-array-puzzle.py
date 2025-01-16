#User function Template for python3
import math
class Solution:
    def productExceptSelf(self, arr):
        if arr.count(0) > 1:
            return [0] * len(arr)
        res = []
        p = math.prod(arr)
        for i in range(len(arr)):
            if arr[i] == 0:
                temp = arr.copy()
                temp.remove(0)
                res.append(math.prod(temp))
            else:
                res.append(int(p/arr[i]))
        return res
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends