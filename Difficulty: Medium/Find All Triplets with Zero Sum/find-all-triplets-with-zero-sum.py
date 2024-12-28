#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        resSet = set()
        n = len(arr)
        mp = {}
        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                if s not in mp:
                    mp[s] = []
                mp[s].append((i, j))
        for i in range(n):
            rem = -arr[i]
            if rem in mp:
                for p in mp[rem]:
                    if p[0] != i and p[1] != i:
                        curr = sorted([i, p[0], p[1]])
                        resSet.add(tuple(curr))
        return [list(triplet) for triplet in resSet]
        # Your code here

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends