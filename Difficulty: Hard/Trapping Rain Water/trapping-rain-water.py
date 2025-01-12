
class Solution:
    def maxWater(self, arr):
        l, r = 1, len(arr) - 2
        lmax, rmax = arr[l - 1], arr[r + 1]
        quant = 0
        while l <= r:
            if rmax <= lmax:
                quant += max(0, rmax - arr[r])
                rmax = max(rmax, arr[r])
                r -= 1
            else:
                quant += max(0, lmax - arr[l])
                lmax = max(lmax, arr[l])
                l += 1
        return quant
        # code here


#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends