class Solution:  
    def findMaxSum(self,arr):
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        secondlast = 0
        last = arr[0]
        res = 0
        for i in range(1, n):
            res = max(arr[i] + secondlast, last)
            secondlast = last
            last = res
        return res
        # code here


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends