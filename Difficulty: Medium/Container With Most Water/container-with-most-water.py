
class Solution:
    def maxWater(self, arr):
        l, r = 0, len(arr) - 1
        quant = 0
        while l < r:
            water = min(arr[l], arr[r]) * (r - l)
            quant = max(quant, water)
            if arr[l] < arr[r]:
                l += 1
            else:
                r -= 1
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