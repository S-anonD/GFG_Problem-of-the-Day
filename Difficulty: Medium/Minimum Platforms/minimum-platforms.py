#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        n = len(arr)
        res = 0
        arr.sort()
        dep.sort()
        j = 0
        cnt = 0
        for i in range(n):
            while j < n and dep[j] < arr[i]:
                cnt -= 1
                j += 1
            cnt += 1
            res = max(res, cnt)
        return res
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(arrival, departure))
        print("~")

# } Driver Code Ends