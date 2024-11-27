#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        n = len(arr)
        for i in range(n):
            while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
                temp = arr[i]
                arr[i] = arr[arr[i] - 1]
                arr[temp - 1] = temp
        
        for i in range(1, n + 1):
            if i != arr[i - 1]:
                return i
        
        return n + 1
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends