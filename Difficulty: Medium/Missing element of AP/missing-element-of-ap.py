#User function Template for python3

class Solution:
    def findMissing(self, arr):
        n = len(arr)
        diff1 = arr[1] - arr[0]
        diff2 = arr[-1] - arr[-2]
        diff3 = (arr[-1] - arr[0]) // n
        if diff1 == diff2:
            diff = diff1
        elif diff1 == diff3:
            diff = diff1
        else:
            diff = diff2
        if diff == 0:
            return arr[0]
        res = self.findMissingUtil(arr, 0, n - 1, diff)
        if res == sys.maxsize:
            return arr[0] + n * diff
        else:
            return res
        # code here
    
    def findMissingUtil(self, arr, low, high, diff):
        if high <= low:
      	    return sys.maxsize
        mid = (low + high) // 2
        if arr[mid + 1] - arr[mid] != diff:
            return arr[mid] + diff
        if mid > 0 and arr[mid] - arr[mid - 1] != diff:
            return arr[mid - 1] + diff
        if arr[mid] == arr[0] + mid * diff:
            return self.findMissingUtil(arr, mid + 1, high, diff)
        return self.findMissingUtil(arr, low, mid - 1, diff)

import sys

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
import math


def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    solution = Solution()

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        print(solution.findMissing(arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends